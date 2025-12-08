# Model Card

## Model Description

**Input:** 
The model takes structured metadata features about digital content releases, including:  
- Hour of release (float)  
- Day of week (integer)  
- Weekend indicator (binary)  
- Title length (integer)  
- Tag count (integer)  
- Platform (categorical: YouTube or OTT)  
- Region (categorical, for YouTube datasets)

**Output:**  
A binary classification label:  
- `0` = Low engagement (below median engagement rate)  
- `1` = High engagement (above median engagement rate)

**Model Architecture:**  
We use tree-based ensemble classifiers (RandomForest and XGBoost) within a scikit-learn pipeline. These models were chosen for their ability to handle mixed feature types, robustness to noise, and interpretability via feature importance.


## Performance

Performance was evaluated using **5-fold stratified cross-validation** and measured with **macro F1 score** to balance both classes. Test set metrics were reported for each dataset.

| Dataset                               | Best CV F1 (macro) | Test Accuracy | Class 0 F1 | Class 1 F1 |
|---------------------------------------|--------------------|---------------|-------------|-------------|
| GB_youtube_trending_data.csv          | 0.725              | 0.623         | 0.613       | 0.632       |
| Youtube_Videos.csv                    | 0.716              | 0.585         | 0.683       | 0.400       |
| Content Scheduling for Engagement.csv | 0.563              | 0.460         | 0.471       | 0.449       |

Feature importance analysis highlighted `title_len`, `tag_count`, and `hour` as dominant predictors in YouTube datasets, while `hour` and `dayofweek` were most important in OTT scheduling.

## Limitations

- **Class imbalance:** The model performs better at identifying low-engagement content than high-engagement content, especially in larger YouTube datasets.  
- **Feature scope:** OTT dataset has limited features (no tags, minimal title metadata), restricting predictive power.  
- **Generalisation:** Results are dataset-specific and may not generalize to other platforms or time periods without retraining.  
- **Temporal context:** External factors (holidays, cultural events) are not captured, which may influence engagement.


## Trade-offs

- **Interpretability vs. accuracy:** Tree-based models provide feature importance for transparency but may underperform compared to deep learning on larger, richer datasets.  
- **Recall vs. precision:** Optimising for macro F1 balances classes but sacrifices recall for high-engagement videos in some datasets.  
- **Dataset size vs. robustness:** Smaller OTT dataset confirms timing importance but yields lower accuracy due to limited sample size.  
- **Cross-platform consistency:** While timing features are consistently predictive, platform-specific metadata (tags, regions) drive differences in performance.
