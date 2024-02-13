# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

For the app to work you have to create an api_key and api_token(https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/)

API_KEY - trello api key
API_TOKEN - trello server token

you'll have to have created trello board and require the board_id stored in the .env file

BOARDID - trello board. 


## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Testing
pytest>=7.4.2 required

files - 

todo_app:

    - test_app.py
    - test_view_model.py
    - .env.test


Use the following to run specific test: e.g. 

```powershell
$ poetry.exe run pytest -s  .\todo_app\test_app.py
```

## DOCKER

The application now resides as a container with to instances that can be run

    - module5_todo:dev
    - module5_todo:prod

To build the containers you will need to build out the instances

DEV instance
```bash
$ docker build --target development --tag module5_todo:dev . --progress plain --no-cache
```
PROD instance
```bash
$ docker build --target production --tag todo-app:prod . --progress plain --no-cache
```

To start the application providing you have docker desktop installed run the following 

DEV instance
```bash
$ docker run --env-file ./.env -p 5000:5000 module5_todo:dev
```
PROD instance
```bash
$ docker run --env-file ./.env -p 5000:5000 module5_todo:prod
```
accessed as http://127.0.0.1:5000/

There is a means to run the following using docker-compose and two files have been provided 

    - DEV
        - todo_dev.yaml
    - PROD
        - todo_prod.yaml

DEV instance
```bash
$ docker-compose -f .\todo_dev.yaml up 
```
PROD instance
```bash
$ docker-compose -f .\todo_prod.yaml up 
```