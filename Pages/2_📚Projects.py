import streamlit as st
from PIL import Image

st.title("Projects")

image1=Image.open("pro 3.GIF")
img2=Image.open("pro2.JPG")
img3=Image.open("pro1.JPG")


st.write("##")
col5,col6=st.columns((1,2))
with col5:
    st.subheader("Plant Disease Identification")
    st.write("#")
    st.image(image1)
    st.write("---")
    st.write("###")
with col6:
    st.subheader("The development of plant disease detection, to recognize the disease and suggesting a remedy to it")
    st.write("""
            The project entitled “Plant Disease Identification” is crucial for ensuring plant quality and food security.
            Recent advances in computer vision and machine learning techniques have made it possible 
            to accurately detect, classify, and monitor plant diseases based on images of leaves.""")
    st.markdown("[Contact me...](dm.wa.link/e4r2ws)")
    #st.write("###")
    st.write("---")
    st.write("###")
with col5:
    st.subheader("Online Grocery Store")
    st.write("###")
    st.image(img2)
    st.write("##")
    st.write("---")
    st.write("####")
with col6:
    st.subheader("The development of an online grocery, to track offer and availability of an item in the market")
    st.write(""" 
            Shop Management System is a software application to be developed to manage most of the activities or tasks running in a grocery shop.
            This system divided in to three main categories: cashier/stock management, supplier information management/generating report, staff management00.
            This application will provide the basic features such as cashier to handle sales transaction, stock management to control.""")
    st.markdown("[Contact me...](dm.wa.link/e4r2ws)")
    #st.write("######")
    st.write("---")
    st.write("###")


with col5:
    st.subheader("Eye Bank Management")
    st.image(img3)
    st.write("#")
    st.write("---")

with col6:
    st.subheader("The development of Eye Bank system,to track camp and donor details")
    st.write("""  
            This application is built such a way that it should suits for all type of Eye Banks in future. 
            So every effort is taken to implement this project in this Eye Bank, on successful implementation in this Eye Bank, 
            we can target other Eye Banks in the city""")
    st.markdown("[Contact me...](dm.wa.link/e4r2ws)")
    st.write("######")
    st.write("---")

