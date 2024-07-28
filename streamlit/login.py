import streamlit as st
import json

# Display Home Page
def HomePage():
    st.title("Simple Login Page")
    st.header("Home")
    st.subheader("Wecome to Simple Login App. Please Login / Sign up")


def formPage(name = False):
    st.title("Simple Login Page")
    username = st.text_input("Enter your username")
    password = st.text_input("Enter your password", type="password")
    if name:
        confirmPassword = st.text_input("Confirm password", type="password")
        return username, password, confirmPassword
    return username, password


def LoginPage():
    username, password = formPage()
    if st.button("Login"):

        with open("user_list.json", "r") as file:
            users = json.load(file)
            if username in users.keys():
                if users[username] == password:
                    st.success("You are logged in successfully")
                else:
                    st.error("Invalid password")
            else:
                st.error("User not found")
    

def SignUpPage():
    username, password, confirm_password = formPage(True)
    
    dict_obj = {}
    if st.button("Sign Up"):
        if password == confirm_password:
            with open("user_list.json", "r") as file:
                try:
                    dict_obj = json.load(file)
                except:
                    dict_obj = {}
                
            usernames = dict_obj.keys()
            if username in usernames:
                st.info("User already registerd. Please log in.")
                return
            with open("user_list.json", "w") as jsonFile:
                dict_obj[username] = password
                json.dump(dict_obj, jsonFile)
            st.success(f"Account created for {username}")
        else:
            st.error("Passwords do not match")


# Display sidebar
res = st.sidebar.selectbox("Menu", ["Home", "Login", "Sign Up"])

if res == "Home":
    HomePage()
if res == "Login":
    LoginPage()
if res == "Sign Up":
    SignUpPage()