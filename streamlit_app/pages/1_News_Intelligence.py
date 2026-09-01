import sys
import os

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


import streamlit as st
import pandas as pd

from src.features.popularity_features import (
    emotion_score,
    lexical_diversity,
    readability_score,
    urgency_score
)

from src.scoring.popularity_score import calculate_popularity



# Page Configuration


st.set_page_config(
    page_title="News Intelligence",
    page_icon="📰",
    layout="wide"
)

st.title("📰 News Intelligence")

st.write(
    "Select a news article and analyze its popularity potential."
)



# Load Dataset


DATA_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "News_dataset.csv"
)

df = pd.read_csv(DATA_PATH)

df["Title"] = df["Title"].fillna("").astype(str)
df["Description"] = df["Description"].fillna("").astype(str)



# Article Selection


st.subheader("Select News Article")

selected_index = st.selectbox(
    "Choose an article",
    df.index,
    format_func=lambda x: df.loc[x, "Title"]
)


title = df.loc[selected_index, "Title"]
description = df.loc[selected_index, "Description"]



# Display Input


st.text_input(
    "News Title",
    value=title,
    disabled=True
)

st.text_area(
    "News Description",
    value=description,
    height=160,
    disabled=True
)



# Analyze


if st.button("🔍 Analyze Popularity"):

    text = title + " " + description

    emotion = emotion_score(text)
    lexical = lexical_diversity(text)
    readability = readability_score(text)
    urgency = urgency_score(text)

    score = calculate_popularity(
        emotion,
        urgency,
        lexical,
        readability
    )

    # Normalize for UI
    score = max(0, min(score * 100, 100))



    # Popularity Score


    st.divider()

    st.subheader("📊 Popularity Score")

    st.metric(
        label="Predicted Attention Potential",
        value=f"{score:.2f} / 100"
    )



    # Key Signals


    st.subheader("🔍 Key Explanatory Highlights")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Emotion",
            f"{emotion:.2f}"
        )

    with col2:
        st.metric(
            "Urgency",
            f"{urgency}"
        )

    with col3:
        st.metric(
            "Lexical Diversity",
            f"{lexical:.2f}"
        )

    with col4:
        st.metric(
            "Readability",
            f"{readability:.2f}"
        )


    # --------------------------------------------------
    # Explanation
    # --------------------------------------------------

    st.subheader("💡 Why This Score?")

    reasons = []

    if urgency > 0:
        reasons.append(
            "⚡ Urgency-related language was detected."
        )

    if emotion >= 0.5:
        reasons.append(
            "🔥 The article contains relatively strong emotional intensity."
        )

    if lexical >= 0.5:
        reasons.append(
            "📚 The article shows relatively high lexical diversity."
        )

    if readability >= 60:
        reasons.append(
            "📖 The article has relatively good readability."
        )

    if not reasons:
        reasons.append(
            "The article shows comparatively weaker attention-oriented signals."
        )

    for reason in reasons:
        st.write(reason)