import pandas as pd
import numpy as np

def load_data_auto(path: str) -> pd.DataFrame:
    """
    Universal loader for OTT and YouTube datasets.
    Detects schema and applies appropriate preprocessing.
    """
    df = pd.read_csv(path)
    cols = df.columns.str.lower()
   

    # --- Case 1: YouTube Trending / General ---
    if "publishedat" in cols or "trending_date" in cols:
       
        if "region" not in df.columns:
            df["region"] = "Unknown"
        if "platform" not in df.columns:
            df["platform"] = "YouTube"

        # Timestamp
        if "publishedAt" in df.columns:
            df["publish_time"] = pd.to_datetime(df["publishedAt"], errors="coerce", utc=True)
        elif "trending_date" in df.columns:
            df["publish_time"] = pd.to_datetime(df["trending_date"], errors="coerce", utc=True)

        # Engagement proxy
        views_col = "view_count" if "view_count" in df.columns else "views"
        df["engagement_rate"] = (df["likes"] + df["comment_count"]) / np.maximum(df[views_col], 1)

        thresholds = df.groupby("region")["engagement_rate"].transform("median")
        df["label"] = (df["engagement_rate"] >= thresholds).astype(int)

        # Time features
        dt = df["publish_time"]
        df["hour"] = dt.dt.hour
        df["dayofweek"] = dt.dt.dayofweek
        df["month"] = dt.dt.month
        df["weekofyear"] = dt.dt.isocalendar().week.astype(int)
        df["is_weekend"] = df["dayofweek"].isin([5,6]).astype(int)

        # Content features
        df["title_len"] = df["title"].astype(str).apply(len)
        if "tags" in df.columns:
            df["tag_count"] = df["tags"].astype(str).apply(lambda x: 0 if x == "[none]" else len(x.split("|")))
        else:
            df["tag_count"] = 0

        keep_cols = [
            "video_id", "region", "platform", "hour", "dayofweek", "month",
            "weekofyear", "is_weekend", "title_len", "tag_count", "label"
        ]
        return df[keep_cols]

    # --- Case 2: OTT Content Scheduling ---
    elif "time of day" in cols or "release date" in cols:
        
        if "platform" not in df.columns:
            df["platform"] = "OTT"

        # Timestamp
        if "Release Date" in df.columns:
            df["publish_time"] = pd.to_datetime(df["Release Date"], errors="coerce", utc=True)

        # Engagement proxy
        if "Viewership" in df.columns:
            df["engagement_rate"] = (df.get("Likes", 0) + df.get("Comments", 0)) / np.maximum(df["Viewership"], 1)
        else:
            df["engagement_rate"] = np.nan

        thresholds = df["engagement_rate"].median()
        df["label"] = (df["engagement_rate"] >= thresholds).astype(int)

        # ✅ Convert '06:59 AM' → float hour
        if "Time of Day" in df.columns:
            time_parsed = pd.to_datetime(df["Time of Day"].astype(str), format="%I:%M %p", errors="coerce")
            df["hour"] = time_parsed.dt.hour + time_parsed.dt.minute / 60.0
            df["hour"] = pd.to_numeric(df["hour"], errors="coerce")

        # ✅ Convert day of week strings → integers
        if "Day of the Week" in df.columns:
            day_map = {
                "Monday": 0, "Tuesday": 1, "Wednesday": 2,
                "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6
            }
            df["dayofweek"] = df["Day of the Week"].map(day_map)
            df["dayofweek"] = pd.to_numeric(df["dayofweek"], errors="coerce")

        df["is_weekend"] = df["dayofweek"].isin([5,6]).astype(int) if "dayofweek" in df else 0

        if "Title" in df.columns:
            df["title_len"] = df["Title"].astype(str).apply(len)
        else:
            df["title_len"] = 0

        df["tag_count"] = 0

        keep_cols = ["platform", "hour", "dayofweek", "is_weekend", "title_len", "tag_count", "label"]
        if "region" in df.columns:
            keep_cols.insert(0, "region")

        # ✅ Drop rows where conversion failed
        df = df.dropna(subset=["hour", "dayofweek"])

        # ✅ Force numeric dtypes before returning
        df["hour"] = df["hour"].astype(float)
        df["dayofweek"] = df["dayofweek"].astype(int)
        df["title_len"] = df["title_len"].astype(int)
        df["tag_count"] = df["tag_count"].astype(int)

        return df[keep_cols]

    else:
        raise ValueError(f"Unrecognized dataset schema: {df.columns}")