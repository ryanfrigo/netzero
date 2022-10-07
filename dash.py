import streamlit as st
import json
import pandas as pd
from datetime import datetime

NAME = "NetZero"

#config
st.set_page_config(
        page_title=NAME,
        page_icon="🌞", #🔋
        layout="wide",
)

# hide streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# HEADER
st.title(NAME)
st.text("forecasting the effects of the MK2 Modified Datacenter Design")
st.text("We are also adding onsite power generation analysis to the tool. This will pave the pathway to NetZero and NetNegative targets.")
st.markdown("____")

# SIDEBAR
# st.sidebar.title("Parameters")

# BODY
mk2 = pd.read_excel("data.xlsx", sheet_name="MK2").set_index("Year")
mk2m = pd.read_excel("data.xlsx", sheet_name="MK2 Modified").set_index("Year")

def join_columns(mk2, mk2m, col_name):
        mk2 = mk2.rename(columns={col_name: "MK2"})
        mk2m = mk2m.rename(columns={col_name: "Modified"})
        df = mk2[["MK2"]].join(mk2m["Modified"])
        return df


kw_cab_df = join_columns(mk2, mk2m, "kW/Cabinet")
st.text("kW/Cabinet")
st.line_chart(kw_cab_df)

installed_cab_df = join_columns(mk2, mk2m, "Installed Cabinets")
st.text("Installed Cabinets")
st.line_chart(installed_cab_df)

average_pue_df = join_columns(mk2, mk2m, "Average PUE")
st.text("Average PUE")
st.line_chart(average_pue_df)

total_load_df = join_columns(mk2, mk2m, "Total load (MW)")
st.text("Total load (MW)")
st.line_chart(total_load_df)

energy_cost_df = join_columns(mk2, mk2m, "Energy cost ($M)")
st.text("Energy cost ($M)")
st.line_chart(energy_cost_df)

revenue_df = join_columns(mk2, mk2m, "Revenue ($M)")
st.text("Revenue ($M)")
st.line_chart(revenue_df)

st.markdown("____")
# notes = st.expander("Notes")
# notes.markdown("""

# """)