#! /bin/bash
apt-get install binutils libproj-dev gdal-bin
cd /app/
pip install -r requirements.txt
python manage.py runserver