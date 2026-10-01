# Task 2 - Chatbot for FAQs
# CodeAlpha Artificial Intelligence Internship

import nltk
import math
import re

from nltk.tokenize import wordpunct_tokenize


# -----------------------------
# FAQ Dataset
# -----------------------------
faqs = [
    {
        "question": "What is Python?",
        "answer": "Python is a high-level, interpreted programming language used for web development, AI, data science and automation."
    },
    {
        "question": "What is Artificial Intelligence?",
        "answer": "Artificial Intelligence is a technology that enables computers to perform tasks that normally require human intelligence."
    },
    {
        "question": "What is Machine Learning?",
        "answer": "Machine Learning is a branch of AI that allows computers to learn patterns from data and make predictions."
    },
    {
        "question": "What is Java?",
        "answer": "Java is a popular object-oriented programming language used for application, web and enterprise development."
    },
    {
        "question": "What is HTML?",
        "answer": "HTML stands for HyperText Markup Language and is used to create the structure of web pages."
    },
    {
        "question": "What is CSS?",
        "answer": "CSS stands for Cascading Style Sheets and is used to design and style web pages."
    },
    {
        "question": "What is an internship?",
        "answer": "An internship is a practical learning experience where students gain industry-related skills and knowledge."
    },
    {
        "question": "How can I learn programming?",
        "answer": "You can learn programming by studying basic concepts, practicing coding problems and building small projects."
    }
]


# -----------------------------
# Stop Words
# -----------------------------
stop_words = {
    "is", "the", "a", "an", "what", "are", "of",
    "to", "and", "in", "for", "how", "can", "i",
    "on", "with", "it", "this", "that"
}


# -----------------------------
# Text Preprocessing
# -----------------------------
def preprocess(text):
    text = text.lower()
    tokens = wordpunct_tokenize(text)

    # Keep only words
    tokens = [
        word for word in tokens
        if re.match(r"^[a-zA-Z]+$", word)
    ]

    # Remove stop words
    tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    return tokens


# -----------------------------
# Cosine Similarity
# -----------------------------
def cosine_similarity(text1, text2):

    words1 = preprocess(text1)
    words2 = preprocess(text2)

    vocabulary = set(words1 + words2)

    if not vocabulary:
        return 0

    vector1 = []
    vector2 = []

    for word in vocabulary:
        vector1.append(words1.count(word))
        vector2.append(words2.count(word))

    dot_product = sum(
        vector1[i] * vector2[i]
        for i in range(len(vocabulary))
    )

    magnitude1 = math.sqrt(
        sum(value * value for value in vector1)
    )

    magnitude2 = math.sqrt(
        sum(value * value for value in vector2)
    )

    if magnitude1 == 0 or magnitude2 == 0:
        return 0

    return dot_product / (magnitude1 * magnitude2)


# -----------------------------
# Find Best FAQ
# -----------------------------
def find_best_answer(user_question):

    best_score = 0
    best_answer = None

    for faq in faqs:

        score = cosine_similarity(
            user_question,
            faq["question"]
        )

        if score > best_score:
            best_score = score
            best_answer = faq["answer"]

    # Minimum similarity threshold
    if best_score >= 0.20:
        return best_answer

    return "Sorry, I could not find a suitable answer. Please try asking another question."


# -----------------------------
# Chatbot
# -----------------------------
def chatbot():

    print("=" * 50)
    print("             FAQ CHATBOT")
    print("=" * 50)

    print("Ask me a question.")
    print("Type 'exit' to stop the chatbot.")

    while True:

        user_question = input("\nYou: ")

        if user_question.lower() in ["exit", "quit", "bye"]:
            print("Bot: Thank you! Goodbye.")
            break

        if not user_question.strip():
            print("Bot: Please enter a question.")
            continue

        answer = find_best_answer(user_question)

        print("Bot:", answer)


# -----------------------------
# Start Program
# -----------------------------
if __name__ == "__main__":
    chatbot()