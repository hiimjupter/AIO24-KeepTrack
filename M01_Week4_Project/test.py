import streamlit as st

# Basic Information and Links
st.title("MY PROJECT")
st.header("Welcome to AI VIETNAM")
st.subheader("Explore the World of AI")
st.caption("AI VIETNAM - Your gateway to learning AI")

# Mathematical Representations
st.markdown("# Mathematical Expressions")
st.markdown("Below are some common mathematical expressions used in AI:")
st.latex(r"\sqrt{2x+2}")
st.markdown(r"$\sqrt{2x+2}$")

# Divider for visual separation
st.divider()

# Media: Images, Audio, and Video
st.header("Media Section")
st.image('data/dogs.jpeg', caption='Funny dogs.')
st.audio('data/audio.mp4')
st.video('data/video.mp4')
st.logo('data/logo.png')  # Display at top-left corner

# Divider for visual separation
st.divider()

# Interactive Components
st.header("Interactivity in Streamlit")
agree = st.checkbox("I agree")
if agree:
    st.write("Great! You agreed.")

st.radio("Choose your favorite color:", [
         'Yellow', 'Blue'], captions=['Yellow', 'Blue'])
color = st.select_slider("Select your favorite color:",
                         options=["red", "orange", "violet"])
st.write("Your favorite color is", color)

contact_type = st.selectbox(
    "Choose your preferred contact method:",
    ("Email", "Home phone", "Mobile phone")
)

# Text input with default values based on the selectbox choice
if contact_type == "Email":
    contact_info = st.text_input("Enter your email:", value="@gmail.com")
elif contact_type == "Home phone":
    contact_info = st.text_input(
        "Enter your home phone number:", value="028")
elif contact_type == "Mobile phone":
    contact_info = st.text_input(
        "Enter your mobile phone number:", value="+84")

st.write("You selected:", contact_type)
st.write("Contact information:", contact_info)

options = st.multiselect("Select your favorite colors:", [
                         "Green", "Yellow", "Red", "Blue"], default=["Yellow", "Red"])
st.write("You selected:", options)

# Divider for visual separation
st.divider()

# Coding and Output Display
st.header("Coding and Outputs")
st.code("""
import torch
data = torch.Tensor([1, 2, 3])
print(data)
""", language="python")

with st.echo():
    def get_email():
        return 'trunghieu.nguyen@gmail.com'
    user_name = "trunghieu.nguyen"
    email = get_email()
    st.write(user_name, email)

# Divider for visual separation
st.divider()

# Forms and Submissions
st.header("Form Submission")
with st.form("my_form"):
    col1, col2 = st.columns(2)
    f_name = col1.text_input('First Name')
    l_name = col2.text_input('Last Name')
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("First Name: ", f_name, " - Last Name:", l_name)

# Divider for visual separation
st.divider()

# File Upload
st.header("File Upload Section")
uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("Filename:", uploaded_file.name)

# Divider for visual separation
st.divider()

# Miscellaneous
st.header("Miscellaneous Components")
title = st.text_input("Movie title:", "Life of Brian")
st.write("The current movie title is", title)

number = st.number_input("Insert a number")
st.write("The current number is ", number)

values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)

if st.button("Say hello"):
    st.write("Hello")
else:
    st.write("Goodbye")

st.link_button("Go to Google", "https://www.google.com.vn/")

# Divider for visual separation
st.divider()

# Chat Input and Output
messages = st.container(height=200)
if prompt := st.chat_input("Say something"):
    messages.chat_message("user").write(prompt)
    messages.chat_message("assistant").write(f"Echo: {prompt}")
