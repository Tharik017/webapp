import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests


def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



lottie_code=load_lottieurl("https://lottie.host/39c705ef-04a4-4d2a-ad08-7e9221028e72/NZ43eclJnH.json")
st.title("Contact")
st.write("---")
st.header("Get In Touch With Me!")
st.write("##")

# HTML form from FormSubmit
contact_form = """
        <form action="https://formsubmit.co/mhmdtharik017@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 8px; margin: 4px 0; border: 1px solid #ccc; border-radius: 4px;">
        <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 8px; margin: 4px 0; border: 1px solid #ccc; border-radius: 4px;">
        <textarea name="message" placeholder="Your message here" required style="width: 100%; padding: 8px; margin: 4px 0; border: 1px solid #ccc; border-radius: 4px;"></textarea>
        <button type="submit" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Send</button>
    </form>
"""

# Create columns layout
left_column, right_column = st.columns(2)

# Display form in the left column
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:

    st_lottie(lottie_code, height=300)