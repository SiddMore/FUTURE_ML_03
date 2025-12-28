import streamlit as st
import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

# 1. Load the Intents Data
def load_intents(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

# 2. Train the Model (Simple NLP)
def train_model(intents):
    corpus = []
    tags = []
    for intent in intents:
        for pattern in intent['patterns']:
            corpus.append(pattern)
            tags.append(intent['tag'])
    
    # Vectorize the text (Convert words to numbers)
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(corpus)
    
    return vectorizer, X, tags, corpus

# 3. Chat Logic
def chatbot_response(user_input, vectorizer, X, tags, intents_data):
    # Convert user input to vector
    user_vec = vectorizer.transform([user_input])
    
    # Calculate similarity with all known patterns
    similarities = cosine_similarity(user_vec, X)
    
    # Find the best match
    best_match_index = similarities.argmax()
    confidence = similarities[0][best_match_index]
    
    # Threshold for "Smart Fallback" (If confidence is too low, bot doesn't understand)
    if confidence < 0.2: 
        return "I'm sorry, I didn't quite understand that. Could you rephrase your question? You can also ask to speak to a human."
    
    # Get the tag of the best match
    predicted_tag = tags[best_match_index]
    
    # Return a random response from that tag
    for intent in intents_data:
        if intent['tag'] == predicted_tag:
            return random.choice(intent['responses'])

# --- STREAMLIT UI SETUP ---
st.set_page_config(page_title="Customer Support Bot", page_icon="🤖")

# Initialize Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add an initial greeting from the bot
    st.session_state.messages.append({"role": "assistant", "content": "Hi! I'm your automated support assistant. How can I help you today?"})

# Load Data & Train
intents_data = load_intents('intents.json')
vectorizer, X, tags, corpus = train_model(intents_data)

# Sidebar
st.sidebar.title("🤖 Support Hub")
st.sidebar.markdown("""
**About this Task:**
This bot uses NLP (TF-IDF) to match your questions to predefined intents.
- Try asking: *"Where is my order?"*
- Try asking: *"I want a refund"*
""")
st.sidebar.info("") 

# Main Chat Interface
st.title("Customer Support Chatbot")
st.markdown("ask me about orders, returns, or payments!")

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Handler
if prompt := st.chat_input("Type your question here..."):
    # 1. Display User Message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Get Bot Response
    response = chatbot_response(prompt, vectorizer, X, tags, intents_data)

    # 3. Display Bot Message
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})