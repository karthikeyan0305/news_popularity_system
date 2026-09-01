def rank_articles(df):
    return df.sort_values(by="popularity_score", ascending=False)