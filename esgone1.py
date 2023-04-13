import streamlit as st
import plotly.express as px
import pandas as pd
from io import StringIO
import PIL.Image as pil

st.set_page_config(page_title="UTM ESG ASSESSMENT TOOL",
                   layout="wide",
                   page_icon="🌱",
                   )

# ----Main Page----
st.header('ESG ASSESSMENT TOOL')

# ----side bar----
logo = pil.open('logo1.jpeg')
st.sidebar.image(logo)
file1 = st.sidebar.file_uploader("")

tab1, tab2, tab3 = st.tabs(["Overview", "Categorial Progression", "Data Table"])


if file1 is not None:
    df1 = pd.read_excel(file1)

    fig1 = px.bar_polar(df1.round(decimals=1), r='PTT', theta='Symbol',
                        hover_name='Parameter',
                        color='Category',
                        color_discrete_sequence=['#0be982', '#10befa', '#ffaa01'],
                        template='plotly_dark',
                        width=750, height=700,
                        range_r=(0, 100),
           
                        )
    with tab1:
        st.plotly_chart(fig1)

    env1 = df1[(df1['Category']) == "Environment"]
    soc1 = df1[(df1['Category']) == "Social"]
    gov1 = df1[(df1['Category']) == "Governance"]

    avgova1 = sum(df1['PTT']) / (len(df1.index))
    avgenvi1 = sum(env1['PTT']) / (len(env1.index))
    avgsoc1 = sum(soc1['PTT']) / (len(soc1.index))
    avggov1 = sum(gov1['PTT']) / (len(gov1.index))

    av1 = {'Progress': [avgova1, avgenvi1, avgsoc1, avggov1],
           'Category': ["Overall", "Environment", "Social", "Governance"],
           'Des': ["Overall progress", "Environment progress", "Social progress", "Governance progress"]}
    avg1 = pd.DataFrame(av1)
    fig2 = px.bar(avg1.round(decimals=1), x='Progress',
                  y='Category',
                  orientation='h',
                  hover_name='Des',
                  hover_data='Progress',
                  color='Category',
                  color_discrete_sequence=['#f63b58', '#0be982', '#10befa', '#ffaa01'],
                  range_x=(0, 100),
                  title="Average progression of each ESG Component"
                  )
    with tab2:
        st.plotly_chart(fig2)


    with tab3:
        st.dataframe(data=df1.round(decimals=1), width=800)
