
# Job Preparation Application

## Overview

This Job Preparation Application is designed to streamline the job search and application process by integrating various tools and technologies. It offers six distinct sections to help users manage their job search effectively.

## Features

### 1. Upload Resume
https://github.com/dishadas168/Job-Prep/assets/44092220/7edec1d5-2aaf-4782-80f5-0f6f3e6f1cf3

In the "Upload Resume" section, users can upload their resume in PDF format. The application stores the document in a MongoDB database for easy access and retrieval.

### 2. Search Jobs


https://github.com/dishadas168/Job-Prep/assets/44092220/22730b8a-93e1-494e-a55a-fdaf8e82b47d



https://github.com/dishadas168/Job-Prep/assets/44092220/36368a49-b7be-4194-8597-dfc119c8e074


The "Search Jobs" section allows users to specify desired job roles and locations. The application utilizes a LinkedIn API to extract job descriptions, URLs, job details, and salary information. The results are displayed in a table format, and users can mark their application status with checkboxes, which are also saved to the database.

### 3. Applications


https://github.com/dishadas168/Job-Prep/assets/44092220/f49b462c-cd2d-43d8-bb94-475245eeb7ac


In the "Applications" section, users can view the jobs they've applied for. This provides a convenient overview of their job application history.

### 4. Generate Resume


https://github.com/dishadas168/Job-Prep/assets/44092220/d99315ac-e5f9-490d-b470-b24ba9b3b8b1


The "Generate Resume" section lets users customize their resume according to the job description. Users simply paste the job description, click submit, and receive a tailored resume in DOCX format. This document can be downloaded and edited as needed.

### 5. Generate Cover Letter


https://github.com/dishadas168/Job-Prep/assets/44092220/0cc32e7d-b819-4fac-9e2a-e0f9bab87c23


In the "Generate Cover Letter" section, users can create a customized cover letter based on the job description. The application generates a cover letter in DOCX format, which users can download and further customize.

## Technologies Used

- **UI & Display:** Streamlit
- **Programming Language:** Python
- **Database:** MongoDB Atlas
- **LinkedIn API:** RapidAPI
- **Text Generation:** OpenAI, Langchain
- **Containerization:** Docker

## Getting Started

1. **RapidAPI Key**: Before starting the application, ensure you have obtained a RapidAPI key and add it to the `.env.example` file.
2. **OpenAI API Key**: You will also need OpenAI API Key to use the GPT models. Add the key to `.env.example` file.
3. **MongoDB URI**: This application currently supports a MongoDB Database for backend storage. Add the URI to `.env.example` file.
4. Execute the following code to get started.
```shell
cp .env.example .env
pip install -r requirements.txt
streamlit run app.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
