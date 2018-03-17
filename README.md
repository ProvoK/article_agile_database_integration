# Agile database integration testing [proof of concept]

This repo is a simple example for an easy database integration testing with pytest, factoryboy and sqlalchemy.

Read the full article [here](https://medium.com/@vittorio.camisa/agile-database-integration-tests-with-python-sqlalchemy-and-factory-boy-6824e8fe33a1)


## Setup
### Database
Tests assume you have a running postgresql database.

If you have UNIX OS and postgres commands installed you can simply run 
```
docker-compose up
```
and then
```
sh init_db.sh
```

### Install dependencies
```
pipenv install
```

## Run test
```
pytest -vv
```


 ~ Have a nice day! ~

