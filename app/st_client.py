import streamlit as st
import base64
from chain import run_llm
import os
from dotenv import load_dotenv

load_dotenv()

# Set up your API key for OpenAI
openai_api_key = os.environ.get("OPENAI_KEY")
if openai_api_key == None:
    with st.sidebar:
        openai_api_key = st.text_input(
            "OpenAI API Key", key="langchain_search_api_key_openai", type="password"
        )
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
with st.sidebar:
    st.markdown("---")
    st.markdown(
        '<h6>Made in &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="16">&nbsp by <a href="https://www.linkedin.com/in/iamdgarcia">@iamdgarcia</a></h6>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div style="margin-top: 0.75em;"><h6>Follow on &nbsp<a href="https://medium.com/@iamdgarcia" target="_blank"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/medium.svg" alt="Medium profile" height="41" width="174"></a></h6></div>',
        unsafe_allow_html=True,
    )

# copies 
home_title = "Ticket Reader"
home_introduction = "Welcome to Ticket Reader, where the power of AI technology is here to assist you in reading and analyzing your supermarket receipts. Whether you need quick data extraction from a ticket or an organized list of your purchases, Ticket Reader has you covered. Get started and explore how AI can make managing your receipts easier and more efficient!"
home_privacy = "At Ticket Reader, your privacy is our top priority. To protect your personal information, our system only uses the hashed value of your API Key, ensuring complete privacy and anonymity. Your API key is only used to access AI functionality during your session and is not stored afterward. You can use Ticket Reader with peace of mind, knowing that your data is always safe and secure."


st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5>Beta</font></span>""",unsafe_allow_html=True)
st.markdown("""\n""")
st.markdown("#### Greetings")
st.write(home_introduction)


st.markdown("#### Privacy")
st.write(home_privacy)


# File uploader for PDF
uploaded_file = st.file_uploader("Upload a ticket", type=["png"])

if uploaded_file is not None:
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    else:
        # Read the uploaded file
        file_data = uploaded_file.read()

        # Encode the file data to base64
        encoded_data = base64.b64encode(file_data).decode("utf-8")
        # Send the encoded data to the endpoint
        with st.spinner("Analizing file. Please wait..."):
            response = run_llm(openai_api_key,encoded_data)
        
        # Display the response
        st.subheader("Result:")
        st.image(uploaded_file,caption="Uploaded ticket")
        st.json(response)
