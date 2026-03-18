import streamlit as st
from transformers import pipeline

# Load the model once and cache it to save memory
@st.cache_resource
def load_model():
    # RoBERTa trained on GoEmotions (28 categories)
    return pipeline("text-classification", 
                    model="SamLowe/roberta-base-go_emotions", 
                    top_k=None)

def analyze_mood_advanced(text): # ✅ To this
    clean_text = text.lower().strip()
    
    # --- LAYER 1: HEURISTIC OVERRIDE (Slang & Idioms) ---
    # This fixes the "Fire" and "Blast" issues directly
    positive_slang = ['fire', 'blast', 'goat', 'slay', 'lit', 'bet', 'clutch']
    if any(word in clean_text for word in positive_slang):
        return "Positive", "🔥", "Slang/Idiom Approval", 1.0

    # --- LAYER 2: TRANSFORMER ANALYSIS ---
    classifier = load_model()
    results = classifier(text)[0]
    
    # Get Top 3 emotions to check for "Weighted Sentiment"
    top_3 = sorted(results, key=lambda x: x['score'], reverse=True)[:3]
    top_emotion = top_3[0]['label']
    confidence = top_3[0]['score']

    # Define Emotion Maps
    pos_list = ['joy', 'excitement', 'admiration', 'love', 'gratitude', 'approval', 'optimism', 'pride', 'relief']
    neg_list = ['anger', 'annoyance', 'disappointment', 'fear', 'sadness', 'disgust', 'grief', 'remorse', 'nervousness']

    # --- LAYER 3: CONSENSUS LOGIC ---
    # If the top emotion is 'neutral' but the 2nd/3rd are strongly positive, we pivot.
    if top_emotion == 'neutral' and confidence < 0.6:
        for extra in top_3[1:]:
            if extra['label'] in pos_list and extra['score'] > 0.15:
                return "Positive", "✨", extra['label'].capitalize(), extra['score']

    # Final Classification
    if top_emotion in pos_list:
        return "Positive", "🌟", top_emotion.capitalize(), confidence
    elif top_emotion in neg_list:
        return "Negative", "📉", top_emotion.capitalize(), confidence
    else:
        return "Neutral", "⚖️", "Neutral", confidence