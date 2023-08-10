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
    centered_style = "<p style='text-align: center; color: blue; font-size:30px'>{}</p>"
    st.markdown(centered_style.format(diff), unsafe_allow_html=True)
    st.title("ratings")
    rate=selected_problem['rating'].values[0]
    rate_style = "<p style='font-size:20px'>{}</p>"
    st.markdown(rate_style.format(rate), unsafe_allow_html=True)
    st.title("Link")
    url_pro=selected_problem['url'].values[0]
    st.write(url_pro)
    st.title("related_topics")
    relate=selected_problem['related_topics'].values[0]
    st.write(relate)
    st.title("companies")
    com=selected_problem['companies'].values[0]
    st.write(com)
    st.title("Related problems")
    tags = selected_problem['tags'].values[0]
    for problem in tags:
        st.write(problem)
