# API DEMO Project
> This project was created to teach about APIs

Using Flask to build a Restful API Server with Swagger document.

Integration with Flask-restplus, Flask-Cors, Flask-Testing, and Flask-SQLalchemy extensions.

### Extension:
- Restful: [Flask-restplus](http://flask-restplus.readthedocs.io/en/stable/)

- SQL ORM: [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)

- Testing: [Flask-Testing](http://flask.pocoo.org/docs/0.12/testing/)

## Installation

Install with pip3:

```
$ pip3 install -r requirements.txt
```

## Flask Application Structure
```
.______api/
|──────app/
| |────controllers/
| |────docker/
| |────models/
| |────parsers/
| |────routes/
| |────serializers/
| |────utils/
| | |────database/
| |────__init__.py
| |────__version__.py
| |────api_factory.py
| |────api.py
| |────gunicorn.config.py
| |────requirements.txt
| |────run.py

```
#### Example Usage

TODO

#### Builtin Configuration Values

SERVER_NAME: the name and port number of the server.


## Run Flask
### Run flask locally for development
```
$ python3 api/app/run.py
```
In flask, Default port is `5000`

Swagger document page:  `http://127.0.0.1:5000/api/v1/`

Go to your favorite web browser and open:
    http://127.0.0.1:5000/api/v1/  $ Check the IP address using 'docker-machine ip'

### Run with Docker

```
$ docker build -t test_api .

$ docker run -p 5000:5000 --name test_api

```

In image building, the api folder will also add into the image


## Reference

Offical Website

- [Flask](http://flask.pocoo.org/)
- [Flask Extension](http://flask.pocoo.org/extensions/)
- [Flask restplus](http://flask-restplus.readthedocs.io/en/stable/)
- [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)
- [gunicorn](http://gunicorn.org/)

Tutorial

- [Flask Overview](https://www.slideshare.net/maxcnunes1/flask-python-16299282)
- [In Flask we trust](http://igordavydenko.com/talks/ua-pycon-2012.pdf)
