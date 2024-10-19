import os

import PyPDF2
import streamlit as st
from dotenv import load_dotenv
from google import generativeai as genai

from prompts.PromptManager import PromptManager

load_dotenv()  # load all the environment variables

genai.configure(api_key=os.environ["GEMINI_API_KEY"])


# Gemini Pro Response
def _get_gemini_response(prompt: str) -> str:
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text


def _extract_text_from_pdf(uploaded_pdf) -> any:
    pdf_reader = PyPDF2.PdfReader(stream=uploaded_pdf, strict=True)
    extracted_text = ""
    for page in pdf_reader.pages:
        text = str(page.extract_text())

        if text:
            extracted_text += (
                text.replace(" ", "").replace("●", "-").replace("\n", " ")
                + " "
            )

    return extracted_text


def main():
    # streamlit app
    st.header(
        "Simple ATS (Application Tracking System) - Powered by Gemini Pro - 1.5"
    )
    st.markdown(
        """Simple ATS helps streamline the recruitment process by 
        automatically analyzing how well a candidate’s CV matches 
        a job description. It provides actionable suggestions on 
        how to improve the CV for better alignment with the job
        requirements. Users can also get a concise summary of 
        the job description and access example CV templates tailored 
        to the role, making the application process easier and 
        more effective."""
    )
    jd = st.text_area("Past the Job Description")
    upload_file = st.file_uploader(
        "Upload Your CV/ Resume", type=["pdf"], help="Please upload the pdf."
    )
    submit_1 = st.button(
        "Tell me comprehensive information from Job Description"
    )
    submit_2 = st.button("Compare my CV with Job Description")
    submit_3 = st.button("How i can improve my CV")

    cv: str = ""
    prompt: str = ""

    if upload_file is not None:
        cv = _extract_text_from_pdf(upload_file)

    if submit_1:
        prompt = PromptManager.get_prompt(
            "extract_comprehensive_information_from_job_description",
            job_description=jd,
        )
    elif submit_2:
        prompt = PromptManager.get_prompt(
            "cv_and_job_description_matching_for_in_depth_ats",
            cv_text=cv,
            job_description=jd,
        )
    elif submit_3:
        prompt = PromptManager.get_prompt(
            "cv_improvement_for_ats_and_hiring_manager",
            cv_text=cv,
            job_description=jd,
        )

    if prompt:
        response: str = _get_gemini_response(prompt)
        st.subheader("The response is")
        st.write(response)


if __name__ == "__main__":
    main()
