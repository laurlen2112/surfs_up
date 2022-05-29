#add dependencies
import datetime as dt
import numpy as np
import pandas as pd
from sklearn.metrics import PrecisionRecallDisplay

#add SQL Alchemy depend
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#add flask depend
from flask import Flask, jsonify

#create engine
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect the db
Base = automap_base()
#reflect database
Base.prepare(engine, reflect = True)

#save reference tables
Measurement = Base.classes.measurement
Station = Base.classes.station

print(Base.classes.keys())

#create session link
session = Session(engine)

#set up flask

app = Flask(__name__)

#create welcome route
@app.route('/')
def welcome():
    return(
        '''
       <p> Welcome to the Climate Analysis API!<p>
       <p> Available Routes:<p>
       <p> /api/v1.0/precipitation<p> 
       <p>/api/v1.0/stations<p>
       <p>/api/v1.0/temp/start/end<p>
        ''' )

#create route for precip
@app.route("/api/v1.0/precipitation")

def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)


#create route for stations
@app.route('/api/v1.0/stations')

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations = stations)

#create route for temp
@app.route("/api/v1.0/tobs")

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#route for statistics
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
      sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

#learning assistant ask-153628
if __name__ == '__main__':
   app.run()
