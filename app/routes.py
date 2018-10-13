from app import app
from app import verify

import requests
import logging

from flask import request, jsonify, render_template

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():

    # Get form response
    number_response = request.json

    print('Phone number:')
    # print(request.form_response.json)
    # print(number_response)
    print(number_response['form_response']['answers'][0]['text'])
    # STEP 1: 
    # get numbers from initial typeform and verify them

    # 1.1 - Get numbers
    # url_numbers = 'https://api.typeform.com/forms/NP3Ab2/responses'
    # headers_numbers = {'Authorization': 'Bearer CGXKAsNt2tWo1PKHqFSeVtesLDxMHFvn8h9X9G44mCXQ'}
    
    # response = requests.get(url, headers=headers)

    # 1.1 - Store numbers
    # numbers_to_verify = response.items.answers

    # 1.2 - Cycle through numbers and verify them
    # for number in numbers_to_verify:
    #     logging.warning(number)

    # number_to_verify = response.phonenumber
    # request_id = verify.send_verification(number_to_verify)
    # user_code = response.code
    # statusCode = response.status_code
    # check_verification(request_id, user_code)

    # logging.warning(response.status_code)
    # logging.log(1, 'sup')
    # return response.status_code

    # return render_template('main.html', statusCode=statusCode)
    # return str(response.status_code)

    

    return "Want to play telephone??"



# @app.route('/', methods=['GET', 'POST'])
@app.route('/verification_code', methods=['GET', 'POST'])
def verification_code():

    # Get form response
    code_response = request.json

    print('Verification Code:')
    # print(request.form_response.json)
    # print(number_response)
    print(code_response['form_response']['answers'][0]['text'])
    # STEP 1: 
    # get numbers from initial typeform and verify them

    # 1.1 - Get numbers
    # url_numbers = 'https://api.typeform.com/forms/NP3Ab2/responses'
    # headers_numbers = {'Authorization': 'Bearer CGXKAsNt2tWo1PKHqFSeVtesLDxMHFvn8h9X9G44mCXQ'}
    
    # response = requests.get(url, headers=headers)

    # 1.1 - Store numbers
    # numbers_to_verify = response.items.answers

    # 1.2 - Cycle through numbers and verify them
    # for number in numbers_to_verify:
    #     logging.warning(number)

    # number_to_verify = response.phonenumber
    # request_id = verify.send_verification(number_to_verify)
    # user_code = response.code
    # statusCode = response.status_code
    # check_verification(request_id, user_code)

    # logging.warning(response.status_code)
    # logging.log(1, 'sup')
    # return response.status_code

    # return render_template('main.html', statusCode=statusCode)
    # return str(response.status_code)

    

    return "You're playing telephone"