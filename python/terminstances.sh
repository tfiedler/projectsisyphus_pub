#!/bin/bash

./listInstances.py | awk '{print "aws ec2 terminate-instances --instance-ids", $1}'
