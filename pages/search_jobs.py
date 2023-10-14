import streamlit as st
from database import Database
from extract import extract_data
from transform import process_data

db = Database()


def main():

    st.title("Search LinkedIn")
    positions = st.text_input("Enter comma separated position titles")
    location = st.text_input("Enter location")

    extract = st.button("Extract data")
    if extract:
        extract_data(positions, location)
        process_data()
    
    display = st.button("Display results")
    if display:
        df = db.get_processed()
        st.session_state['df'] = df

    
    if 'df' in st.session_state:
        edited_df = st.data_editor(st.session_state['df'],
            column_order=("applied", "posted_date", 
                        "job_title", "job_location", 
                        "company_name", "salary_low",
                        "salary_high", "description",
                        "job_url"),
            column_config={
                        "job_url": st.column_config.LinkColumn()
            }
        )

        for i in range(len(edited_df)):
            st.session_state["df"][i]["applied"] = edited_df[i]["applied"]

    save_progress = st.button("Save Progress")
    if save_progress:
        db.update(st.session_state['df'])
    

if __name__ == '__main__':
    main()