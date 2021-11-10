import streamlit as st
from streamlit_folium import folium_static

import folium
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy
import statsmodels.api as sm

# Page config
st.set_page_config(
  page_title='COVID-19 Dashboard',
  layout='wide',
  menu_items={
    'Get Help': None,
    'Report a bug': None
  }
)

df = pd.read_csv('data/merged.csv')
mapdata = pd.read_csv('data/mapdata.csv')

st.markdown('## Dashboard COVID-19 cijfers wereldwijd')
st.caption('Eindopdracht Visual Analytics | 12-11-2021 | Boaz Geelhoed (500825279) en Michael Westland (500889605)')

st.markdown("""<hr style="height:1px; border:none; background-color:#efefef;" /> """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
  median_annotation = [
    dict(
      x=df['Total_Cases_Per_Million'].mean(),
      y=1.08,
      xref='x',
      yref='paper',
      text='Gemiddelde: {:,.0f}'.format(df['Total_Cases_Per_Million'].mean()),
      showarrow=True,
      arrowhead=7,
      ax=1,
      ay=1
    )
  ]

  mean_annotation = [
    dict(
      x=df['Total_Cases_Per_Million'].median(),
      y=1.03,
      xref='x',
      yref='paper',
      text='Mediaan: {:,.0f}'.format(df['Total_Cases_Per_Million'].median()),
      showarrow=True,
      arrowhead=7,
      ax=1,
      ay=1
    )
  ]

  median_shape = [{
    'line': {'color': '#540B0E', 'dash': 'solid', 'width': 1},
    'type': 'line',
    'x0': df['Total_Cases_Per_Million'].mean(),
    'x1': df['Total_Cases_Per_Million'].mean(),
    'xref': 'x',
    'y0': 0,
    'y1': 1,
    'yref': 'paper'
  }]

  mean_shape = [{
    'line': {'color': '#540B0E', 'dash': 'solid', 'width': 1},
    'type': 'line',
    'x0': df['Total_Cases_Per_Million'].median(),
    'x1': df['Total_Cases_Per_Million'].median(),
    'xref': 'x',
    'y0': 0,
    'y1': 1,
    'yref': 'paper'
  }]

  trace = go.Histogram(x=df['Total_Cases_Per_Million'], marker_color='#9E2A2B') 

  layout = go.Layout(
    title='Histogram aantal coronabesmettingen per miljoen inwoners',
    xaxis=dict(title='Aantal coronabesmettingen per miljoen inwoners'),
    yaxis=dict(title='Aantal')
  )

  fig = go.Figure(data=trace, layout=layout)

  fig.update_layout(
    font_family='Roboto',
    updatemenus=[
      dict(
        type='buttons',
        direction='right',
        x=1,
        y=1.15,
        buttons=list([
          dict(
            label='-',
            method='relayout',
            args=[{
              'shapes': [],
              'annotations': []
            }]
          ),
          dict(
            label='+',
            method='relayout',
            args=[{
              'shapes': median_shape + mean_shape,
              'annotations': median_annotation + mean_annotation}        
            ]
          )
        ])
      )
    ])

  st.plotly_chart(fig)
with col2:
  median_annotation = [
    dict(
      x=df['Total_Deaths_Per_Million'].mean(),
      y=1.08,
      xref='x',
      yref='paper',
      text='Gemiddelde: {:,.0f}'.format(df['Total_Deaths_Per_Million'].mean()),
      showarrow=True,
      arrowhead=7,
      ax=1,
      ay=1
    )
  ]

  mean_annotation = [
    dict(
      x=df['Total_Deaths_Per_Million'].median(),
      y=1.03,
      xref='x',
      yref='paper',
      text='Mediaan: {:,.0f}'.format(df['Total_Deaths_Per_Million'].median()),
      showarrow=True,
      arrowhead=7,
      ax=1,
      ay=1
    )
  ]

  median_shape = [{
    'line': {'color': '#540B0E', 'dash': 'solid', 'width': 1},
    'type': 'line',
    'x0': df['Total_Deaths_Per_Million'].mean(),
    'x1': df['Total_Deaths_Per_Million'].mean(),
    'xref': 'x',
    'y0': 0,
    'y1': 1,
    'yref': 'paper'
  }]

  mean_shape = [{
    'line': {'color': '#540B0E', 'dash': 'solid', 'width': 1},
    'type': 'line',
    'x0': df['Total_Deaths_Per_Million'].median(),
    'x1': df['Total_Deaths_Per_Million'].median(),
    'xref': 'x',
    'y0': 0,
    'y1': 1,
    'yref': 'paper'
  }]

  trace = go.Histogram(x=df['Total_Deaths_Per_Million'], marker_color='#9E2A2B') 

  layout = go.Layout(
    title='Histogram aantal coronadoden per miljoen inwoners',
    xaxis=dict(title='Aantal coronadoden per miljoen inwoners'),
    yaxis=dict(title='Aantal')
  )

  fig = go.Figure(data=trace, layout=layout)

  fig.update_layout(
    font_family='Roboto',
    updatemenus=[
      dict(
        type='buttons',
        direction='right',
        x=1,
        y=1.15,
        buttons=list([
          dict(
            label='-',
            method='relayout',
            args=[{
              'shapes': [],
              'annotations': []
            }]
          ),
          dict(
            label='+',
            method='relayout',
            args=[{
              'shapes': median_shape + mean_shape,
              'annotations': median_annotation + mean_annotation}        
            ]
          )
        ])
      )
    ])

  st.plotly_chart(fig)

st.markdown("""<hr style="height:1px; border:none; background-color:#efefef;" /> """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
  median_annotation = [
    dict(
      x=df['Vaccinatiegraad'].mean(),
      y=1.08,
      xref='x',
      yref='paper',
      text='Gemiddelde: {:,.0f}'.format(df['Vaccinatiegraad'].mean()),
      showarrow=True,
      arrowhead=7,
      ax=1,
      ay=1
    )
  ]

  mean_annotation = [
    dict(
      x=df['Vaccinatiegraad'].median(),
      y=1.03,
      xref='x',
      yref='paper',
      text='Mediaan: {:,.0f}'.format(df['Vaccinatiegraad'].median()),
      showarrow=True,
      arrowhead=7,
      ax=1,
      ay=1
    )
  ]

  median_shape = [{
    'line': {'color': '#540B0E', 'dash': 'solid', 'width': 1},
    'type': 'line',
    'x0': df['Vaccinatiegraad'].mean(),
    'x1': df['Vaccinatiegraad'].mean(),
    'xref': 'x',
    'y0': 0,
    'y1': 1,
    'yref': 'paper'
  }]

  mean_shape = [{
    'line': {'color': '#540B0E', 'dash': 'solid', 'width': 1},
    'type': 'line',
    'x0': df['Vaccinatiegraad'].median(),
    'x1': df['Vaccinatiegraad'].median(),
    'xref': 'x',
    'y0': 0,
    'y1': 1,
    'yref': 'paper'
  }]

  trace = go.Histogram(x=df['Vaccinatiegraad'], marker_color='#E09F3E') 

  layout = go.Layout(
    title='Vaccinatiegraad COVID-19 van totale bevolking met volledige vaccinatie',
    xaxis=dict(title='Vaccinatiegraad (%)'),
    yaxis=dict(title='Aantal')
  )

  fig = go.Figure(data=trace, layout=layout)

  fig.update_layout(
    font_family='Roboto',
    updatemenus=[
      dict(
        type='buttons',
        direction='right',
        x=1,
        y=1.15,
        buttons=list([
          dict(
            label='-',
            method='relayout',
            args=[{
              'shapes': [],
              'annotations': []
            }]
          ),
          dict(
            label='+',
            method='relayout',
            args=[{
              'shapes': median_shape + mean_shape,
              'annotations': median_annotation + mean_annotation}        
            ]
          )
        ])
      )
    ])

  st.plotly_chart(fig)
with col2:
  color_map = {
    'Azië': '#E09F3E',
    'Europa': '#E09F3E',
    'Afrika': '#E09F3E',
    'Noord-Amerika': '#E09F3E',
    'Zuid-Amerika': '#E09F3E',
    'Oceanië': '#E09F3E',
  } 
  fig = px.box(df, x='Continent', y='Vaccinatiegraad', title='Vaccinatiegraad COVID-19 van totale bevolking met volledige vaccinatie per continent', color='Continent', color_discrete_map=color_map)

  fig.update_layout(
    font_family='Roboto',
    yaxis=dict(title='Vaccinatiegraad (%)'),
    showlegend=False
  )

  st.plotly_chart(fig)

st.markdown("""<hr style="height:1px; border:none; background-color:#efefef;" /> """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
  trend_na = [dict(
    type="line",
    xref="x", yref="y",
    x0=0, y0=9412.22,
    x1=50000000, y1=820632.22,
    line=dict(color="#AB63FA"))
  ]

  trend_sa = [dict(
    type="line",
    xref="x", yref="y",
    x0=0, y0=10486.4,
    x1=50000000, y1=0.0272414 * 50000000 + 10486.4,
    line=dict(color="#FFA15A"))
  ]

  trend_afr = [dict(
    type="line",
    xref="x", yref="y",
    x0=0, y0=-590.898,
    x1=50000000, y1=0.0293276 * 50000000 -590.898,
    line=dict(color="#00CC96"))
  ]

  trend_eur = [dict(
    type="line",
    xref="x", yref="y",
    x0=0, y0=-485.25,
    x1=50000000, y1=0.0209529 * 50000000 -485.25,
    line=dict(color="#EF553B"))
  ]

  trend_asia = [dict(
    type="line",
    xref="x", yref="y",
    x0=0, y0=2339.75,
    x1=50000000, y1=0.0134327 * 50000000 + 2339.75,
    line=dict(color="#636EFA"))
  ]

  trend_oce = [dict(
    type="line",
    xref="x", yref="y",
    x0=0, y0=2.48912,
    x1=50000000, y1=0.0112754 * 50000000 + 2.48912,
    line=dict(color="#19D3F3"))
  ]

  fig = px.scatter(df, x='Total_Cases', y='Total_Deaths', title='Spreidingsdiagram aantal COVID-19 besmettingen tegen aantal doden', color='Continent')

  fig.update_layout(
    font_family='Roboto',
    yaxis=dict(title='Totaal aantal doden'),
    xaxis=dict(title='Totaal aantal besmettingen'),
    updatemenus=[
      dict(
          type='buttons',
          direction='right',
          x=1,
          y=1.15,
          buttons=[
              dict(label='-',
                    method='relayout',
                    args=['shapes', []]),
              dict(label='+',
                    method='relayout',
                    args=['shapes', trend_na + trend_sa + trend_afr + trend_eur + trend_asia + trend_oce])
          ]
      )
    ]
  )

  st.plotly_chart(fig)
with col2:
  st.markdown("""<br><br><br>
  <div style='margin-left:20px'>
    <b>Informatie over trendlijnen:</b>
    <ul>
      <li><b>Azië</b>: y = 0,0134327 𝑥 + 2339,75 met R² = 0,949314</li>
      <li><b>Europa</b>: y = 0,0209529 𝑥 - 485,25 met R² = 0,912805</li>
      <li><b>Afrika</b>: y = 0,0293276 𝑥 - 590,898 met R² = 0,957031</li>
      <li><b>Noord-Amerika</b>: y = 0,0162244 𝑥 + 9412,22 met R² = 0,912353</li>
      <li><b>Zuid-Amerika</b>: y = 0,0272414 𝑥 + 10486,4 met R² = 0,938173</li>
      <li><b>Oceanië</b>: y = 0,0112754 𝑥 + 2,48912 met R² = 0,995669</li>
    </ul>
  </div>
  """, unsafe_allow_html=True)

st.markdown("""<hr style="height:1px; border:none; background-color:#efefef;" /> """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
  fig = px.scatter(df, x='Total_Cases', y='Total_Deaths', title='Spreidingsdiagram aantal COVID-19 besmettingen tegen aantal doden', trendline='ols')

  fig.update_layout(
    font_family='Roboto',
    yaxis=dict(title='Totaal aantal doden'),
    xaxis=dict(title='Totaal aantal besmettingen')
  )

  st.plotly_chart(fig)
with col2:
  st.text("""
                              OLS Regression Results                            
==============================================================================
Dep. Variable:           Total_Deaths   R-squared:                       0.866
Model:                            OLS   Adj. R-squared:                  0.866
Method:                 Least Squares   F-statistic:                     1153.
Date:                Wed, 10 Nov 2021   Prob (F-statistic):           1.08e-79
Time:                        16:11:09   Log-Likelihood:                -2116.1
No. Observations:                 180   AIC:                             4236.
Df Residuals:                     178   BIC:                             4243.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
===============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------
const        4325.1879   2406.226      1.797      0.074    -423.213    9073.589
Total_Cases     0.0171      0.001     33.960      0.000       0.016       0.018
==============================================================================
Omnibus:                      207.451   Durbin-Watson:                   2.123
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             8603.212
Skew:                           4.458   Prob(JB):                         0.00
Kurtosis:                      35.674   Cond. No.                     4.97e+06
==============================================================================
""")

st.markdown("""<hr style="height:1px; border:none; background-color:#efefef;" /> """, unsafe_allow_html=True)

st.markdown("""
### Aantal coronadoden per miljoen inwoners per land

Grootte van cirkels staan in verhouding met het aantal coronadoden per miljoen.
""")

m = folium.Map(
  location=[40.866667, 34.566667], 
  zoom_start=1.5,
  tiles='CartoDB positron'
)

for lat, lng, Locatie, Dood in zip(mapdata['Latitude (average)'],
                                  mapdata['Longitude (average)'],
                                  mapdata['Country'],
                                  mapdata['Total_Deaths_Per_Million']):
  folium.CircleMarker([lat, lng],
    radius=(Dood/100),
    popup=folium.Popup(f"""<b>{Locatie}</b><p>Aantal doden per miljoen: {Dood}</p>""",
        min_width=180,
        max_width=1000
      ),
    fill=True,
    fill_opacity=0.7,
    color='#9E2A2B',
    parse_html=False
  ).add_to(m)
    
folium_static(m)
  

st.markdown("""<hr style="height:1px; border:none; background-color:#efefef;" /> """, unsafe_allow_html=True)

st.markdown(f"""
#### Bronvermelding
>CaptainClever. (2021, 12 oktober). COVID-19 Dataset (Versie 1) [Dataset]. Kaggle. https://www.kaggle.com/abhimaneukj/covid19-dataset

>Verma, A. (2021, 16 oktober). World Population Density (Versie 1) [Dataset]. Kaggle. https://www.kaggle.com/varpit94/world-population-density""")