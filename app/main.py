import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from .chains import Chain
from .portfolio import Portfolio
from .utils import clean_text

def create_streamlit_app(llm, portfolio, clean_text):
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")

    # 💡 Custom Page Header
    st.markdown("""
        <h1 style='text-align: center; color: #4CAF50;'>💌 Cold Mail Generator</h1>
        <p style='text-align: center; font-size:16px;'>Generate personalized job application emails with AI</p>
    """, unsafe_allow_html=True)

    # 🔗 URL Input + Submit Button in Columns
    col1, col2 = st.columns([5, 1])
    with col1:
        url_input = st.text_input("🔗 Enter a Job URL", value="https://www.metacareers.com/jobs/774198984091403/")
    with col2:
        submit_button = st.button("🚀 Submit")

    if submit_button:
        try:
            with st.spinner("🔍 Extracting job data and generating email..."):
                loader = WebBaseLoader([url_input])
                data = clean_text(loader.load().pop().page_content)

                portfolio.load_portfolio()
                jobs = llm.extract_jobs(data)

                for job in jobs:
                    skills = job.get('skills', [])
                    links = portfolio.query_links(skills)
                    email = llm.write_mail(job, links)

                    # 🎯 Pretty email display box
                    st.markdown("""
                        <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; color: #212529;
                                    font-family: "Courier New", monospace; overflow-x: auto;'>
                    """, unsafe_allow_html=True)
                    st.code(email, language='markdown')
                    st.markdown("</div>", unsafe_allow_html=True)

                    # 💾 Download email
                    st.download_button("📥 Download Email", email, file_name="cold_email.txt")

                    # 🔍 Show extracted job JSON (optional)
                    with st.expander("🧠 View Extracted Job JSON"):
                        st.json(job)

        except Exception as e:
            st.error(f"❌ An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio, clean_text)
