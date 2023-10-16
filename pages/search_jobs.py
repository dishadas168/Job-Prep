import streamlit as st
from database import Database
from extract import extract_data
from transform import process_data

db = Database()


def main():

    st.title("Search LinkedIn")
    positions = st.text_input("Enter comma separated position titles")
    location = st.text_input("Enter location")

    col1, col2, col3 = st.columns(3)
    with col1:
        extract = st.button('Extract data')

    with col2:
        display = st.button('Display results')

    with col3:
        save_progress = st.button('Save Progress')

    if extract:
        with st.spinner('Extracting data from LinkedIn...'):
            extract_data(positions, location)
            process_data()
            st.write('Extracted data successfully!')
    
    if display:
        with st.spinner('Fetching data...'):
            df = db.get_processed()
            st.session_state['df'] = df
            
    if save_progress:
        with st.spinner('Saving...'):
            db.update(st.session_state['df'])
            st.write("Progress saved successfully!")
    
    if 'df' in st.session_state:
        edited_df = st.data_editor(st.session_state['df'],
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

        for i in range(len(edited_df)):
            st.session_state["df"][i]["applied"] = edited_df[i]["applied"]
    

if __name__ == '__main__':
    main()