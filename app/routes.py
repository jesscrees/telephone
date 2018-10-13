from app import app
import requests
import logging

from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    url = 'https://api.typeform.com/forms/uOjfdY/responses'
    headers = {'Authorization': 'Bearer CGXKAsNt2tWo1PKHqFSeVtesLDxMHFvn8h9X9G44mCXQ'}

    response = requests.get(url, headers=headers)
    
    statusCode = response.status_code

    logging.warning(response.status_code)
    # logging.log(1, 'sup')
    # return response.status_code

    return render_template('main.html', statusCode=statusCode)
    # return str(response.status_code)

    

    # return "Want to play telephone?"