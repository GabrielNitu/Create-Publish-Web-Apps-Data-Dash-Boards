import streamlit as st
import pandas


data ={
  'Series_1':[1, 2, 3, 4, 7],
  'Series_2':[10, 30, 40, 100, 250]
}
df = pandas.DataFrame(data)
st.title('Our First Streamlit App')
st.subheader('Introducing Streamlit in Automate Everything with Python')
st.write(''' 
Aceasta este prim apagină web.
''')
st.write(df)