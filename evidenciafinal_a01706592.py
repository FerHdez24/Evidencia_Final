import streamlit as st
import pandas as pd
import numpy as np
import plotly as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from bokeh.plotting import figure
import matplotlib.pyplot as plt
import altair as alt

st.title(':red[Police Incident Reports from 2018 to 2020 in San Francisco]')

df = pd.read_csv("Police_Department_Incident_Reports__2018_to_Present.csv")

st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')

mapa = pd.DataFrame()
mapa['Date'] = df['Incident Date']
mapa['Day'] = df['Incident Day of Week']
mapa['Year'] = df['Incident Year']
mapa['Police District'] = df['Police District']
mapa['Neighborhood'] = df['Analysis Neighborhood']
mapa['Incident Category'] = df['Incident Category']
mapa['Incident Subcategory'] = df['Incident Subcategory']
mapa['Resolution'] = df['Resolution']
mapa['lat'] = df['Latitude']
mapa['lon'] = df['Longitude']
mapa = mapa.dropna()

subset_data3 = mapa
police_district_input = st.sidebar.multiselect(
'Police District',
mapa.groupby('Police District').count().reset_index()['Police District'].tolist())
if len(police_district_input) > 0:
    subset_data3 = mapa[mapa['Police District'].isin(police_district_input)]
    
subset_data2 = subset_data3
Neighborhood_input = st.sidebar.multiselect(
'Neighborhood',
mapa.groupby('Neighborhood').count().reset_index()['Neighborhood'].tolist())
if len(Neighborhood_input) > 0:
    subset_data2 = mapa[mapa['Neighborhood'].isin(Neighborhood_input)]

subset_data1 = subset_data2
year_input = st.sidebar.multiselect(
'Year',
subset_data2.groupby('Year').count().reset_index()['Year'].tolist())
if len(year_input) > 0:
    subset_data1 = subset_data2[subset_data2['Year'].isin(year_input)]

subset_data = subset_data1
incident_input = st.sidebar.multiselect(
'Incident Category',
subset_data1.groupby('Incident Category').count().reset_index()['Incident Category'].tolist())
if len(incident_input) > 0:
    subset_data = subset_data1[subset_data1['Incident Category'].isin(incident_input)]
            
subset_data

st.markdown('It is important to mention that any police district can answer to any incident, the neighborhood in which it happened is not related to the police district.')

st.markdown('**Crime locations in San Francisco**')
st.map(subset_data)

st.markdown('**Crimes ocurred per Police District**')
st.area_chart(subset_data['Police District'].value_counts())

st.markdown('**Crimes ocurred per year**')
st.bar_chart(subset_data['Year'].value_counts())

st.markdown('**Type of crimes committed**')
st.bar_chart(subset_data['Incident Category'].value_counts())

st.markdown('**Subtype of crimes committed**')
st.line_chart(subset_data['Incident Subcategory'].value_counts())

agree = st.button('Click to see Resolution status')
if agree:
    st.markdown('Resolution status')
    st.bar_chart(subset_data['Resolution'].value_counts())

agree = st.button('Click to see Incident day')
if agree:
    st.markdown('**Incident day of the week**')
    fig1, ax1 = plt.subplots()
    labels = subset_data['Day'].unique()
    ax1.pie(subset_data['Day'].value_counts(), labels=labels, autopct='%1.1f%%', startangle=20)
    st.pyplot(fig1)


