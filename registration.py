import streamlit as st
import sqlite3
import pandas as pd
conn=sqlite3.connect("register.db")
cursor=conn.cursor()

#create table

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    email text,
    phone integer,
    username text,
    pwd text
)
""")
conn.commit()

menu=["REGISTER","VIEW","LOGIN"]
choice=st.sidebar.selectbox("Menu",menu)
if choice=="REGISTER":
    email=st.text_input("EMAIL")
    phone=st.number_input("PHONE")
    username=st.text_input("NAME")
    pwd=st.text_input("PASSWORD",type="password")
    if st.button("REGISTER"):
        cursor.execute("""INSERT INTO users(email,phone,username,pwd)
        VALUES(?,?,?,?)""",(email,phone,username,pwd))
        conn.commit()
        st.success("REGISTRATION COMPLETED SUCCESSFULLY")
if choice=="VIEW":
    data=cursor.execute("SELECT * FROM users")
    st.dataframe(data)
if choice=="LOGIN":
    username=st.text_input("NAME")
    pwd=st.text_input("PASSWORD",type="password")
    if st.button("LOGIN"):
        cursor.execute("""SELECT * FROM users WHERE username=? AND pwd=?""",(username,pwd))
        result=cursor.fetchone()
        if result:
            st.success("VALID USER")
        else:
            st.success("INVALID USER")

    
        
