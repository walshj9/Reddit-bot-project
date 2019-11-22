#!/bin/bash

cd ..
cd ..
source final_project/bin/activate
cd Project/Reddit-bot-project/


while :
do
	python3 reddit-bot-project.py
	echo "Press Ctrl+C to stop loop excecution"
	sleep 15
done
