#!/usr/bin/python
import boto3

ec2 = boto3.resource('ec2')

servers = ec2.instances.all()

for server in servers:
  #print (server.id, server.image, server.key_name, server.public_dns_name, server.public_ip_address)
  print (server.id)
   
