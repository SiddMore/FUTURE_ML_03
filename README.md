# 🤖 AI Customer Support Chatbot

A smart, NLP-based chatbot built with **Python** and **Streamlit**. This bot uses **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity** to understand customer queries and provide accurate responses from a predefined dataset.

## 🚀 Features
* **Intent Recognition:** Uses NLTK and Scikit-learn to classify user intent.
* **Smart Fallback:** Detects low-confidence queries and asks for clarification.
* **Interactive UI:** Built with Streamlit for a clean, chat-like interface.
* **Easy Customization:** All questions and answers are stored in a simple JSON file.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Frontend:** Streamlit
* **NLP/ML:** NLTK, Scikit-learn (TF-IDF Vectorizer, Cosine Similarity)

## 📂 Project Structure

├── app.py # Main application code 
├── intents.json # Dataset containing patterns and responses 
├── requirements.txt # List of dependencies 
└── README.md # Project documentation

## ⚙️ Installation & Usage

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/your-username/support-bot.git](https://github.com/your-username/support-bot.git)
    cd support-bot
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application**
    ```bash
    streamlit run app.py
    # OR if you have path issues:
    python -m streamlit run app.py
    ```

## 🧠 How It Works
1.  **Preprocessing:** The bot loads `intents.json` and tokenizes the patterns.
2.  **Vectorization:** It converts text into numerical vectors using `TfidfVectorizer`.
3.  **Matching:** When a user asks a question, the system calculates the **Cosine Similarity** between the user's input and the known patterns.
4.  **Response:** If the similarity score is above a threshold, it returns the appropriate response; otherwise, it triggers a fallback message.

## 🌐 Live Deployment
This project is fully deployed using **Streamlit Cloud**.
👉 **[Click here to chat with the bot](https://customersupportbot01.streamlit.app/)**

## 🔮 Future Scope
* Integrate OpenAI API for generative responses.
* Add a database to store user chat history.
* Deploy on a live server (Streamlit Cloud/Heroku).

