import boto3
import hashlib
import json

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

passw='Namaganda.7'
encoded_password = passw.encode('utf-8')
password = hashlib.sha256(encoded_password).hexdigest()
"""
table.put_item(
   Item={
        'username': 'janedoe',
        'password': password,
        "age": 20,
        "email": "mbalireshawal@gmail.com",
        "gender": "male",
        "insurance": 'none',
        "surname": 'Mbalire',
        "other_name": 'Shawal',
        "phone_number": '0760044705',
        "role": 'patient',
        "records": {}
    }
)"""

response = table.get_item(
    Key={
        'username': 'janedoe',
        'password': password
    }
)
try:
    user = response['Item']
    print(user)
except:
    user = None
