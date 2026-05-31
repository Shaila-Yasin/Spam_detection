# Email Spam Detection using Machine Learning

This project is a machine learning-based spam detection system that classifies messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) techniques. The model processes text data, cleans it, converts it into numerical features using TF-IDF vectorization, and then trains a classification algorithm (SVM / Naive Bayes) to detect spam messages.

---

## Project Overview

The goal of this project is to detect spam messages using text classification techniques. The model is trained on labeled SMS data and learns patterns that differentiate spam from normal messages.

---

## Workflow

1. Data Collection (SMS Spam Dataset)
2. Data Cleaning (lowercasing, removing punctuation)
3. Stopwords Removal
4. TF-IDF Vectorization
5. Model Training (SVM / Naive Bayes)
6. Model Evaluation
7. Model Saving using Joblib
8. Prediction on new messages

---

## Dataset

- SMS Spam Collection Dataset  
- Labels:
  - **ham** → Normal messages  
  - **spam** → Unwanted / promotional messages  

---

## Model Performance

- Accuracy: ~97%
- Strong performance in spam classification
- SVM performs slightly better than Naive Bayes in most cases

---

## Project Structure

email-spam-detector/
│
├── data/
│   └── spam.csv
│
├── models/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── notebooks/
│   └── spam_detection.ipynb
│
├── preprocessing.py
├── predict.py
├── test.py
├── requirements.txt
└── README.md

---

## How to Run

### 1. Clone the repository  
git clone https://github.com/your-username/email-spam-detector.git  
cd email-spam-detector  

### 2. Install dependencies  
pip install -r requirements.txt  

### 3. Run the prediction script  
python test.py  

### 4. Test Example  

Input:  
Free money win prize now!!!  

Output:  
Spam  

---

## Author

Developed by **Shaila Yasin**  
GitHub: https://github.com/Shaila-Yasin
