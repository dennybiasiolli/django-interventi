# DJANGO INTERVENTI

A sample project using Django, django-rest-framework and related packages.


[![Updates](https://pyup.io/repos/github/dennybiasiolli/django-interventi/shield.svg)](https://pyup.io/repos/github/dennybiasiolli/django-interventi/)

[ ~ Dependencies scanned by PyUp.io ~ ]


#### Run

- Clone the project

- Create a virtual environment with Python 3

    `python3 -m venv venv`

- Activate the virtual environment

    `source venv/bin/activate`

- Use (or customize) the dev settings

    `cp mysite/settings_dev.py mysite/settings.py`

- Migrate the database

    `python manage.py migrate`

- Run the instance

    `python manage.py runserver`


#### Deploying to heroku

1. Configuring `DJANGO_SETTINGS_MODULE` for heroku

    `heroku config:set DJANGO_SETTINGS_MODULE=mysite.settings_heroku`

2. Pushing `heroku` branch to `heroku/master` branch

    ```sh
    git checkout heroku
    git rebase master
    git push heroku heroku:master
    ```

3. Migrating heroku database

    ```sh
    heroku run python manage.py migrate
    ```
