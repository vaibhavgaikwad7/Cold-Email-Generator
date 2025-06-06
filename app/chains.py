import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama3-70b-8192")


    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
        """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}
        ### INSTRUCTION:
        The scraped text is from the career's page of a website.
        Your job is to extract the job postings and return them in JSON format containing the 
        following keys: `role`, `experience`, `skills` and `description`.
        Only return the valid JSON.
        ### VALID JSON (NO PREAMBLE):    
        """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

           ### INSTRUCTION:
            You are Vaibhav, a recently graduated student from Syracuse University - with the degree of Masters in Applied Data Science. 
            Your job is to write a cold email to the HR of that job description telling that you are fit for this role.
            Also add the most relevant ones from the following links to showcase Your's portfolio: {unique_list}
            Remember you are Vaibhav, A data enthusiast looking for full time role, Your former experience include 1) AI researcher at HeadOn (description - Developed and fine-tuned LLMs (BERT, GPT) to generate meeting summaries and classify discussion sentiment (positive/negative). Integrated real-time inference into the product using REST APIs, reducing manual note-taking by 80%.Achieved 90%+ accuracy in sentiment detection through iterative model optimization and feedback loops.). 
            2) Data Science Researcher at NEXIS Student Labs (description - Built robust ETL pipelines using Python and SQL to process large volumes of medical diagnostic data. Developed predictive models that improved diagnostic accuracy and early detection rates by 25%. Designed interactive Power BI dashboards to visualize patient trends and clinical insights.)
            3) Teaching Assistant at Syracuse University (description - •	Supported 90+ students in machine learning and forecasting courses using Python and Power BI.). 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):

            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "unique_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))