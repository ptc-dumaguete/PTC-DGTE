import streamlit as st
import time
# PTC-Dumaguete Rule-Based Chatbot
# Created for TESDA trainees and staff

print("🤖 Welcome to PTC-Dumaguete Chatbot!")
print("Type 'exit' to end the conversation.\n")

# Dictionary of responses
responses = {
    "hello": "Hello! Welcome to PTC-Dumaguete, your gateway to technical-vocational excellence. How can I assist you today?",
    "driving nc ii": "Driving NC II prepares you for professional driving. Requirements include a valid license, medical clearance, and enrollment forms. Ask us about the next schedule!",
    "carpentry nc ii": "Carpentry NC II equips you with woodworking and construction skills. Ideal for building and renovation careers.",
    "tile setting nc ii": "Tile Setting NC II trains you to install floor and wall tiles with precision. Great for finishing work.",
    "masonry nc ii": "Masonry NC II covers bricklaying, concrete work, and finishing techniques. Perfect for aspiring builders.",
    "enrollment": "Enrollment is ongoing! Visit PTC-Dumaguete or contact our registrar for assistance. We’ll guide you step by step.",
    "requirements": "Basic requirements include a valid ID, medical certificate, and application form. Some programs may require additional documents.",
    "schedule": "Training schedules vary by program. Check our bulletin board, Facebook page, or ask the registrar for updates.",
    "certificate": "Certificates of Completion and Enrollment are issued upon fulfilling attendance and assessment requirements. Contact the registrar for details.",
    "location": "We’re located at Rovira Drive, Dumaguete City, Negros Oriental. Look for the TESDA signage near the highway!",
    "contact": "Reach us via our official Facebook page or visit the center during office hours. We’re happy to assist!",
    "thank you": "You're most welcome! PTC-Dumaguete is proud to serve and empower every Filipino learner.",
    "bye": "Goodbye for now! Keep learning, keep growing. We hope to see you at PTC-Dumaguete soon.",
}

# Chat loop
while True:
    user_input = input("You: ").lower()
    if user_input == "exit":
        print("Bot: Salamat! Ingat ka. 👋")
        break
    elif user_input in responses:
        print("Bot:", responses[user_input])
    else:
        print("Bot: I'm sorry, I don't have information on that yet. Try asking about TESDA programs or enrollment.")
