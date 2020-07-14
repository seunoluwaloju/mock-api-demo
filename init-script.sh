#!/bin/bash
sudo apt update -y
sudo apt install docker.io -y
sudo apt install awscli -y
sudo $(aws ecr get-login --region us-east-1 --no-include-email)
