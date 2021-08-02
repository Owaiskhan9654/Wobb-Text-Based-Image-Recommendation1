import numpy as np
import pandas as pd
import nltk.data
import pickle
from rank_bm25 import BM25Okapi


def rank(query):
    Image_Mappings = [
        "Cute 15 year Old chinese Girl (1)",
        "Cute 15 year Old chinese Girl 3",
        "Cute 15 year Old chinese Girl",
        "Cute 15 year Old chinese Girl",
        "old Indian Man 2",
        "old Indian Man 3",
        "old Indian Man",
        "Young American Boy 2",
        "Young American Boy 3",
        "Young American Boy"

    ]

    tokenized_corpus = [doc.split(" ") for doc in Image_Mappings]

    bm25 = BM25Okapi(tokenized_corpus)

    tokenized_query = query.split(" ")

    list1 = bm25.get_top_n(tokenized_query, Image_Mappings, n=3)
    return list1,query
