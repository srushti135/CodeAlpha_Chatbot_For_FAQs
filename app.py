import streamlit as st
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- 1. SET UP NLP TOOLS ---
@st.cache_resource
def setup_nlp():
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('punkt_tab')
    return WordNetLemmatizer()

lemmatizer = setup_nlp()

def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())
    return " ".join([lemmatizer.lemmatize(word) for word in tokens])

# --- 2. THE FAQ DATA ---
faq_data = {
    "What are your working hours?": "Our working hours are Monday to Friday, 9 AM to 6 PM.",
    "How can I reset my password?": "You can reset your password by clicking on the 'Forgot Password' link on the login page.",
    "Do you offer refunds?": "Yes, we offer a 30-day money-back guarantee for all our products.",
    "How do I contact support?": "You can contact support via email at support@codealpha.tech.",
    "Where are you located?": "Our headquarters are based in tech-park, but we operate globally."
}

raw_questions = list(faq_data.keys())
answers = list(faq_data.values())
processed_questions = [preprocess_text(q) for q in raw_questions]

# Vectorize the training data
vectorizer = TfidfVectorizer(stop_words='english')
question_vectors = vectorizer.fit_transform(processed_questions)

# --- 3. BOT LOGIC ---
def get_bot_response(user_input):
    processed_input = preprocess_text(user_input)
    user_vector = vectorizer.transform([processed_input])
    
    similarities = cosine_similarity(user_vector, question_vectors)
    best_match_index = np.argmax(similarities)
    highest_similarity = similarities[0, best_match_index]
    
    if highest_similarity > 0.25:
        return answers[best_match_index]
    else:
        return "I'm sorry, I couldn't find an answer to that. Try asking about our hours, refunds, or support contact details."

# --- 4. STREAMLIT FRONTEND UI ---
st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖")

st.title("🤖 CodeAlpha FAQ Assistant")
st.write("Ask any questions regarding our operational hours, support channels, or refund policies.")

# Maintain chat messages state across web reruns
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I am your AI assistant. How can I help you today?"}]

# Render previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Capture user input from the chat bar
if prompt := st.chat_input("Type your question here..."):
    # Append and show User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
        
    # Generate, append, and show Bot response
    response = get_bot_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)