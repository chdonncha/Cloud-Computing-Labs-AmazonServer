# This script created a queue
#
# Author - Paul Doyle Nov 2015
#
#
import boto.sqs
import boto.sqs.queue
import httplib
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys

conn = httplib.HTTPConnection("ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81")
conn.request("GET", "/key")

r1 = conn.getresponse().read().split(":")


# Get the keys from a specific url and then use them to connect to AWS Service 
access_key_id = r1[0]
secret_access_key = r1[1]


# Set up a connection to the AWS service. 
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)


# Get a list of the queues that exists and then print the list out

myqueue = conn.create_queue("D14123580-%s" % sys.argv[1])

print(myqueue.id)

"""
rs = conn.get_all_queues()
for q in rs:
	print q.id
"""
