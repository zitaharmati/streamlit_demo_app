import streamlit as st

st.title("Streamlit demo page")

st.header("This is my heading for my streamlit")
st.subheader("This is the subheading")

st.text("This is an example text just to try")

st.success("This is a success message")
st.warning("This is a warning")
st.info("This is an information")
st.error("This is error message")

if st.checkbox("Select/Unselect"):
    st.text("User selected checkbox")
else:
    st.text("Please select the checkbox")

state=st.radio("What is your favorite color?", ("Red", "Green", "Blue"))

if state=="Green":
    st.success("That is my favorite color as well!")

occupation=st.selectbox("What do you do?", ["Student", "Vlogger", "Data scientist", "Data engineer"])

st.text(f"Selected option is {occupation}")

if st.button("Example"):
    st.error("You clicked it!")


st.sidebar.header("Heading of sidebar")
st.sidebar.text("Created by Zita")

