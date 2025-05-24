import streamlit as st

st.title("This is a simple Streamlit Calculator")

name = st.text_input("Enter your name: ")
st.subheader(f"Hello! {name} welcome to this calculator.")

a = st.number_input("Enter your 1st number: ")
b = st.number_input("Enter your 2nd number: ")

st.write("Operation")
 
operation = st.radio("Select an operation to perform:",
                    ("Add", "Subtract", "Multiply", "Divide"))

output = 0

def calculator():
    if operation == "Add":
        output = a+b
    elif operation == "Subtract":
        output = a-b
    elif operation == "Multiply":
        output = a*b
    elif operation == "Divide" and b != 0:
        output = a/b
    else:
        st.warning("Division by zero. Please enter a non zero number in denomenator.")
        output = "Not Defined"
    st.success(f"Your calculation ans is: {output}")

if st.button("Calculate Result"):
    calculator()
        



