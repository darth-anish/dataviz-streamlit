import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_csv('wdi.csv')
df['gdp_capita'] = df.gdp / df.population
df.head()

regions = df.region.unique()
regions_select = st.multiselect(label='region', options=regions)



plot = alt.Chart(df[(df.date == 2020)&(df.region.isin(regions_select))]).mark_point().encode(
    x = "gdp_capita",
    y = "fertility",
    color='region'
)
st.altair_chart(plot)