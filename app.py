#!/usr/bin/python
# -*- coding: utf-8 -*-
from textblob import TextBlob
from typing import List


def hello(name: str):
    return f"Hello {name}"


def extract_sentiment(text: str):
    text = TextBlob(text)
    return text.sentiment.polarity


def text_contain_word(word: str, text: str):
    return word in text


def bubble_sort(tab: List[int]):
    ret_tab = tab.copy()
    change = True
    while change:
        change = False
        for i in range(len(tab)-1):
            if ret_tab[i] > ret_tab[i+1]:
                ret_tab[i], ret_tab[i+1] = ret_tab[i+1], ret_tab[i]
                change = True
    return ret_tab
