# KursyWalut - Pyramid

It is a program synchronizing the current exchange rates from the NBP website. Created as a recruitment task based on the Pyramid and Pylons Project documentation.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
1. Create your virtual environment
2. Clone this repository
3. Install requirements
4. Initialize database
5. Run app
```

### Installing and deployment with clone repository:

A step by step series of examples that tell you how to get a development env running

1. Create new virtual environment, for example with virtualenvwrapper:

```
$ pip install virtualenvwrapper
$ mkvirtualenv example_venv
```

2. Clone this repository:

```
$ (example_venv) git clone https://github.com/3Cement/KursyWalut-Pyramid
```
2.1. Change you time zone in settings.py if you are in different one than Europe/London

```
TIME_ZONE = 'Europe/London'
```

3. Installation in the folder containing setup.py file:

```
$ (example_venv) pip install -e .
```

4. Initialize database

```
$ (example_venv)  initialize_kursy_db development.ini
```

5. Run KursyWalut app:

```
$ (example_venv) $ kursy_run development.ini
```

### Installing and deployment with PyPI:

1. Create new virtual environment, for example with virtualenvwrapper:

```
$ pip install virtualenvwrapper
$ mkvirtualenv example_venv
```

2. Installation all required files:

```
$ (example_venv) pip install waitress pyramid-tm zope.sqlalchemy pyramid-chameleon pyramid-debugtoolbar
```

3. Installation KursyWalut app from PyPI:

```
$ (example_venv) $ python3 -m pip install --index-url https://test.pypi.org/simple/ kursy
```

4. Initialize database

```
$ (example_venv) initialize_kursy_db development.ini
```

5. Run KursyWalut app:

```
$ (example_venv) $ kursy_run development.ini
```

## Screenshots

After runserver you should see something like that in your localhost (deafult port: http://127.0.0.1:6550/)

![](images/KursyWalut)

## Running the tests

Run tests from folder with manage.py file:

```
$ (example_venv) py.test test kursy/tests.py -q
```

## Built With

* [Pyramid](https://trypyramid.com/) - The web framework used
* [PylonsProject](https://docs.pylonsproject.org) - Web development with Pyramid tutorial
* [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL toolkit and ORM
* [PyPA](https://packaging.python.org/) - Python Packaging User Guide

## Contributing

Please feel free to contribute this project and contact me for questions.

## Authors

* **Daniel Milewski** - https://github.com/3Cement

See also the list of [contributors](https://github.com/3Cement/KursyWalut-Pyramid/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Big thanks to developers for creating amazing Pylons Project tutorial which helps me to learn Pyramid
