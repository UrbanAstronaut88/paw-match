#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python backend/manage.py collectstatic --no-input
python backend/manage.py migrate
python backend/manage.py loaddata breeds_fixture.json || true
python backend/manage.py loaddata breed_comparisons_fixture.json || true
