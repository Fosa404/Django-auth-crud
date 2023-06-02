#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install
<<<<<<< HEAD
# pip install -r requirements.txt
=======
>>>>>>> user-auth
pipenv install

python manage.py collectstatic --no-input
python manage.py migrate