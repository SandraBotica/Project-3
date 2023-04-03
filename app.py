import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///coffee.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Exports = Base.classes.exports
Imports = Base.classes.imports
Non_member_imports = Base.classes.nonmemberimports
Growersprices = Base.classes.growersprices
Retailproces = Base.classes.retailprices

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Displaying Available routes on landing page