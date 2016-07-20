import os
from boto.s3.bucket import Bucket
from boto.s3.connection import S3Connection
from thumbor.utils import logger

def load_sync(path):
    url_by_piece = path.lstrip("/").split("/")
    bucket_name = url_by_piece[0]
    bucket_path = path.lstrip("/").lstrip(bucket_name)

    boto_opts = {
        'aws_access_key_id': os.environ.get('S3_ACCESS_KEY'),
        'aws_secret_access_key': os.environ.get('S3_SECRET_KEY'),
    }
    conn = S3Connection(**boto_opts)

    bucket_loader = Bucket(
        connection=conn,
        name=bucket_name
    )

    file_key = None

    try:
        file_key = bucket_loader.get_key(bucket_path)

    except Exception, e:
        logger.warn("ERROR retrieving image from S3 {0}: {1}".format(url, str(e))) 

    if file_key:
        return file_key.read()

    return None
