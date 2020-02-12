# kwazar-website-public
Public version of commercial website made using Python and Flask

Live version available at [this web adress](https://czyszczenie.bydgoszcz.pl)

## requirements
- python 3.6+
- pipenv

## usage
the easiest way to run the website locally is to:
- create local environment by `pipenv shell` in main folder
- in your local environment use `pip install -r requirements.txt`
- run `python build.py` to create database (you can check and edit credentials to administrator's panel in `build.py`)
- run `python run.py` to start the server. website should be available at [localhost port 5000](http://localhost:5000)