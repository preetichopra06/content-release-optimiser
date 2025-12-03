# Optimising Digital Content Release Timing for Engagement

## Overview
This project builds machine learning models to predict whether digital content will achieve high or low engagement based on release timing and simple metadata. Using datasets from YouTube and OTT platforms, we trained classification pipelines that learn patterns from features such as hour of release, day of week, title length, and tag count. Results show that timing and content cues consistently influence engagement: the YouTube Trending dataset achieved the strongest balance across classes, while general YouTube and OTT data highlighted challenges in detecting high‑engagement items. These findings demonstrate both robustness and opportunities for richer feature design.

## Problem Statement
How can we optimise the timing and targeting of digital content releases to maximise user engagement across platforms and regions?

## DATA
We used three datasets to study how release timing and metadata influence digital content engagement:
- **GB YouTube Trending Data** (Kaggle, 2017–2018): 268k+ videos with views, likes, comments, and trending dates.
- **YouTube_Videos.csv** (Kaggle, 2020): 390k+ videos with metadata including title length and tags.
- **Content Scheduling for Engagement.csv** (synthetic OTT dataset): 1,000 rows simulating release times, day of week, and viewership metrics.

## Data Sources
- Content Scheduling for Maximizing Engagement  
  [Kaggle Dataset](https://www.kaggle.com/datasets/aashwinkumar/ott-content-scheduling-for-maximizing-engagement)  
- GB YouTube Trending Data  
  [Kaggle Dataset](https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset)  
- YouTube Video Trends & Non-Trends  
  [Kaggle Dataset](https://www.kaggle.com/datasets/muhammedchreiki/youtube-video-trends-and-non-trends-dataset)  


## MODEL
We trained binary classification models to predict high vs. low engagement. We chose **XGBoost** and **RandomForest** because they handle mixed feature types, provide feature importance for interpretability, and perform well on imbalanced datasets. These models allow us to benchmark across platforms while keeping workflows transparent and reproducible.

## HYPERPARAMETER OPTIMISATION
We optimised hyperparameters using **GridSearchCV** with 5‑fold stratified cross‑validation, targeting **macro F1 score** to balance performance across both classes. Key hyperparameters included:
- `n_estimators` (number of trees)
- `max_depth` (tree depth)
- `learning_rate` (for XGBoost)
- `min_samples_split` and `min_samples_leaf` (for RandomForest)

This ensured robust tuning without overfitting.

## RESULTS
Across datasets, timing and content features consistently influenced engagement:
- **GB YouTube Trending:** Best CV F1 = 0.725, balanced performance across classes.
- **YouTube_Videos:** Best CV F1 = 0.716, strong recall for low‑engagement but weaker for high‑engagement.
- **OTT Scheduling:** Best CV F1 = 0.563, smaller dataset confirmed timing importance but limited feature diversity.

Top features included `title_len`, `tag_count`, `hour`, and `is_weekend`.  
These results highlight the predictive value of release timing and metadata, while showing opportunities to enrich OTT datasets with more content descriptors.

![Screenshot](reports/figures/confusion_matrix.png)

### Repository Structue

optimising-content-release/
│
├── README.md                  # Project overview, setup, non-technical summary, data sources
│
│
├── data/
│   ├── sample/                 # Small sample datasets for quick testing
│   │   ├── Content Scheduling for Maximizing Engagement.csv
│   │   ├── GB_youtube_trending_data.csv
│   │   └── Youtube_Videos.csv
│   └── README.md               # Links to full datasets on Kaggle
│
├── docs/
│   ├── data_sheet.md           # Datasheet documenting datasets
│   └── model_card.md           # Model card documenting model details
│
├── notebooks/
│   └── 01_release_timing_classification.ipynb
│
├── src/
│   ├── data.py                 # Data loading, preprocessing, labeling functions
│
├── reports/
│   ├── figures/                # Saved plots (confusion matrix, feature importance)
│   └── results.md              # Summary of metrics and findings


## (OPTIONAL: CONTACT DETAILS)
Prepared by Preeti  
Email: preeti_chopra06@yahoo.co.in
LinkedIn: https://www.linkedin.com/in/preeti-chopra-09557743/
