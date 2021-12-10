# -*- coding: utf-8 -*-
import time
import pandas as pd
from augment import augment_w_gptj
from sklearn.model_selection import train_test_split

df = pd.read_excel('../../data/sentences_with_sentiment.xlsx')
df['Polarity'] = df['Positive'] - df['Negative'] + 1
df['Augmentation'] = 0

X = df["Sentence"]
y = df["Polarity"]
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

rows_list = []

for i, example in X_train.iteritems(): # Only augmenting using the training to not accidentally leak the validation to training

    # Add the original
    example_dict = {}
    example_dict["Sentence"] = example
    example_dict["Augmentation"] = 0
    example_dict["Polarity"] = y_train[i]
    rows_list.append(example_dict)


    response = augment_w_gptj(example.encode("ascii", "ignore").decode())
    try:
        # Add first variation
        example_dict = {}
        variation_0 = response["text"].strip().split("\n\n")[0]
        if (variation_0 != example):
            example_dict["Sentence"] = variation_0
            example_dict["Augmentation"] = 1
            example_dict["Polarity"] = y_train[i]
            rows_list.append(example_dict)

        # Add second variation
        example_dict = {}
        variation_1 = response["text"].strip().split("\n\n")[1]
        if (variation_1 != example and variation_1 != variation_0):
            example_dict["Sentence"] = variation_1
            example_dict["Augmentation"] = 1
            example_dict["Polarity"] = y_train[i]
            rows_list.append(example_dict)

    except KeyError:
        print("Got to", i, "backing up")
        # Backup the work so far
        generative_aug_df = pd.DataFrame(rows_list)
        generative_aug_df.to_csv("../../data/train_augmented.csv")
        # Wait to free up requests
        print("Waiting 10 minutes...")
        time.sleep(600)
        # Try again once
        print("Trying again...")
        response = augment_w_gptj(example.encode("ascii", "ignore").decode()) # The api seems to have trouble with non-ascii
        try:
            # Add first variation
            example_dict = {}
            variation_0 = response["text"].strip().split("\n\n")[0]
            if (variation_0 != example):
                example_dict["Sentence"] = variation_0
                example_dict["Augmentation"] = 1
                example_dict["Polarity"] = y_train[i]
                rows_list.append(example_dict)
            # Add Second variation
            example_dict = {}
            variation_1 = response["text"].strip().split("\n\n")[1]
            if (variation_1 != example and variation_1 != variation_0):
                example_dict["Sentence"] = variation_1
                example_dict["Augmentation"] = 1
                example_dict["Polarity"] = y_train[i]
                rows_list.append(example_dict)
        except:
            print("Didn't get alternatives for index", i, ", skipping...")
            continue
        continue

generative_aug_df = pd.DataFrame(rows_list)
generative_aug_df.to_csv("../../data/train_augmented.csv")

