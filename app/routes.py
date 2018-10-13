from app import app
from app import verify

import requests
import logging

from flask import request, jsonify, render_template

request_id_dict = {}

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    # Get phone number from form
    number_response = request.json['form_response']['answers'][0]['text']

    # Send verification code to phone number and get request id
    request_id = verify.send_verification(number_response)

    # Store phone number and request_id
    # print('Number:')
    # print(number_response)

    # print('Request ID:')
    # print(request_id)

    request_id_dict[number_response] = request_id
    print(request_id, number_response)

    # url_numbers = 'https://api.typeform.com/forms/NP3Ab2/responses'
    # headers_numbers = {'Authorization': 'Bearer CGXKAsNt2tWo1PKHqFSeVtesLDxMHFvn8h9X9G44mCXQ'}
    
    # response = requests.get(url, headers=headers)
    # logging.warning(response.status_code)

    # return render_template('main.html', statusCode=statusCode)
    # return str(response.status_code)

    return "flapjacks"



@app.route('/verification_code', methods=['GET', 'POST'])
def verification_code():

    # Get form response
    code_response = request.json['form_response']['answers'][0]['text']
    phone_number_param = request.json['form_response']['hidden']['phone']


    # Get the request id from the file for this phone number
    request_id = request_id_dict[phone_number_param]
    print(request_id, phone_number_param)

    verification_status = verify.check_verification(request_id, code_response)
    if verification_status == "0":
        verify.store_number(phone_number_param)

    # print('Verification Code:')
    # print(code_response)
    # print(phone_number_param)

    return "You're playing telephone"