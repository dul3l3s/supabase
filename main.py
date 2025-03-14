import psycopg2
from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# Connect to the database
try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    )
    print("Connection successful!")

    # Streamlit inputs
    st.text_input("Id", key="id")
    st.text_input("Desc", key="desc")

    prod_id = st.session_state.id
    prod_desc = st.session_state.desc

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # Insert into example
    cursor.execute("insert into produce (id, description) values (%s, %s)", (int(prod_id), prod_desc))

    # Example query
    cursor.execute("SELECT id, description from produce;")
    rows = cursor.fetchall()

    # Place database table into a pandas dataframe
    df = pd.DataFrame(rows)

    # Display the dataframe with streamlit
    st.dataframe(df, use_container_width=True)

    print("Results:", rows)
    for r in rows:
        print(f"{r}")

    # Commit changes
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")
    st.write(f"Failed to connect: {e}")