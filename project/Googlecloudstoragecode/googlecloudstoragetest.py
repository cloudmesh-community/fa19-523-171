
def gcstest():
    from google.cloud import storage


    gcs = storage.Client.from_service_account_json('/Users/jagadeeshk/Downloads/fa19e516jkandima-829634a1b8ad.json')

    # Make an authenticated API request
    buckets = list(gcs.list_buckets())
    print(buckets)

    # Get the bucket that the file will be uploaded to.
    bucket = gcs.get_bucket('fa19e516jkandima.appspot.com')

    # Create a new blob and upload the file's content.
    message = 'test'
    blob = bucket.blob(message)

    blob.upload_from_string(
        message

    )


gcstest();
