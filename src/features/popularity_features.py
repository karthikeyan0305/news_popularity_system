from nltk.sentiment import SentimentIntensityAnalyzer
import textstat

sia = SentimentIntensityAnalyzer()

urgent_words = ["breaking","war","crisis","attack","death","alert"]

def emotion_score(text):
    score = sia.polarity_scores(text)
    return abs(score["compound"])

def lexical_diversity(text):
    words = text.split()
    return len(set(words)) / len(words) if len(words) > 0 else 0

def readability_score(text):
    return textstat.flesch_reading_ease(text)

def urgency_score(text):
    return sum(1 for word in urgent_words if word in text)
