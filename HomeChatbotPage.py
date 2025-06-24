import streamlit as st
import openai
import os

# Set OpenAI API key (for local dev: set an env variable; on cloud, use Streamlit secrets)
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="🤖 AI Credit Chatbot")
st.title("🤖 AI Chatbot for Farmer Credit Scoring")

st.markdown("Ask questions like:")
st.markdown("- *Will a 40-year-old farmer in rural area with secondary education get a loan?*")
st.markdown("- *What is the credit score of a woman with access to phone and tertiary education?*")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi there! I'm your credit scoring assistant. Ask me about any farmer profile and I'll predict their loan eligibility."}
    ]

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
prompt = st.chat_input("Type your question here...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call to OpenAI or local model
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=st.session_state.messages
                )
                reply = response["choices"][0]["message"]["content"]
            except Exception as e:
                reply = f"Something went wrong: {str(e)}"

            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})


st.markdown("---")
st.markdown("<div style='text-align: center;'>📌 Made with ❤️ by <strong>Team Numerixa</strong></div>", unsafe_allow_html=True)
