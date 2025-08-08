import streamlit as st
import pandas as pd
from web_functions import get_options, get_case

site = "https://delhihighcourt.nic.in/app/get-case-type-status"
st.set_page_config(layout="wide")
with st.form("my_form"):

    case_type = st.selectbox(
        "Select Case Type",
        get_options(site, "case_type"),
    )

    case_number = st.text_input("Enter Case Number")

    case_year = st.selectbox(
        "Select Case year",
        get_options(site, "case_year"),
    )

    submitted = st.form_submit_button()

    if submitted:
        header, rows, links = get_case(site, case_type, case_number, case_year)

        if header and rows:
            if isinstance(rows[0], str):
                df = pd.DataFrame([rows], columns=header)
            else:
                df = pd.DataFrame(rows, columns=header)

            st.subheader("Case Details")
            st.dataframe(df, use_container_width=True)

            if links:
                st.subheader("Orders & Documents")
                for i, link in enumerate(links, 1):

                    filename = link.split("/")[-1] if "/" in link else f"Document_{i}"
                    display_name = (
                        filename.replace(".pdf", "")
                        if filename.endswith(".pdf")
                        else filename
                    )
                    st.markdown(f"{i}. [{display_name}]({link})")
        else:
            st.warning("No data found for the selected case.")
