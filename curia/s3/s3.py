import sys
import json
import os
import subprocess
import boto3

class S3Handler:
    '''
    Helper class for opening connection to s3 buckets. Handles authentication and configuration.
    '''

    def __init__(self, config):
        self.client = s3 = boto3.resource(
                service_name='s3',
                region_name=config['AWS_REGION'] or os.environ['AWS_REGION'],
                aws_access_key_id=config['AWS_ACCESS_KEY_ID'] or os.environ['AWS_ACCESS_KEY_ID'],
                aws_secret_access_key=config['AWS_SECRET_ACCESS_KEY'] or os.environ['AWS_SECRET_ACCESS_KEY']
            )


class S3Data:
    '''
    Class for storing and retrieving data from Amazon Simple Storage Service (s3).
    '''

    def __init__(self, config):
        self.s3_client = S3Handler(config)


    def get_data(self, bucket_name, object_name, file_name):
        with open(file_name, 'wb') as f:
            self.s3_connection.download_fileobj(bucket_name, object_name, f)
