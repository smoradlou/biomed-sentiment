#!/usr/bin/env python3
# -- coding: utf-8 --
# For talking to GPT-J api
import json
import requests

# For NLPAug models
import nlpaug.augmenter.char as nac
import nlpaug.augmenter.word as naw
import nlpaug.augmenter.sentence as nas
import nlpaug.flow as nafc

from nlpaug.util import Action
def augment_w_gptj(text, temprature=.4):
    print(text)
    response = requests.post(
        "https://bellard.org/textsynth/api/v1/engines/gptj_6B/completions",
        headers={
            "Connection": "keep-alive",
            "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
            "sec-ch-ua-platform": '"Linux"',
            "Content-Type": "application/json",
            "Accept": "/",
            "Origin": "https://bellard.org",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://bellard.org/textsynth/",
            "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8,de;q=0.7,fr;q=0.6",
        },
        data=json.dumps(
            {
                "prompt": text + "\n\nIn other words,",
                "temperature": temprature, # lower temperatures to stay close to the original and not get too creative
                "top_k": 40,
                "top_p": 0.9,
                "seed": 0,
                "stream": False,
            }
        ),
    ).json()
    return response


