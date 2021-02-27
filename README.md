Project Skyway Connect
=================

Prerequisites
-------------
* Python
* Redis
* Postgresql (Default database) sqlite can be used for dev
* Python Imaging (jpeg/png) support if you would like to work with images
* Nginx (needed for production deployment)

Quickstart
----------




    $ git clone git@github.com:givecamp/skyway-connect.git

    $ cd skyway-connect

    $ virtualenv env

    $ source env/bin/activate

    $ pip install -r requirements.txt



Edit the settings.py and change the values to suit your needs, specifically you can change Flask security settings, security keys, Redis DB settings, and Flask mail.

If you are installing Skyway Connect locally, you will also need to replace "redis" and "postgres" with "localhost" in connection strings.

After that, copy or rename the file (.env-sample) to (.env) and adjust the settings inside, then run


    flask create-db
    flask install

and follow the instructions, that will create your database tables, and  first admin user and role.

to run the system, you can use the following management command:

    $ flask run

to use Vue and Parcel bundler for development:
```
$ npm install -g parcel-bundler
$ npm install
$ npm run watch
```
to build for production run:

    $ npm run build

Favicons Generator
-----------------
To use the favicons generator, just replace `skyway_connect/src/favicons/skyway_connect.svg` with your own logo and run:
```
$ npm run favicons
```
A full set of favicons will be generated inside `skyway_connect/static/favicons/` directory.

feel free to modify the script inside `favicons.js` to fit your needs.


Running Celery
-------------

`celery -A skyway_connect.tasks worker `

you can add `-b` to activate Celery heartbeat (periodic tasks)

A sample task that runs within the app context has been prepared for you within the `enfenro/tasks/__init__.py` file, this is helpful if you have background tasks that interact with your SQLAlchemy models.



Using Docker
------------
Feel free to adjust Docker settings inside the docker-compose.yml and Dockerfile / .env file.
then run:

    $ docker-compose up

https://asciinema.org/a/219755


License
-------

In progress...

