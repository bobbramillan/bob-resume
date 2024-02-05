from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = "Resume.pdf"
profile_pic = current_dir / "assets" / "bavi_photo.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Bob Bramillan"
PAGE_ICON = ":wave:"
NAME = "Bob (Bavanan) Bramillan"
DESCRIPTION = """
ECE Sophomore @ Drexel University.
"""
EMAIL = "bob.bramillan@gmail.com"
SOCIAL_MEDIA = {
    #"YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "www.linkedin.com/in/bavananb",
    "GitHub": "https://github.com/bobbramillan",
    #"Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Personal Website temporarily hosted on GitPages with HTML, CSS, JS"
    "🏆 Income and Expense Tracker - Web app with NoSQL database"
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 2 Years experience extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: Streamlit, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write('\n')
st.write("🚧", "**Associate | 7-Eleven**")
st.write("01/2021 - 12/2023")
st.write(
    """
- ► Addressed customer inquiries and provided detailed product information
- ► Proficiently handled cash and credit transactions while overseeing store operations
- ► Inventory management, balanced cash drawers and tracked lottery sales of evening shift
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(project)
    st.write(link)
    #st.write(f"[{project}]({link})")
