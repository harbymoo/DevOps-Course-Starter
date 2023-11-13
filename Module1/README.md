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

## ANSIBLE



Deployment of the package will be carried out using ansible as a deliver mechanism

The following is the layout of the files:

```bash
DevOps-Course-Starter/Module1/ansible/
├── ansible.cfg
├── files
│   └── todoapp.service
├── hosts
├── master_playbook_template.yml
├── module4_playbook.yml
├── secrets.yml
├── teardown_playbook.yml
└── templates
    └── env.j2
```

To run the ansible playbook 

```bash
cd /home/ec2-user/DevOps-Course-Starter/Module1/ansible
# To run the playbook with debug output
/usr/local/bin/ansible-playbook module4_playbook.yml --ask-vault-pass
# Alternatively to run WITHOUT debug output
/usr/local/bin/ansible-playbook module4_playbook.yml --ask-vault-pass --skip-tags debug_output

follow the prompts and this will create what is needed to run the todoapp
play #1 (module4): module4    TAGS: []
  tasks:
    create user todoapp       TAGS: []
        debug for user    TAGS: [debug_output]
    package installation      TAGS: []
        debug     TAGS: [debug_output]
    installation of poetry    TAGS: []
        debug     TAGS: [debug_output]
    create directory  TAGS: []
        dir output        TAGS: [debug_output]
    Example clone of a single branch  TAGS: []
        output git clone  TAGS: [debug_output]
    poetry update     TAGS: []
        debug     TAGS: [debug_output]
    Create .env from template TAGS: []
        debug template    TAGS: [debug_output]
    copy the service file     TAGS: []
        debug service     TAGS: [debug_output]
    systemd enable    TAGS: []
        debug systemd     TAGS: [debug_output]
