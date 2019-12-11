from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

table = dynamodb.Table("RetailDatabase")

table.update(
        StreamSpecification={
            'StreamEnabled': True,
            'StreamViewType': 'NEW_IMAGE' # Could be any of the following values 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
        },
)