import streamlit as st
from PIL import Image

st.title("Welcome to Silky's Beauty Spa")
st.image('nature.jpeg', use_column_width=True)
st.write("We offer a wide range of Beauty Services to help you look and feel your best")
st.button("Book an Appointment")
st.title("Our Services")
st.write("Here are the Beauty Services we offer:")
st.write("-Facial Treatements")
st.write("-Massages")
st.write("-Manicures and Pedicures")
st.write("-Waxing")
st.write("-Hair Styling")
import datetime

st.title("Book an Appopintment")
service = st.selectbox("Select a service", ["Facial Treatment", "Massages", "Manicures and Pedicures", "Waxing", "Hair Styling"])
date = st.date_input("Select a date", datetime.date.today())
time = st.time_input("Select a time", datetime.time(9, 0))
name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
phone = st.text_input("Enter your phone")

if st.button("submit"):
    st.write("Thank you for booking an appointment!")
    
    
st.title("Customer Review")
st.write("Here are some reviews from our Satisfied customers:")
st.write("- 'Amazing service and great staff. Highly recommended!'")
st.write("- 'The best spa experience I've had in a long time.'")
st.write("- ' I feel so relaxed and rejunvenated after my visit.'")

st.title("About Us")
st.write("We are a team of experienced beauty proffessionals who are passionate about helping you look and feel your best. Our mission is to provide a relaxing and rejuvenating spa experience that leaves you feeling refreshed and renewed.")

st.title("Frequently Asked Questions")
st.write("Here are some commonly asked questions about our beauty spa:")
st.write("-What are your hours of operation?")
st.write("-Do you offer gift cards?")
st.write("- How much do you offer services cost?")
st.write("- Where are you located?")
st.write("- What type of payment do you accept?")

st.title("Contact Us")
st.write("If you have any question or comments, please fill out the form below and we will get back to you as soon as possible.")
message = st.text_area("Enter your message")

if st.button("Enter"):
    st.write("Thank you for contacting us. We will get back to you soon!")
    







