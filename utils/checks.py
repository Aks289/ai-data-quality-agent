import pandas as pd


def get_missing_values(df):
    return df.isnull().sum()


def get_duplicate_count(df):
    return df.duplicated().sum()


def get_datatypes(df):
    return df.dtypes


def get_quality_score(df):

    score = 100

    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    score -= min(missing * 0.1, 30)
    score -= min(duplicates * 2, 20)

    return max(round(score, 2), 0)