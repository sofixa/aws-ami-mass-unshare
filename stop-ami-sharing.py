import boto3
from botocore.config import Config

filters = [{'Name': '', 'Values': ['']}]
owners=[]

client = boto3.client('ec2')

amis = client.describe_images(
    Filters=filters,
    Owners=owners
)

print(amis)
print(len(amis['Images']))

for a in amis['Images']:
    print(a['ImageId'])
    response = client.reset_image_attribute(
    Attribute='launchPermission',
    ImageId=a['ImageId']
    )
    print(response)
