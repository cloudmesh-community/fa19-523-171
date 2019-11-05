import json
import logging

from flask import Flask, jsonify, request
from six.moves import http_client
from google.cloud import storage


app = Flask(__name__)



@app.route('/processmessage', methods=['POST'])
def process():
    """Process messages with information about S3 objects"""
    message = request.get_data().decode('utf8')
    #message = request.get_json().get('https://console.cloud.google.com/storage/browser/fa19e516jkandima.appspot.com', '')
    # Create a Cloud Storage client.
    gcs = storage.Client.from_service_account_json('/Users/jagadeeshk/Downloads/fa19e516jkandima-829634a1b8ad.json')

    # Get the bucket that the file will be uploaded to.
    bucket = gcs.get_bucket('fa19e516jkandima.appspot.com')

    # Create a new blob and upload the file's content.
    blob = bucket.blob(message)

    blob.upload_from_string(
        message
    )

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

