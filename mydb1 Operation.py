#pip3 install mysql-connector-python
import mysql.connector

# To create database variable
mydb=mysql.connector.Connect(host='localhost',
                             user='root',
                             password='Your Password',
                             database='mydb1')

mycursor=mydb.cursor()
print('Connection Establish')

import streamlit as st

def main():
    st.title('CRUD Operation With MySQL')

    option= st.sidebar.selectbox("select&Operation",("Create","Read","Update","Delete"))


    #Perform Selected Crud Operation
    if option=="Create":
        st.subheader("Create a Report")
        name=st.text_input('Enter Name')
        email=st.text_input('Enter Email')
        if st.button('Create'):
            sql='insert into user(name,email) values(%s,%s)'
            val=(name,email)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success('Record Create Successfully')
    elif option=='Read':
        st.subheader('Read a Record')
        if st.button('Read'):
            mycursor.execute('Select * from user')
            result = mycursor.fetchall()
            for row in result:
                st.write(row)
    elif option=='Update':
        st.subheader('Update a Record')
        id = st.number_input('Enter the ID',min_value=1)
        name=st.text_input('Enter New Name')
        email=st.text_input('Enter New Email')
        if st.button('Update'):
            sql='update user set name=%s, email=%s where id=%s'
            val=(name,email,id)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success('Record Update Successfully')
    elif option=='Delete':
        st.subheader('Delete a Record')
        id = st.number_input('Enter the ID',min_value=1)
        if st.button('Delete'):
            sql='delete from user where id=%s'
            val=(id,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success('Delete Record Successfully')

if __name__=='__main__':
    main()



