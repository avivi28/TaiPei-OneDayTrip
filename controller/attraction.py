from flask import *
from model.attraction import attraction_model

attractions_api=Blueprint("attractions",__name__)

@attractions_api.route("/api/attractions")
def getAttractionData():
    result = attraction_model.get()
    if result == None:
        error_message = result
        return jsonify(error_message), 500
    else:
        success_data_return = attraction_model.get()
        return jsonify(success_data_return)

@attractions_api.route("/api/attraction/<attractionId>") #this is path parameter
def getDataById(attractionId):
    result = attraction_model.getId(attractionId)
    try:
        return jsonify(result)
    except TypeError: 
        return jsonify(result), 400
    except:
        return jsonify(result), 500