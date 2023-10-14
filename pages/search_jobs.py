import streamlit as st
from database import Database
from extract import extract

db = Database()

def main():

    st.title("Search LinkedIn")
    positions = st.text_input("Enter comma separated position titles")
    location = st.text_input("Enter location")

    submit = st.button("Get job postings")

    if submit:
        #Get LinkedIn json data
        extract(positions, location)

        # #Process to extract data 
        # transform()
        # #Store in DB
        # load()
        #Display by queyying db

if __name__ == '__main__':
    main()