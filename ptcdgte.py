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
    "bye": "Goodbye for now! Keep learning, keep growing. We hope to see you at PTC-Dumaguete soon.",}

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
# --------------------------
# Page config and session
# --------------------------
st.set_page_config(page_title="Simple Chatbot", page_icon="🤖", layout="wide")

if "messages" not in st.session_state:
    # messages is a list of tuples: (role, text)
    st.session_state.messages = [("Bot", "👋 Hi! Welcome to TESDA Chatbot. Type 'help' to see options.")]

# last_action will hold a quick-action command when a button is clicked
if "last_action" not in st.session_state:
    st.session_state.last_action = None

# --------------------------
# Sidebar info + reset
# --------------------------
with st.sidebar:
    st.title("ℹ️ About this Chatbot")
    st.write("This is a simple **rule-based chatbot** built with Streamlit. You can:")
    st.markdown("""
    - 👋 Greet the bot  
    - 📝 Create an account  
    - 📦 View courses  
    - 📞 Talk to a human agent  
    """)
    if st.button("🔄 Reset Chat"):
        st.session_state.messages = [("Bot", "👋 Hi! Welcome to TESDA Chatbot. Type 'help' to see options.")]
        st.session_state.last_action = None
        st.experimental_rerun()

# --------------------------
# Top title
# --------------------------
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🤖 Rule-Based Chatbot</h1>", unsafe_allow_html=True)
st.write("Interact with the chatbot by typing or using quick action buttons below.")

# --------------------------
# Quick action buttons (safe pattern)
# --------------------------
col1, col2, col3 = st.columns(3)
if col1.button("📝 Create Account"):
    st.session_state.last_action = "create account"
if col2.button("📦 Courses"):
    st.session_state.last_action = "courses"
if col3.button("📞 Talk to Agent"):
    st.session_state.last_action = "talk to agent"

# --------------------------
# Determine user_input:
# - priority: last_action (button) -> chat_input (if available) -> text_input fallback
# --------------------------
user_input = None

# If a button was clicked (last_action set), consume it exactly once
if st.session_state.last_action:
    user_input = st.session_state.last_action
    # clear it immediately so it won't repeat on next run
    st.session_state.last_action = None

# Try to use chat_input (Streamlit >= 1.25). If not available, fall back to text_input.
try:
    # chat_input returns a value only when user submits
    if user_input is None:
        chat_in = st.chat_input("Type your message here...")
        if chat_in:
            user_input = chat_in
except Exception:
    # fallback to text_input with a session_state key so we can clear it after processing
    if user_input is None:
        # use a session key so we can reset it safely
        if "typed_value" not in st.session_state:
            st.session_state.typed_value = ""
        typed = st.text_input("Type your message here:", value=st.session_state.typed_value, key="typed_value")
        # Only process if not empty and not same as last processed (to avoid reprocessing)
        if typed and (len(st.session_state.messages) == 0 or st.session_state.messages[-1] != ("You", typed)):
            user_input = typed

# --------------------------
# Process a single user_input (if any)
# --------------------------
if user_input:
    # Append user message
    st.session_state.messages.append(("You", user_input))

    # Simulate typing effect (non-blocking visual)
    with st.spinner("Bot is typing..."):
        time.sleep(0.9)

    # Get bot reply
    try:
        bot_reply = chatbot_response(user_input)
    except Exception as e:
        bot_reply = f"⚠️ An internal error occurred while generating a reply: {e}"

    st.session_state.messages.append(("Bot", bot_reply))

    # If using the text_input fallback, clear stored value after processing
    if "typed_value" in st.session_state:
        st.session_state.typed_value = ""

# --------------------------
# Display conversation safely
# --------------------------
for entry in st.session_state.messages:
    # defensive check to avoid unpacking errors
    if not (isinstance(entry, (list, tuple)) and len(entry) == 2):
        # skip malformed entries
        continue
    role, msg = entry
    if role == "You":
        st.markdown(
            f"<div style='background-color:#DCF8C6; padding:10px; border-radius:15px; margin:5px; text-align:right;'>"
            f"🧑 <b>{role}:</b> {msg}</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"<div style='background-color:#E6E6FA; padding:10px; border-radius:15px; margin:5px; text-align:left;'>"
            f"🤖 <b>{role}:</b> {msg}</div>",
            unsafe_allow_html=True,
        )
