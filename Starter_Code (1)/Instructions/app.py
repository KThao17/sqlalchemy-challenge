from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine)

Base.classes.keys()

measurement = Base.classes.measurement
station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"Available Routes for Hawaiian Climate API:<br/>"
         f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start/2010-01-01<br/>"
        f"/api/v1.0/start/2010-01-01/end/2017-08-23"
    )