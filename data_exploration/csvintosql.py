import sqlite3
import pandas as pd

from pathlib import Path

# Path to sqlite
database_path = '../coffee/coffee.sqlite'
Path(database_path).touch()

conn = sqlite3.connect(database_path)
c = conn.cursor()

c.execute('''CREATE TABLE coffee_data (Id int, Country text, Year int, Import_Volume float, Export_Volume float, Growers_Price float, Retail_Price float)''')

csv_coffee = pd.read_csv("../coffee/coffee.csv")
csv_coffee.to_sql("coffee", conn, if_exists='append', index =False)

conn.close()
# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func

# from flask import Flask, jsonify

# #################################################
# # Database Setup
# #################################################
# engine = create_engine("sqlite:///coffee.sqlite")

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(autoload_with=engine)

# # Save reference to the table
# Exports = Base.classes.exports
# Imports = Base.classes.imports
# Non_member_imports = Base.classes.nonmemberimports
# Growersprices = Base.classes.growersprices
# Retailproces = Base.classes.retailprices

# #################################################
# # Flask Setup
# #################################################
# app = Flask(__name__)

# #################################################
# # Displaying Available routes on landing page