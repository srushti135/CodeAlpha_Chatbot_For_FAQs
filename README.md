# 🤖 CodeAlpha AI Internship – FAQ Chatbot using NLP

## 📌 Project Description

This project is an intelligent FAQ Chatbot developed as part of the CodeAlpha Artificial Intelligence Internship Program. The chatbot uses Natural Language Processing (NLP) and Machine Learning techniques to understand user queries and provide the most relevant response from a predefined knowledge base.

Unlike traditional keyword-based chatbots, this system applies text preprocessing, TF-IDF vectorization, and cosine similarity algorithms to identify the semantic meaning of user questions, allowing it to handle different phrasings and minor spelling variations effectively.

The application features a modern and interactive web interface built with Streamlit, providing a smooth conversational experience similar to commercial AI assistants.

---

## 🚀 Features

### ✅ Intelligent Question Matching

* Matches user queries with stored FAQs using NLP techniques.
* Handles alternative wording and sentence structures.
* Provides accurate responses based on semantic similarity.

### ✅ NLP Preprocessing

* Text Cleaning
* Tokenization
* Stopword Removal
* Lemmatization using NLTK

### ✅ Machine Learning-Based Retrieval

* TF-IDF Vectorization
* Cosine Similarity Scoring
* Confidence-Based Response Selection

### ✅ Interactive Chat Interface

* Real-time chatbot conversation
* Chat history support
* User-friendly Streamlit interface

### ✅ Error Handling

* Unknown query detection
* Fallback responses for unmatched questions
* Input validation

---

## 🛠️ Technology Stack

| Technology   | Purpose                     |
| ------------ | --------------------------- |
| Python       | Core Programming Language   |
| NLTK         | Natural Language Processing |
| Scikit-learn | TF-IDF & Cosine Similarity  |
| NumPy        | Mathematical Computation    |
| Streamlit    | Web Application Framework   |

---

## 📂 Project Structure

```text
CodeAlpha_Chatbot_For_FAQs/
│
├── app.py
├── chatbot.py
├── faq_data.json
├── requirements.txt
├── README.md
│
├── assets/
│   └── chatbot_demo.png
│
└── utils/
    └── preprocessing.py
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_Chatbot_For_FAQs.git
cd CodeAlpha_Chatbot_For_FAQs
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

Or

```bash
pip install streamlit nltk scikit-learn numpy pandas
```

### 5. Download NLTK Resources

```python
import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
```

### 6. Run Application

```bash
streamlit run app.py
```

Application will start at:

```text
http://localhost:8501
```

---

## 🔄 Working Principle

### Step 1: User Input

The user enters a question through the chatbot interface.

### Step 2: Text Preprocessing

The query undergoes:

* Lowercasing
* Tokenization
* Stopword Removal
* Lemmatization

### Step 3: Feature Extraction

TF-IDF transforms text into numerical vectors.

### Step 4: Similarity Calculation

Cosine Similarity measures how closely the query matches existing FAQs.

### Step 5: Response Generation

The answer with the highest similarity score is returned to the user.

### Step 6: Fallback Mechanism

If confidence is below the threshold, the chatbot asks the user to rephrase the question.

---

## 📊 AI Concepts Implemented

* Natural Language Processing (NLP)
* Information Retrieval
* Text Vectorization
* TF-IDF
* Cosine Similarity
* Text Normalization
* Machine Learning-Based Matching

---

## 📸 Screenshots

<img width="808" height="640" alt="image" src="https://github.com/user-attachments/assets/eca32dde-0062-4cbd-a94b-073bdef4a439" />



## 🎯 Internship Task Requirements Covered

✔ FAQ Collection and Knowledge Base Creation

✔ Text Preprocessing using NLP

✔ Cosine Similarity Matching

✔ Best Answer Retrieval

✔ Interactive Chatbot Interface

✔ Machine Learning Integration

---

## 🔮 Future Enhancements

* Voice-Based Interaction
* Multilingual Support
* Database Integration
* Generative AI Responses
* OpenAI/Gemini API Integration
* User Authentication
* Chat Analytics Dashboard

---

## 👩‍💻 Author

Srushti Kale

B.Tech Computer Science Engineering

Artificial Intelligence Intern – CodeAlpha

GitHub: https://github.com/srushti135

LinkedIn: https://www.linkedin.com/in/srushti-kale-b8101a28a/

---

## 📄 License

This project was developed for educational and internship purposes under the CodeAlpha Artificial Intelligence Internship Program.
