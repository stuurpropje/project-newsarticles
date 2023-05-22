# Applying a sentiment analysis on the 100 largest companies based on market cap
## Table of Contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Setup](#setup)
* [Data cleaning](#data-cleaning)
* [Topic Modelling](#topic-modelling)
* [Future Possibilities](#future-posibilities)
* [Linear regression](#linear-regression)
* [Sources](#sources)

## Introduction
The purpose of this project is to explore a potential relationship between media sentiment about companies and their market cap in a ranking.

## Technologies
SciSpacy
* Lemmatizer
NLTK
* Stop Word Remover

## Setup
This project requires some installations.

#### Data cleaning
```
$ python -m spacy download en_core_web_sm

```
#### Topic Modelling
```
$ pip install scispacy
$ pip install pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.4/en_core_sci_lg-0.2.4.tar.gz
$ pip install sklearn
$ pip install stop-words
$ pip install nltk
$ pip install ipywidgets
```

## Data cleaning
decreasing size of dataframes
stop word removing

### Topic modelling
filtering of only relevant articles of the companies

## Future Possibilities

### Sentiment analysis
Scikit-learn sentiment analysis

### Linear regression
Comparison between companies

## Sources
This project is based on the dataset created by Andrew Thompson, 2022 (https://components.one/datasets/all-the-news-2-news-articles-dataset/).

The code for topic modelling is taken from Daniel Wolfram's notebook on Kaggle (https://www.kaggle.com/code/danielwolffram/topic-modeling-finding-related-articles/notebook) 
and Nina Alblas (https://github.com/spcourse/transformation/blob/main/health-code-violations-1/10%20HealthCode.md).
