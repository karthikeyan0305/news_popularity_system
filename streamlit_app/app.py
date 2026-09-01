import streamlit as st

st.set_page_config(
    page_title="News Popularity Intelligence",
    page_icon="📰",
    layout="wide"
)

st.title("📰 News Popularity Intelligence System")

st.subheader("Transformer-Based Deep Learning")

st.write("""
This system estimates the potential popularity of a news article
using only its title and description.
""")

st.divider()


# Problem Overview


st.header("📌 Problem Overview")

st.write("""
Digital news platforms publish a large number of articles every day.
At the time of publication, actual popularity indicators such as
clicks, shares, impressions and engagement are not yet available.

Therefore, the system estimates the attention potential of an article
using its textual content.
""")


# Why Popularity Labels Are Unavailable


st.header("❓ Why Are Popularity Labels Unavailable?")

st.write("""
Real-world popularity depends on future user behaviour.

For a newly published article, the following information may not
yet exist:

• Clicks
• Shares
• Impressions
• Likes
• Reading time
• User engagement
""")

st.info(
    "Therefore, popularity is treated as a latent variable and "
    "proxy signals are used to estimate attention potential."
)


# Architecture


st.header("🏗️ High-Level System Architecture")

st.code("""
News Title + Description
          ↓
     Text Cleaning
          ↓
 Transformer Tokenizer
          ↓
     DistilBERT
          ↓
  Contextual Embedding
          ↓
   Proxy Popularity Signals
          ↓
   Popularity Scoring
          ↓
    Article Ranking
          ↓
      Streamlit UI
""")

st.divider()

st.success(
    "Use the sidebar to open News Intelligence or Model Reasoning."
)