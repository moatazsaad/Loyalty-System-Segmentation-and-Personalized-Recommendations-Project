# Loyalty System Segmentation and Recommendations

**Visit the app:** [Loyalty System Segmentation and Personalized Recommendations](https://loyalty-system-segmentation-and-personalized-recommendations-p.streamlit.app/)

This project uses DBSCAN clustering to segment users based on transaction behavior and offers personalized merchant recommendations.

---

## Overview

This repository contains a Jupyter notebook focused on customer segmentation and personalized recommendations using transactional data from a loyalty system.

---

## Setup and Libraries

- **Libraries Used**: Pandas, NumPy, Plotly Express, Scikit-learn
- **Data**: `Cleaned_Data_Merchant_Level.csv`

---

## Exploratory Data Analysis (EDA)

- Descriptive statistics and visualizations for transaction rank, points, transaction age, customer age, and transaction categories.

---

## Data Preprocessing

- Outlier handling for points above 100,000.
- Binning and transformation of transaction age (`Trx_Age`) for clustering.

---

## Clustering with DBSCAN

- Application of DBSCAN algorithm for user segmentation based on transaction features.

---

## Personalized Recommendations

- Development of a function to recommend merchants based on user clusters.

---

## Streamlit Application

- Implementation of a Streamlit app (`streamlit_app.py`) for an interactive recommendation system.

---

## Usage

1. **Clone the repository**: git clone https://github.com/moatazsaad/Loyalty-System-Segmentation-and-Personalized-Recommendations-Project.git
2. **Navigate to the project directory**: cd Loyalty-System-Segmentation
3. **Install dependencies**: pip install -r requirements.txt
4. **Run the Streamlit app**: streamlit run streamlit_app.py
---

## Data

The dataset (`Cleaned_Data_Merchant_Level.csv`) includes transaction details such as transaction rank, points, transaction age, customer age, and categories.






