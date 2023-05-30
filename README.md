
# Exploratory Data Analysis of a Large Dataset 

## Table of Contents

* [Introduction](#introduction)
* [Project Overview](#project-overview)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Project Summary](#project-summary)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)

## Introduction

This project aims to process the dataset of all-the-news-2-1.csv 
by [Andrew Thompson (2022)](https://components.one/datasets/all-the-news-2-news-articles-dataset/) for textual analysis.
The process for the textual analysis is performed through several natural language processing (NLP) libraries such as SciSpacy, NLTK or scikitlearn. 

The results of the dataset processing can be found in the Jupyter Notebook file [results.ipynb](/results.ipynb).
This notebook provides insights and visualizations of the processing steps performed on the dataset and the results of this processing.
The results and findings can be used for a better understanding of pre-processing steps for NLP, potential roadblocks and possible solutions.

## Project Overview

This project aims to analyze a large dataset of news articles to gain insights into the underlying text data. 
The analysis involves various NLP techniques, including data cleaning, lemmatization, vectorization, and topic modeling.
By performing these steps, the project seeks to uncover patterns which form latent topics presented in the news articles.

## Requirements

* Python 3.10.6 or later
* NLTK: Stop Word Remover
* SciSpacy
    * Lemmatizer
    * jensenshannon
* sklearn:
    * CountVectorizer
    * LatentDirichletAllocation
* Pandas library
* NumPy library
* Matplotlib
* ipynb
* iPywidgets
* iPython
* joblib
* tqdm

## Installation

To install the required libraries, the following commands are to be executed:

```
$ python3 -m spacy download en_core_web_sm
$ pip install nltk
$ python3 -c "import nltk; nltk.download('stopwords')"
$ pip install scispacy
$ pip install pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.4/en_core_sci_lg-0.2.4.tar.gz
$ pip install sklearn
$ pip install pandas
$ pip install numpy
$ pip install matplotlib
$ pip install ipynb
$ pip install ipywidgets
$ pip install iPython
$ pip install joblib
$ pip install tqdm
```

## Usage

1. Download the project files from the [GitHub repository](https://github.com/minprog-platforms/project-stuurpropje/archive/refs/heads/main.zip). Ensure the target directory maintains the same file structure as the GitHub repository.
2. Download [all-the-news-2-1.csv](https://components.one/datasets/all-the-news-2-news-articles-dataset/)
    and place it in the csv/ subdirectory.
3. Pre-processing steps
    - Run the load.py module.
    - Run the data_cleaning.py module.
    - Run the random_sample.py module.  
        > Note: If you'd like to use the entire dataset, change the sample size argument to 1.0. This means no sample is taken. Other sample sizes are of course also possible.  
        
        > Warning: The following modules are very processing-power and time intensive. Taking a random sample allows for faster file processing.

    - Run the lemmatization.py module.

        > Warning: This module has a **long** runtime. 10 cores with an average clock speed of 2.1 GHz required 6 hours to finish.

        > Note: Due to the long runtime requirements for this module, it is possible to intermittently execute this module. Simply run the module again and it will pick off where it was stopped.

4. Topic modeling steps
    - Run the vectorizer.py module.
        > Warning: Unlike lemmatization.py, this module does **not** support intermittent execution. Ensure the module can fully complete its work before running it.
        
        > Note: This module has a runtime around 1/4th the runtime requirement of lemmatization.py.  
        
    - Open the topic_modelling.ipynb Jupyter Notebook file and ensure that no errors occur.
    - Open the results.ipynb Jupyter Notebook file and run it. results.ipynb contains the visualisations and further explanations to modules and functions. 

## Project Structure

The project follows the following directory structure:

csv: A folder containing the datafile all-the-news-2-1.csv and all its derivate files.  
[datacleaning:](datacleaning/) Contains all pre-processing modules up to lemmatization.py.  
[topicmodeling](topicmodeling/) Contains a secondary csv for vectorized datafiles and the vectorizer.py module.  topicmodeling/csv: A folder containing the vectorized datafiles, the LDA files and the normalized topic distribution files.

## Project Summary

The processing of the dataset was done through several steps:
- Removing stop words from articles.
- Applying lemmatization to reduce words to their base form, improving text representation.
- Utilizing vectorization techniques to convert text data into numerical features.
- Conducting topic modeling to identify latent themes and topics in the news articles.

For detailed insights and visualizations, refer to the [results.ipynb](/results.ipynb) Jupyter Notebook in the root directory of this repository.

## Acknowledgements

We would like to thank Andrew Thompson who created the dataset processed in this project, as well as Daniel Wolfram for the foundations on which the code of this project is built.

This project is based on the dataset created by [(Andrew Thompson, 2022)](https://components.one/datasets/all-the-news-2-news-articles-dataset/).

The code in this project is based on the code written by [Daniel Wolfram (2022)](https://www.kaggle.com/code/danielwolffram/topic-modeling-finding-related-articles/notebook) in his notebook on Kaggle.

## Contact

For any inquiries or feedback, please contact me, Niels, at niels.huang@student.uva.nl.



