from crypt import methods
from biorhythm import app
from flask import redirect, render_template, session
from biorhythm.manager import biorhythmManager, eventManager
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker

@app.route("/newEvent")
def get_newEvent(id=".datepicker", # identifier will be passed to Jquery to select element
           dateFormat='yy-mm-dd', # can't be explained more !
           maxDate='2018-12-30', # maximum date to select from. Make sure to follow the same format yy-mm-dd
           minDate='2017-12-01', # minimum date
           btnsId='.btnId' # id assigned to instigating buttons if needed
    ):
    biorhythm = biorhythmManager.getBioRhythm("622d0e529523a13ef2ad42f8")
    return render_template(
        "createEvent.html",
        biorhythm=biorhythm,
    )
