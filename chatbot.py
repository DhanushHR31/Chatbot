import openai
import streamlit as st

# Set your OpenAI API key (use your actual key here)
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_response(prompt):
    """Generate a response from OpenAI's GPT model."""
    try:
        # Use the new API interface
        response = openai.completions.create(
            model="gpt-3.5-turbo",  # Ensure to use the correct model name
            prompt=prompt,
            max_tokens=150  # You can adjust max_tokens as needed
        )
        return response['choices'][0]['text'].strip()  # Adjusting response format for new API
    except Exception as e:
        return f"Error: {e}"

def main():
    st.title("Chatbot App")
    st.write("Ask me anything! I'm powered by OpenAI's GPT model.")

    # Initialize the session state to store the conversation
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Input box for user query
    user_input = st.text_input("Your message:", "", key="user_input")

    # Display chat history
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Bot:** {msg['content']}")

    # Process user input and generate response
    if user_input.strip():  # Only process if the input is not empty
        # Append user message
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Generate bot response
        bot_response = generate_response(user_input)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})

        # Display the bot response
        st.markdown(f"**Bot:** {bot_response}")

if __name__ == "__main__":
    main()
