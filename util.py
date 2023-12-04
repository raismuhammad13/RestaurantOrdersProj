# This is a util file where the connections will be performed
import pyodbc
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()


def connection_to_db():

    Server = os.getenv("Server")
    DB = os.getenv("Database")
    Trusted_Connection = os.getenv("Trusted_Connection")

    connection_string = f"Driver={{ODBC Driver 17 for SQL Server}};Server={Server};Database={DB};Trusted_Connection={Trusted_Connection};"
    
    try:
        connection = pyodbc.connect(connection_string)
        print("Connection Successfull")
    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server : {e}")
    except Exception as e:
        print(f"An unexpected error occured : {e}")
    return connection