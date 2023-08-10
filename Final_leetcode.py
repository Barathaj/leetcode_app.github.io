import streamlit as st
import pickle
import pandas as pd
with open('final_leetcode.pkl','rb') as file:
    problems= pickle.load(file)
st.title("Leetcode recommended problems")
problems_list=problems['title'].values
option=st.selectbox(
    'search the leetcode problems',
    problems_list
    )
if st.button('show recommendation'):
    selected_problem = problems[problems['title'] == option]
    diff=selected_problem['difficulty'].values[0]