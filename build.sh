#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python backend/manage.py collectstatic --no-input
python backend/manage.py migrate

python backend/manage.py loaddata backend/breeds_fixture.json
python backend/manage.py loaddata backend/breed_comparisons_fixture.json