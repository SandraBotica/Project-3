# Import dependencies
# import datetime as dt
# import numpy as np
import pandas as pd

# import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/coffee_db')
# conn = engine.connect()

# data = pd.read_sql("SELECT * FROM coffee_data", conn)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Coffee = Base.classes.coffee

#################################################
# Flask Setup
#################################################
# Create an app, being sure to pass __name__
app = Flask(__name__)

#################################################
# Displaying Available routes on landing page
# Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to the Coffee API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/coffee_data<br/>"
        f"/api/v1.0/coffee_export<br/>"
        f"/api/v1.0/coffee_import<br/>"
        f"/api/v1.0/coffee_grower<br/>"
        f"/api/v1.0/coffee_retail<br/>"
        )



# # Creating coffee_data route 
# # Converting query into a dictionary with Country as the key and exports, imports, growers price and retial price as the values
# # Returning json representation of the dictionary

@app.route("/api/v1.0/coffee_data")
def coffee_data():
    # print("Server received request for 'coffee_data' page...")
    # Create a session (link) from Python to the DB
    session = Session(engine)
    
    coffee_dataset = session.query(Coffee.Id, Coffee.Country, Coffee.Year, Coffee.Import_Volume, Coffee.Export_Volume, Coffee.Growers_Price, Coffee.Retail_Price).all()
    
    session.close()
    
    coffee_data_list = []
    for Id, Country, Year, Import_Volume, Export_Volume, Growers_Price, Retail_Price in coffee_dataset:
        coffee_data_dict = {"Row": [Id, Country, Year, Import_Volume, Export_Volume, Growers_Price, Retail_Price]}
        coffee_data_list.append(coffee_data_dict)
    return jsonify(coffee_data_list)




# # Creating export route 
# # Converting query into a dictionary with Country as the key and exports as the value
# # Returning json representation of the dictionary

# @app.route("/api/v1.0/coffee_export")
# def coffee_export():
#     # print("Server received request for 'coffee_export' page...")
#     # Create a session (link) from Python to the DB
#     session = Session(engine)
    
#     export_dataset = session.query(Coffee.Country, Coffee.Year, Coffee.Export_Volume).all()
    
#     session.close()
    
#     export_data_list = []
#     for Country, Year, Export_Volume in export_dataset:
#         export_data_dict = {Country:[Year,Export_Volume]}
#         export_data_list.append(export_data_dict)
#     return jsonify(export_data_list)




# # Creating import route 
# # Converting query into a dictionary with Country as the key and imports as the value
# # Returning json representation of the dictionary

# @app.route("/api/v1.0/coffee_import")
# def coffee_import():
#     # print("Server received request for 'coffee_import' page...")
#     # Create a session (link) from Python to the DB
#     session = Session(engine)
    
#     import_dataset = session.query(Coffee.Country, Coffee.Year,Coffee.Import_Volume).all()
    
#     session.close()
    
#     import_data_list = []
#     for Country, Year, Import_Volume in import_dataset:
#         import_data_dict = {Country:[Year, Import_Volume]}
#         import_data_list.append(import_data_dict)
#     return jsonify(import_data_list)


# # Creating growers route 
# # Converting query into a dictionary with Country as the key and growers as the value
# # Returning json representation of the dictionary

# @app.route("/api/v1.0/coffee_grower")
# def coffee_grower():
#     # print("Server received request for 'coffee_grower' page...")
#     # Create a session (link) from Python to the DB
#     session = Session(engine)
    
#     grower_dataset = session.query(Coffee.Country, Coffee.Year, Coffee.Growers_Price).all()
    
#     session.close()
    
#     grower_data_list = []
#     for Country, Year, Growers_Price in grower_dataset:
#         grower_data_dict = {Country:[Year, Growers_Price]}
#         grower_data_list.append(grower_data_dict)
#     return jsonify(grower_data_list)



# # Creating retails route 
# # Converting query into a dictionary with Country as the key and retails as the value
# # Returning json representation of the dictionary

# @app.route("/api/v1.0/coffee_retail")
# def coffee_retail():
#     # print("Server received request for 'coffee_retail' page...")
#     # Create a session (link) from Python to the DB
#     session = Session(engine)
    
#     retail_dataset = session.query(Coffee.Country, Coffee.Year, Coffee.Retail_Price).all()
    
#     session.close()
    
#     retail_data_list = []
#     for Country, Year, Retail_Price in retail_dataset:
#         retail_data_dict = {Country:[Year, Retail_Price]}
#         retail_data_list.append(retail_data_dict)
#     return jsonify(retail_data_list)


if __name__ == "__main__":
    app.run(debug=True)