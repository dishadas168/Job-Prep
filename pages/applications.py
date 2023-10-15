import streamlit as st
from database import Database
from extract import extract_data
from transform import process_data

db = Database()


def main():

    st.title("Applied Jobs")
    st.write("My completed applications")
    st.text("")
    st.text("")
    df = db.get_processed(applied=True)

    st.data_editor(df,
        column_order=("applied", "posted_date", 
                    "job_title", "job_location", 
                    "company_name", "salary_low",
                    "salary_high", "description",
                    "job_url"),
        column_config={
            "applied": "Applied?",
            "posted_date": "Date posted",
            "job_title": "Job Title",
            "job_location": "Location",
            "company_name": "Company",
            "salary_low": "Min. Salary",
            "salary_high": "Max. Salary",
            "description": st.column_config.TextColumn("Description", width="medium"),
            "job_url": st.column_config.LinkColumn("Job URL", width="medium")
        }
    )




if __name__ == '__main__':
    main()