Development Environment Setup
-----------------------------

Clone Source

    git clone git://github.com/spoon16/dblog.git
    cd dblog

Install virtualenv

    easy_install -U virtualenv

Install pip

    easy_install -U pip

Setup virtualenv

    virtualenv --no-site-packages .
    source bin/activate

Install requirements

    pip install -r requirements.txt

Create database

    createuser -U postgres `dblog_db`
    createdb -U `dblog_db` dblog_db

Initialize database schema

    cd dblog
    python manage.py syncdb

Run server

    python manage.py runserver

Deploying to Heroku
-------------------

Install heroku gem

    gem install heroku

Create an app on the cedar stack

    heroku create --stack cedar

Add database (postgres) addon

    heroku addons:add shared-database

Push code to heroku for deployment

    git push heroku master

Initialize heroku database

    heroku run bin/python dblog/manage.py syncdb


Notes
-----

Reset database

    # local
    pg_dump -s -f db.dump dblog_db
    python manage.py syncdb

    # heroku
    heroku pg:reset SHARED_DATABASE
    heroku run bin/python dblog/manage.py syncdb

Related
-------
[Getting Started with Python/Django on Heroku/Cedar](http://devcenter.heroku.com/articles/django)
