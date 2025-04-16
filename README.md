# Sentiment Analysis Aardy.com

This project implements sentiment analysis on Aardy customer reviews using various Natural Language Processing (NLP) techniques and machine learning algorithms. The goal is to classify customer reviews into three sentiment categories: Positive, Neutral, and Negative.

## 📁 Project Structure

- `scrapping.py`: Script for collecting review data from related sources.
- `aardy_reviews_clean.csv`: Dataset of cleaned customer reviews.
- `sentiment_analysis_aardy_Achmad_Fariz.ipynb`: Main notebook that includes the entire analysis process, from data preprocessing to model evaluation.
- `requirements.txt`: List of required Python libraries for the project.
- `models/`: Folder containing the saved models used for sentiment prediction (`model_dense_layer.h5`, `model_logistic_regression.h5`, etc.).
- `count_vectorizer_70.pkl`: The CountVectorizer object used to transform input text data for model prediction.

## 🚀 Getting Started

To get started with this project, you need to clone the repository and install the necessary dependencies.

### Clone the Repository

```bash
git clone https://github.com/faRIZky/sentiment_analysis_aardy.git
cd sentiment_analysis_aardy
```

### Install Dependencies

It is recommended to use a virtual environment to install the dependencies:

```bash
pip install -r requirements.txt
```
