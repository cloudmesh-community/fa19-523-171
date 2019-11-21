import base64
import json
import logging

from flask import Flask, jsonify, request
from six.moves import http_client


app = Flask(__name__)


def _base64_decode(encoded_str):

    num_missed_paddings = 4 - len(encoded_str) % 4
    if num_missed_paddings != 4:
        encoded_str += b'=' * num_missed_paddings
    return base64.b64decode(encoded_str).decode('utf-8')


@app.route('/processmessage', methods=['POST'])
def process():
    """Process messages with information about S3 objects"""
    message = request.get_json()
    #message = request.get_json().get('inputMessage', '')


    return jsonify({'In app code for endpoint, received message': message})


@app.errorhandler(http_client.INTERNAL_SERVER_ERROR)
def unexpected_error(e):
    """Handle exceptions by returning swagger-compliant json."""
    logging.exception('An error occured while processing the request.')
    response = jsonify({
        'code': http_client.INTERNAL_SERVER_ERROR,
        'message': 'Exception: {}'.format(e)})
    response.status_code = http_client.INTERNAL_SERVER_ERROR
    return response


if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8080, debug=True)
