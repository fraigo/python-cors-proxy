#!/bin/bash

echo "Starting..."
pwd
echo "Checking $REQUIREMENTS_FILE..."
if [ -e $REQUIREMENTS_FILE ]; then
    echo "Installing from $REQUIREMENTS_FILE"
    pip install -r $REQUIREMENTS_FILE
fi
sleep 3

python manage.py migrate    
python manage.py runserver 0.0.0.0:8000
