import streamlit as st
from database import Database
from extract import extract_data
from transform import process_data

db = Database()


def main():

    st.title("Applied Jobs")

    df = db.get_processed(applied=True)

    st.data_editor(df,
        column_order=("applied", "posted_date", 
                    "job_title", "job_location", 
                    "company_name", "salary_low",
                    "salary_high", "description",
                    "job_url"),
        column_config={
            "job_url": st.column_config.LinkColumn()
        }
    )




if __name__ == '__main__':
    main()