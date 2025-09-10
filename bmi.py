import google.generativeai as genai
import streamlit as st 
st.title("This is my first st application")
st.header("App is about BMI calculator")
st.subheader("we need basic information from you")
st.markdown("##Initial Assessment : A healthy BMI")

genai.configure(api_key="AIzaSyCAO4WGnVP74LAzadc2kWdCA3JI3itq8Yo")

model = genai.GenerativeModel(model_name="gemini-2.5-flash-lite")

if st.button("Press Now"):
    st.write("hello Pratik !")
    
if st.checkbox("show text"):
    st.write("text is visible")

name = st.text_input("type your Name:")
st.write(f"your name : {name}")

number = st.number_input("type your age?:")
st.write(f"your age : {number}")


wt = st.number_input("type your wt?:")
st.write(f"your age : {wt}")

ht = st.slider("type your ht in cm:",50,250)
st.write(f"your age : {ht}")

bmi = wt/(ht/100)**2
st.write(f"your bmi is  : {bmi}")


prompt1 = st.text_area(f"Enter prompt (you can edit this):", 
                       f"A person with height {ht} cm and weight {wt} kg has a BMI of {bmi:.2f}. Is this healthy? What is the safe BMI range?")

if st.button("Get AI Feedback"):
    response = model.generate_content(prompt1)
    st.write(response.text)
