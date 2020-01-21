#!/bin/bash
python manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
