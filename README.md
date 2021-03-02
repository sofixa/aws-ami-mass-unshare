# aws-ami-mass-unshare
A small Python and boto3 script to unshare/make private all AMIs matching a filter

# Usage

git clone/download the stop-ami-sharing.py file, edit the filters and owners variables as per [the boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_images), and run it.