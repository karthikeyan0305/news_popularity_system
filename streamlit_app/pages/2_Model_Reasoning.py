import streamlit as st

st.set_page_config(
    page_title="Model Reasoning",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Model Reasoning")

st.write(
    "Understand how the system generates and interprets "
    "the popularity score."
)


# --------------------------------------------------
# Scoring Logic
# --------------------------------------------------

st.header("1️⃣ Scoring Logic")

st.write("""
The system does not have direct popularity labels such as clicks,
shares or impressions.

Therefore, proxy popularity signals are used.
""")

st.code("""
Popularity Score =
    0.30 × Emotion
  + 0.30 × Urgency
  + 0.20 × Lexical Diversity
  + 0.20 × Readability
""")

st.info(
    "The final score represents estimated attention potential, "
    "not actual user popularity."
)


# --------------------------------------------------
# Transformer Representation
# --------------------------------------------------

st.header("2️⃣ Transformer Representation")

st.write("""
The textual content is processed using a pretrained DistilBERT
Transformer model.

The Transformer converts the article text into a contextual
semantic representation.

The representation captures information about the meaning and
context of the news text.
""")

st.code("""
Title + Description
        ↓
DistilBERT Tokenizer
        ↓
Transformer Encoder
        ↓
Contextual Embedding
        ↓
Popularity Intelligence
""")


# --------------------------------------------------
# Proxy Signals
# --------------------------------------------------

st.header("3️⃣ Proxy Signals")

signals = {
    "Emotion": "Measures emotional intensity in the article.",
    "Urgency": "Detects urgency-related keywords and expressions.",
    "Lexical Diversity": "Measures vocabulary richness.",
    "Readability": "Measures how easy the article is to read."
}

for name, explanation in signals.items():

    st.subheader(name)
    st.write(explanation)


# --------------------------------------------------
# Example Comparison
# --------------------------------------------------

st.header("4️⃣ Example Comparison")

col1, col2 = st.columns(2)

with col1:

    st.subheader("📰 Article A")

    st.write(
        "BREAKING: Major earthquake hits the city, "
        "emergency teams deployed."
    )

    st.metric(
        "Example Score",
        "High"
    )

    st.write("""
    • Strong urgency
    • Emotional intensity
    • Breaking-news language
    """)


with col2:

    st.subheader("📰 Article B")

    st.write(
        "Local community meeting scheduled for next week."
    )

    st.metric(
        "Example Score",
        "Lower"
    )

    st.write("""
    • Low urgency
    • Lower emotional intensity
    • Routine information
    """)


# --------------------------------------------------
# Model Behaviour
# --------------------------------------------------

st.header("5️⃣ Model Behaviour Interpretation")

st.write("""
A higher score does not mean that an article will definitely become
popular.

It means that, based on the selected proxy signals, the article
contains comparatively stronger characteristics associated with
potential reader attention.
""")

st.warning(
    "The system estimates popularity potential because the dataset "
    "does not contain real engagement labels."
)
