# Simple Application Tracking System (ATS) - Powered by Gemini Pro - 1.5

**Simple ATS** is a recruitment tool that leverages Google Generative AI (
Gemini Pro 1.5) to enhance the hiring process. It automatically analyzes how
well a candidate's CV matches a job description and provides actionable
feedback for improvement. The system also summarizes job descriptions and
provides downloadable example CV templates, helping candidates align their CVs
with job requirements more effectively.

## Features

- **Job Description Analysis**: Get comprehensive information from job
  descriptions.
- **CV and Job Description Matching**: Automatically compare CV content with a
  job description and get a matching score.
- **CV Improvement Suggestions**: Receive suggestions on how to improve your CV
  to better align with the job description.
- **Example CV Templates**: Download example CV templates tailored to different
  roles.

## How to Use

1. **Upload Your CV**: Upload a PDF version of your CV.
2. **Paste the Job Description**: Paste the job description into the provided
   text box.
3. **Choose an Action**:
    - Get comprehensive information from the job description.
    - Compare your CV to the job description.
    - Get suggestions on how to improve your CV.
4. **Download Example CV**: Download an example CV to help you create or modify
   your own CV for better alignment with job roles.

## Technologies Used

- **Google Generative AI (Gemini Pro 1.5)**: For advanced Natural Language
  Processing (NLP) tasks, such as summarizing job descriptions and analyzing
  CVs.
- **Streamlit**: For building the user-friendly web interface.
- **PyPDF2**: For extracting text from PDF documents.
- **Python**: For backend logic and application control.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/simple-ats.git
    ```
2. Navigate to the project directory:
    ```bash
    cd simple-application-tracking-system
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up the environment variables in a `.env` file:
    ```
    GEMINI_API_KEY=your_gemini_pro_api_key
    ```
5. Run the Streamlit application:
    ```bash
    streamlit run main.py
    ```

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to check out
the [issues page](https://github.com/shevanfernando/simple-application-tracking-system/issues).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file
for more details.
