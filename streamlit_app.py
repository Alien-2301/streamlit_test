import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Example 1
st.write("Hello, *World!* :sunglasses:")

# Example 2
st.write(1234)

# example 3

df = pd.DataFrame({
    'first_col': [1,2,3,4],
    'second_col': [10,20,30,40]
})

st.write(df)

# Example 4
st.write('Below is Dataframe', df, 'Above is Dataframe')

df2 = pd.DataFrame(
    np.random.rand(200,3),
    columns = ['a','b','c']
)

c = alt.Chart(df2).mark_circle().encode(
    x='a',
    y='b',
    size = 'c',
    color = 'c',
    tooltip = ['a', 'b', 'c']
)

st.write(c)