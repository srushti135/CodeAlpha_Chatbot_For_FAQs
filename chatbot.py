import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download the necessary NLTK tokenizer models
nltk.download('punkt')
nltk.download('punkt_tab')

# 1. Collect FAQs (Feel free to edit these questions and answers!)
faq_data = {
    "What are your working hours?": "Our working hours are Monday to Friday, 9 AM to 6 PM.",
    "How can I reset my password?": "You can reset your password by clicking on the 'Forgot Password' link on the login page.",
    "Do you offer refunds?": "Yes, we offer a 30-day money-back guarantee for all our products.",
    "How do I contact support?": "You can contact support via email at support@example.com.",
    "Where are you located?": "Our headquarters are based in tech-park, but we operate globally."
}

questions = list(faq_data.keys())
answers = list(faq_data.values())

# 2. Preprocess and Vectorize
vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize, stop_words='english')
question_vectors = vectorizer.fit_transform(questions)

def get_bot_response(user_input):
    user_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vector, question_vectors)
    best_match_index = np.argmax(similarities)
    highest_similarity = similarities[0, best_match_index]
    
    if highest_similarity > 0.2:
        return answers[best_match_index]
    else:
        return "I'm sorry, I don't quite understand. Could you rephrase your question?"

# 3. Chatbot loop
print("🤖 FAQ Chatbot is live! Ask me a question. (Type 'quit' to exit)")
print("-" * 60)

while True:
    user_text = input("You: ")
    if user_text.lower() in ['quit', 'exit']:
        print("Bot: Goodbye!")
        break
        
    response = get_bot_response(user_text)
    print(f"Bot: {response}\n")