import streamlit as st


name = st.text_input("Enter Your Name : ")
fname = st.text_input("Enter Your Father Name : ")
age = st.text_input("Enter Your Age : ")
adr = st.text_area("Enter Yoyr Text : ")
classdata = st.selectbox("Enter Your Class : ",(1,2,3,4,5,6,7,8,9,10,11,12,"FY","SY","TY"))

button = st.button("Done")
if button :
    st.markdown(f"""
                Name : {name}
                Father Name : {fname}
		Age : {age}
                address : {adr}
                class : {classdata}""")