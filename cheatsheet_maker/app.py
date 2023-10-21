# Importing necessary libraries
import streamlit as st  # Streamlit library to build web apps quickly with Python
import openai  # OpenAI's API to communicate with the GPT-3 model
from dotenv import load_dotenv  # Library to load environment variables (e.g., API keys)
import os  # Operating system library to interact with the environment variables

# Load environment variables (e.g., OpenAI API key) from a .env file
load_dotenv()

# Setting up the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def format_with_gpt3(input_command):
    # Sends the input Linux command to GPT-3.5 model and requests it to format it into a cheatsheet item
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {
                "role": "user",
                "content": f"""Turn this Linux command :{input_command} into a cheatsheet item by adding a description of the command. The description should be a single sentence.
                Example: 
                <command> \n
                description of the command""",
            }
        ],
        temperature=0.4,  # Controls randomness of output. Lower value makes output more deterministic
    )
    # Extracts and returns the content of the model's response
    return response.choices[0].message.content


def main():
    # Setting the title of the web application
    st.title("Linux Command Cheatsheet Formatter")

    # Using a session state to manage the value of the input_command
    if "input_command" not in st.session_state:
        st.session_state.input_command = ""

    # Textbox to allow users to enter a Linux command
    user_input = st.text_input(
        "Enter your Linux command:", value=st.session_state.input_command
    )

    if (
        user_input and user_input != st.session_state.input_command
    ):  # This ensures that the code is run only when Enter is pressed
        st.session_state.input_command = (
            user_input  # Storing the value in session state
        )

        # If a command is entered, get its cheatsheet format from GPT-3 and display it
        with st.spinner(
            "Processing..."
        ):  # Display a loading spinner while the command is being processed
            formatted_text = format_with_gpt3(user_input)

            st.code(formatted_text, language="bash")
            st.write(
                "Click and drag to select the above content, then right-click and copy or use Ctrl+C!"
            )

            st.session_state.input_command = (
                ""  # Reset the input command in session state
            )


# If this script is being run directly (not imported), execute the main function
if __name__ == "__main__":
    main()
