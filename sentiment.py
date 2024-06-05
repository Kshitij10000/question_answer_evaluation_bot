from transformers import pipeline

# Initialize the sentiment analysis pipeline with the specified model
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_response(transcription):
    analysis = sentiment_analyzer(transcription)
    return analysis

