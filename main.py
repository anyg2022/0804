import streamlit as st
view = [300, 200, 100, 500, 600]
st.write('# raw data')
show_raw = st.checkbox('show raw data')
if show_raw == True:
    st.write('# table')
    view

st.table(view)
st.write('# bar graph')
st.bar_chart(view)
