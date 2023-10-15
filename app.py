import streamlit as st
from st_pages import Page, show_pages, add_page_title
from database import Database
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current)
sys.path.append(current + "/pages")


db = Database()

def main():
    st.set_page_config(layout="wide")

    # Display Pages in the side bar
    show_pages(
        [
            Page("app.py", "Upload Resume"),
            Page("pages/search_jobs.py", "Search Jobs"),
            Page("pages/generate_resume.py", "Generate Resume"),
            Page("pages/generate_cover_letter.py", "Generate Cover Letter"),
            Page("pages/applications.py", "Applications")
        ]
    )

    st.title("Upload resume")
    st.write("Please upload your resume in PDF format")
    pdf = st.file_uploader("",type=["pdf"])

    submit=st.button("Upload to Database")

    if submit:
        with st.spinner('Uploading...'):
            db.store_resume(pdf)
            st.write("You have successfully uploaded your resume. Please choose a utility from the side panel next.")
    
    
if __name__ == '__main__':
    main()