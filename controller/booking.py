from flask import *
from model.booking import booking_model

booking_api=Blueprint("booking",__name__)

@booking_api.route("/api/booking", methods=['GET','POST','PATCH','DELETE'])
def get():
    if request.method == 'GET':
        return_result = booking_model.getbooking()
        get_result = return_result[0]
        get_status = return_result[1]
        if get_status == 200:
            user_name = return_result[2]
            user_email = return_result[3]
            return jsonify(get_result), user_name, user_email
        else:
            return jsonify(get_result), 403

    
    elif request.method == 'POST':
        return_result = booking_model.postbooking()
        post_result = return_result[0]
        post_status = return_result[1]
        if post_status == 200:
            return jsonify(post_result)
        elif post_status == 400:
            return jsonify(post_result), 400
        elif post_status == 403:
            return jsonify(post_result), 403
        else:
            return jsonify(post_result), 500
    
    elif request.method == 'DELETE':
        return_result = booking_model.deletebooking()
        delete_result = return_result[0]
        delete_status = return_result[1]
        if delete_status == 200:
            return jsonify(delete_result), 200
        else:
            return jsonify(delete_result), 403