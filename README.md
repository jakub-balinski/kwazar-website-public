# kwazar-website-public
Initial public version of commercial website made using Python and Flask (not updated here anymore)

Live version available [at this web adress](https://czyszczenie.bydgoszcz.pl)

## requirements
- python 3.6+
- virtualenv

## usage
the easiest way to run the website locally is to:
- create local environment by `python -m virtualenv .` in main folder
- activate local environment `source ./bin/activate`
- in your local environment use `pip install -r requirements.txt`
- run `python build.py` to create database (you can check and edit credentials to administrator's panel in `build.py`)
- (also it may be neccessary to set values in `config.json` but it's very unlikely)
- run `python run.py` to start the server. website should be available at [localhost port 5000](http://localhost:5000)

## credits
[@andreknieriem](https://github.com/andreknieriem/simplelightbox) for SimpleLightbox (used in gallery)

[@amendoa](https://github.com/amendoa/fullPageScrollPureJS) for fullPageScrollPureJS (used on landing page)

## licensing
commercial use is forbidden
