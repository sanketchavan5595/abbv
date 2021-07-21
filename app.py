import streamlit as st 
from bs4 import BeautifulSoup
import requests
import time


# st.header('Hello world')

st.title("Hey Guys")
st.header('This is simple webapp for finding fullforms')
st.subheader("Enter the Abbreviation")
abbv = st.text_input("")

try:
    url = 'https://www.abbreviations.com/{}'.format(abbv)
    page = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(page.text, 'lxml')

    i = 1
    st.subheader('Full forms: ')
    tbodies = soup.find_all('td', class_ = 'tal dx fsl')
    for tbody in tbodies:
        full_form = tbody.find('p', class_ ='desc')
        st.write('{}'.format(full_form.text))
        i = i + 1
    st.balloons()
except:
    st.write('')

st.sidebar.markdown('''
created by Sanket Chavan 
''')

st.sidebar.markdown('''
Connect on <a href = "https://www.linkedin.com/in/sanket-chavan5595/" target = "_blank"> Linkedin </a>
''', True)