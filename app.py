import streamlit as st
import pandas as pd
from prophet.plot import plot_plotly
import plotly.express as px
import requests
from streamlit_lottie import st_lottie
import smtplib
import datetime
import matplotlib.pyplot as plt
import os
from PIL import Image
import plotly.graph_objects as go


st.set_page_config(page_title="MQH", page_icon=":tada:", layout="wide")
# ---- HEADER SECTION ----
with st.container():
    c1, c2 = st.columns(2)
    with c1:
        st.title("MQH")
        st.write(
            "Stay Ahead of the Game with MQH."
        )
        st.write("[Learn More >](https://hertshtengroup-my.sharepoint.com/:p:/p/deepak_mittal/EdQYjle-XERNjucFyRdO6oYB_deuDL44tZqnHBhVW87Idg?e=WITCcb)")
    with c2:
          
            image = Image.open('images/mqh_logo.jpeg')

            resized_image = image.resize((300, 300))

            st.image(resized_image)




def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Description
def info(title, text):
    with st.expander(f"{title}"):
        st.write(text)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding_1 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_coding_2 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_2cwDXD.json")


# Function to parse date strings
def parse_date(date_str):
    return pd.to_datetime(date_str, format='%d-%m-%Y')

st.sidebar.header('MQH')
st.sidebar.header("Select The Parameters:")
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
csv_file = st.sidebar.selectbox('**Select CSV File:**', csv_files) 
start_date = st.sidebar.date_input('**Start Date:**', parse_date('18-01-2011'))  
end_date = st.sidebar.date_input('**End Date:**', parse_date('25-01-2011'))
year = st.sidebar.selectbox('**Select Year:**', ['2011', '2012', '2013', '2014']) 

st.sidebar.markdown('''
---
Created with ❤️ by [Shivansh](https://github.com/Shivansh1203/MQH).
''')


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What we do")
        st.write("##")
        st.write(
            """
           MQH is a comprehensive online platform dedicated to providing data visualization and in-depth analysis of major moves in international markets. With a focus on empowering traders and investors, MQH offers a range of tools and resources to delve into market trends, enabling users to scrutinize charts and identify trading opportunities with precision. By offering a closer perspective on market dynamics, MQH equips users with valuable insights to make informed decisions and navigate the complexities of global trading effectively
           
            """
        )
        st.write("[Our Repository >]()")
    with right_column:
       
        st_lottie(lottie_coding_1, height=300, key="coding")
       

# ---- PROJECTS ----
with st.container():
    st.write("---")

  


# # Function to parse date strings
# def parse_date(date_str):
#     return pd.to_datetime(date_str, format='%d-%m-%Y')

# Function to visualize data
def visualize_data(csv_file, start_date, end_date, year):
    # Load the CSV file
    df = pd.read_csv(csv_file)

    # Streamlit UI
    st.title('Data Visualization')
    
    st.write(f'**CSV File Selected: {csv_file}**')  

  
    filtered_data = df[(df[f'Timestamp.{year}'] >= start_date.strftime('%d-%m-%Y')) & 
                       (df[f'Timestamp.{year}'] <= end_date.strftime('%d-%m-%Y'))]


    filtered_data[year] = pd.to_numeric(filtered_data[year], errors='coerce')

    filtered_data[year] = filtered_data[year].interpolate()

    # Toggle button to switch between graph representations
    graph_type = st.radio("**Select Graph Representation:**", ("Data Points", "Continuous"))

    # Show Matplotlib or Plotly visualization based on selected representation
    if graph_type == "Continuous":
        if not filtered_data.empty:
                plt.figure(figsize=(10, 6))
                plt.plot(filtered_data[f'Timestamp.{year}'], filtered_data[year])
                plt.xlabel('Date')
                plt.ylabel('Values')
                plt.title(f'Line Graph of Values from {year}')
                plt.xticks(rotation=45)

            
                st.pyplot(plt)
        else:   
                st.write('No data available for the selected date range.')

    elif graph_type == "Data Points":
        if not filtered_data.empty:
           fig = go.Figure()
           fig.add_trace(go.Scatter(x=filtered_data[f'Timestamp.{year}'], y=filtered_data[year],
                                             mode='lines+markers', hoverinfo='y'))
           fig.update_layout(title=f'Line Graph of Values from {year}',
                                    xaxis_title='Date', yaxis_title='Values')
           st.plotly_chart(fig)



           
        else:
            st.write('No data available for the selected date range.')
            


        

     # Calculate broader range where data was oscillating the most
    differences = filtered_data[year].diff()
    max_diff_range = differences.abs().max()
    st.write(f'**The broader range where the data was oscillating the most in {year}: ±{max_diff_range}**')

     # Calculate highest and lowest values
    highest_value = filtered_data[year].max()
    lowest_value = filtered_data[year].min()
    st.write(f'**Highest value in Timestamp.{year} column: {highest_value}**')
    st.write(f'**Lowest value in Timestamp.{year} column: {lowest_value}**')
    # else:
    #     st.write('No data available for the selected date range.')

# List available CSV files
# csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]


# csv_file = st.selectbox('**Select CSV File:**', csv_files) 
# start_date = st.date_input('**Start Date:**', parse_date('18-01-2011'))  
# end_date = st.date_input('**End Date:**', parse_date('25-01-2011'))
# year = st.selectbox('**Select Year:**', ['2011', '2012', '2013', '2014']) 

# Visualize data
visualize_data(csv_file, start_date, end_date, year)




# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Our Approach")
    text_column, image_column= st.columns((2))
    with text_column:
        st.subheader("")
        st.write(
            """
           MQH is a comprehensive online platform dedicated to providing data visualization and in-depth analysis of major moves in international markets. With a focus on empowering traders and investors, MQH offers a range of tools and resources to delve into market trends, enabling users to scrutinize charts and identify trading opportunities with precision. By offering a closer perspective on market dynamics, MQH equips users with valuable insights to make informed decisions and navigate the complexities of global trading effectively
            """
        )

    with image_column:

            image = Image.open('images/mqh_logo.jpeg')

            resized_image = image.resize((300, 300))  

            st.image(resized_image)

with st.container():
        st.subheader("Our Vision")
        st.write(
            """
            MQH is a comprehensive online platform dedicated to providing data visualization and in-depth analysis of major moves in international markets. With a focus on empowering traders and investors, MQH offers a range of tools and resources to delve into market trends, enabling users to scrutinize charts and identify trading opportunities with precision. By offering a closer perspective on market dynamics, MQH equips users with valuable insights to make informed decisions and navigate the complexities of global trading effectively
            """
        )
    
# ---- CONTACT ----

with st.container():
    st.write("---")
    st.header("Get In Touch With Us")
    st.write("##")

 
    def send_email(name, email, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("epicstruchain@gmail.com", "imttyfmbkriojftd")
        msg = f"Subject: New message from {name}\n\n{name} ({email}) sent the following message:\n\n{message}"
        server.sendmail("epicstruchain@gmail.com", "epicstruchain@gmail.com", msg)
        st.success("Thank you for contacting us.")
        
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    if st.button("Send"):
        send_email(name, email, message)

    
    st.markdown(
    """
    <style>
       
         /* Adjust the width of the form elements */
        .stTextInput {
            width: 50%;
        }
        
        .stTextArea {
            width: 20%;
        }
        /* Style the submit button */
        .stButton button {
            background-color: #45a049;
            color: #FFFFFF;
            font-weight: bold;
            padding: 10px;
            border-radius: 5px;
            width: 10%;
        }
        /* Style the success message */
        .stSuccess {
            color: #0072C6;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


