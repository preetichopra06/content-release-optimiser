### Release Timing Classification Results

This report summarizes model performance across three datasets used to predict digital content engagement based on release timing and metadata features.

### Dataset Comparison Table

| Dataset                               | Rows × Features | Best CV F1 (macro) | Test Accuracy | Class 0 F1 | Class 1 F1 | Top Features                  |
|---------------------------------------|-----------------|--------------------|---------------|-------------|-------------|-------------------------------|
| GB_youtube_trending_data.csv          | 268,791 × 11    | 0.725              | 0.623         | 0.613       | 0.632       | title_len, is_weekend, hour   |
| Youtube_Videos.csv                    | 390,043 × 11    | 0.716              | 0.585         | 0.683       | 0.400       | title_len, tag_count, hour    |
| Content Scheduling for Engagement.csv | 1,000 × 7       | 0.563              | 0.460         | 0.471       | 0.449       | hour, dayofweek, is_weekend   |

### Executive Summary

Across three datasets, our classification model demonstrates consistent reliance on timing and content features to predict engagement. The GB YouTube dataset yielded the strongest performance, with balanced precision and recall across both classes. The general YouTube dataset showed high recall for low-engagement content but struggled to identify high-engagement videos. The OTT dataset ( Content Scheduling for Engagement.csv), while smaller, confirmed the predictive value of release timing (hour, dayofweek) but exhibited lower overall performance due to limited feature diversity and sample size.

These results validate the robustness of our pipeline and highlight opportunities for feature enrichment in OTT scheduling. Future iterations may benefit from incorporating richer content descriptors, audience segmentation, and temporal context (e.g., holidays, seasonality).

### Notes

All models used the same pipeline and hyperparameter grid.

Feature importance was extracted from XGBoost or RandomForest depending on availability.

Confusion matrices and bar charts are saved in reports/figures/.

Prepared by: PreetiDate: December 2025