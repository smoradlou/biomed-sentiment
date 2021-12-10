# -*- coding: utf-8 -*-
import time
import pandas as pd
from sklearn.model_selection import train_test_split

import nlpaug.augmenter.word as naw
import nlpaug.augmenter.sentence as nas

import csv

df = pd.read_excel('../../data/sentences_with_sentiment.xlsx')
df['Polarity'] = df['Positive'] - df['Negative'] + 1
df['Augmentation'] = 0

X = df["Sentence"]
y = df["Polarity"]
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

X_train = list(X_train)
# SciBert word embeddings
aug = naw.ContextualWordEmbsAug(
    model_path='allenai/scibert_scivocab_uncased', action="insert")
scibert_augmented = aug.augment(X_train)

with open('../../data/train_aug_scibert.txt', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(zip(y_train, scibert_augmented))

# Back Translation
aug = naw.BackTranslationAug(
    from_model_name='facebook/wmt19-en-de',
    to_model_name='facebook/wmt19-de-en'
)
bt_augmented = aug.augment(X_train)

with open('../../data/train_aug_bt.txt', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(zip(y_train, bt_augmented))

