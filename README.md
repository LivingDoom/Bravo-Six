# Project: Bravo-Six

Bravo-Six is an online application used to help determine eligibility for health benefits, including health insurance, welfare, and unemployment benefits. The program also provides the forms necessary to apply for benefits and attempts to auto-fill the forms based on information provided by the user. All sensitive data is permanently deleted after being used for the applicable forms, and links are provided to the submission sites. 

# Team: The Bayesian Conspiracy
 - Josh Harmon
 - Aidan Mattson
 - Alexander Yeang

# Status: Completed(ish)

# Notes

`bsix` is the app directory (a Django project root).

To run locally with Python 3.7 and Django 3.0:

`$ python manage.py runserver`

You may need to create and run some migrations.

`$ python manage.py makemigrations`

`$ python manage.py migrate`