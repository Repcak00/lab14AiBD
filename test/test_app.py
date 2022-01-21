#!/usr/bin/python
# -*- coding: utf-8 -*-

from app import hello
from app import extract_sentiment
from app import text_contain_word
from app import bubble_sort
import pytest


def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want


testdata1 = ["I think today will be a great day", "What a great day!"]


@pytest.mark.parametrize('sample', testdata1)
def test_extract_sentiment(sample):
    sentiment = extract_sentiment(sample)
    assert sentiment > 0


testdata2 = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
]


@pytest.mark.parametrize('sample, word, expected_output', testdata2)
def test_text_contain_word(sample, word, expected_output):
    assert text_contain_word(word, sample) == expected_output


testdata_bubblesort = [([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]), ([5, 3, 2, 5, 1], [1, 2, 3, 5, 5]),
                       ([4, 2, 1, 5, 3], [1, 2, 3, 4, 5]), ([5, 5, 5, 1, 2], [1, 2, 5, 5, 5]),
                       ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])]


@pytest.mark.parametrize('argument, expected_output', testdata_bubblesort)
def test_bubblesort(argument, expected_output):
    assert bubble_sort(argument) == expected_output
