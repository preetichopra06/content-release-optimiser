# Datasheet for Datasets Used in Project

This datasheet documents the datasets included in this repository:  
1. Content Scheduling for Maximizing Engagement.csv  
2. GB_youtube_trending_data.csv  
3. Youtube_Videos.csv

## Motivation
- Purpose: These datasets are used to study how timing, platform, and content features influence digital engagement.  
- Intended use: Training and evaluating machine learning models that classify release windows into high vs low engagement.  
- Decisions supported: Scheduling recommendations for media distribution teams, benchmarking ML workflows, and exploring ethical/transparent model use.

## Composition
- Instances:
  - Content Scheduling for Maximizing Engagement.csv: OTT content metadata, scheduling info (time of day, day of week), engagement metrics (viewership, likes, shares, comments), demographics.  
  - GB_youtube_trending_data.csv: YouTube trending videos in Great Britain, including publish time, views, likes, comments, tags, and categories.  
  - Youtube_Videos.csv: General YouTube video metadata with engagement statistics, not limited to trending.  

- Size:  
  - OTT dataset: ~159 KB (few hundred rows).  
  - GB YouTube trending: ~several MB depending on sample size.  
  - Youtube_Videos: varies, typically thousands of rows.  

- Features:  
  - Time-based: publish time, day of week, hour, seasonality.  
  - Engagement: views, likes, comments, shares, ratings.  
  - Content: title, tags, category, duration.  
  - Demographics (OTT only): age, gender, location.  

- Labels:  
  - Engagement level (high vs low) created via thresholds (e.g., median engagement rate per region/platform).  
  - Trending vs non-trending (YouTube datasets).  

## Collection Process
- OTT dataset: Curated for research purposes, combining scheduling metadata with engagement outcomes.  
- YouTube datasets: Collected via YouTube API and Kaggle community contributions.  
- Timeframe:  
  - OTT dataset: synthetic/aggregated across multiple release windows.  
  - GB YouTube trending: covers trending videos over multiple years.  
  - Youtube_Videos: general sample across platforms.  

## Preprocessing
- Converted `publish_time` to UTC datetime.  
- Derived features: hour, day of week, week of year, weekend flag.  
- Calculated engagement rate = (likes + comments) / views.  
- Created binary label: high vs low engagement (threshold = median per region/platform).  
- Normalized categorical features (region, platform, genre).  
- Removed duplicates and handled missing values.  

## Sources
- Content Scheduling for Maximizing Engagement: [Kaggle Dataset](https://www.kaggle.com/datasets/aashwinkumar/ott-content-scheduling-for-maximizing-engagement)  
- GB YouTube Trending Data: [Kaggle Dataset](https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset)  
- YouTube Videos (Trends & Non-Trends): [Kaggle Dataset](https://www.kaggle.com/datasets/muhammedchreiki/youtube-video-trends-and-non-trends-dataset)  

---

## Uses
- Appropriate uses:  
  - Research on content scheduling and engagement.  
  - Benchmarking ML classification workflows.  
  - Educational demonstrations of datasheets and model cards.  

- Inappropriate uses:  
  - Predicting individual user behavior.  
  - Commercial deployment without retraining and validation.  
  - Sensitive demographic profiling without ethical review.  

## Distribution
- Availability: Public datasets hosted on Kaggle.  
- Licensing: Kaggle community datasets (research use).  
- Access: Linked above.  

## Maintenance
- Updates: Datasets are static snapshots; not continuously updated.  
- Responsibility: Original dataset creators (Kaggle contributors).  
- Contact: Refer to Kaggle dataset pages for maintainers. 

## Known Limitations and Biases
- Engagement metrics may be biased by platform algorithms (e.g., YouTube trending selection).  
- OTT dataset may not represent all regions or genres equally.  
- Labels (high vs low engagement) depend on arbitrary thresholds (median), which may not generalize.  
- Demographic fields may be incomplete or synthetic.  
- Temporal drift: engagement patterns change over time; models trained on old data may underperform.  

## Ethical Considerations
- Models should not be used to manipulate audiences unfairly or exploit addictive behaviors.  
- Regional differences must be respected; avoid homogenizing cultural engagement patterns.  
- Transparency: datasheet and model card included to highlight limitations and responsible use.  
- Human-in-the-loop recommended for scheduling decisions.  
