import streamlit as st
from st_pages import Page, show_pages, add_page_title
from database import Database

db = Database()

def main():

    # Display Pages in the side bar
    show_pages(
        [
            Page("app.py", "Upload Resume"),
            Page("pages/search_jobs.py", "Search Jobs"),
            Page("pages/dashboard.py", "Dashboard"),
            Page("pages/generate_resume.py", "Generate Resume"),
            Page("pages/generate_cover_letter.py", "Generate Cover Letter"),
            Page("pages/applications.py", "Applications")
        ]
    )

    st.title("Please upload your resume")
    pdf = st.file_uploader("",type=["pdf"], accept_multiple_files=True)

    submit=st.button("Upload to Database")

    if submit:
        with st.spinner('Uploading...'):
            db.store_resumes(pdf)
            st.write("You have successfully uploaded your resume. Please choose a utility from the side panel next.")
    
    
if __name__ == '__main__':
    main()