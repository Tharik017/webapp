import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import multipage_streamlit as mt
from pages import *
import requests
import os


app=mt.Multipage()
app.add("Project", project.run)
app.add("Contact", contact.run)


st.set_page_config(
    page_title="Multipage App",
    page_icon=":wave:"
    )

st.title("Main Page")
st.sidebar.success("Pages Loaded")


def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding=load_lottieurl("https://lottie.host/28785e1d-98c4-4616-8b78-e0da2c9afe6c/m79m8uNtFp.json")

st.write("##")
st.subheader("Hey Everyone!:wave:")
st.subheader("I am Mohamed Tharik")
st.write(" I am  passionate about finding ways to use python to effective in modern world")
st.write("[Know more>>](dm.wa.link/e4r2ws)")
st.write("###")
st.subheader("Resume")
#file_path = "New/web/Mohamed Tharik.PDF"  # Replace with your actual file path
#if os.path.exists(file_path):
 #   print("File exists.")
#else:
 #   print("File does not exist.")
#print(f"Current working directory: {os.getcwd()}")
#base_dir = os.path.dirname(__file__)  # Get the directory of the script
#file_path = os.path.join(base_dir, "New/web/Mohamed Tharik.PDF")  # Construct the file path

                
file_path = "Mohamed Tharik.PDF"
certificate1="google certificate.PDF"
certificate2="meta certificate.PDF"
with open(file_path, "rb") as file:
    st.download_button(
    label="Download File",
    data=file,
    file_name="Mohamed Tharik.PDF",
    mime="text/plain"  # Adjust MIME type based on your file
    )
#except FileNotFoundError:
 #   print(f"File not found: {file_path}")
#except IOError as e:
    #print(f"IOError occurred: {e}")

st.header("About Me:")
with st.container():
        col1,col2=st.columns(2)
with col1:
            st.write("##")
            st.subheader("Profile Summary")
            st.write(""" 
             Dynamic knowledge in Python and Basics in Django, Streamlit and RDBMS. Fresh 
             Graduate with an aptitude for aptitude and passion for Continuous Learning.
             Eager to contribute to collaborative and impactful Software development projects and drive innovation in field""")
            st.write("###")

with col2:
            st_lottie(lottie_coding, height=300)


st.header("Education:")
col3,col4=st.columns(2)
with col3:
    st.header("Education-College")
    
    st.subheader("Post Graduate")
    st.write("M.Sc - Computer Science")
    st.write ("2022 - 2024")
    st.write("GTN arts and science college") 
    st.write("CGPA – 7")

    st.subheader("Under Graduate")
    st.write("B.Sc - Computer Science") 
    st.write("2019 - 2022")
    st.write("Parvathis arts and science college") 
    st.write("CGPA – 6.7")
with col4:
    st.header("Education-School")
    st.subheader("Higher Secondary")
    st.write("CSMA Higher Secondary School(2019)")
    st.write("Percentage = 47%")

    st.subheader("SSLC")
    st.write("TPKN Matric Higher Secondary School(2017)")
    st.write("Percentage = 97%")

st.header("Certifications:")
col5,col6=st.columns(2)
with col5:
       st.write("1.Crash Course on Python provided by Google on Coursera")
       st.write("###")
with col6:
    with open(certificate1, "rb") as file:
        st.download_button(
        label="Download File",
        data=file,
        file_name="google certificate.PDF",
        mime="text/plain"  # Adjust MIME type based on your file
        )

col7,col8=st.columns(2)
with col7:
      st.write("2.Programming In Python provided by Meta on Coursera")
      st.write("###")
with col8:
    with open(certificate2, "rb") as file:
        st.download_button(
        label="Download File",
        data=file,
        file_name="meta certificate.PDF",
        mime="text/plain"  # Adjust MIME type based on your file
        )

