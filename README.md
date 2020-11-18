# python-cors-proxy

A simple CORS proxy in Python/Django to fetch content from remote sites without a CORS policy. 



## Run a web server locally

1. [Install Python 3](https://developerhowto.com/2018/10/31/install-python-and-web-development-tools/)

2. Run the package installation

`pip install -r requirements-dev.txt`

(`python3 -m pip install -r requirements-dev.txt` if your default is python2)

3. Start the local web server

`python manage.py runserver`

(`python3 manage.py runserver` if your default is python2)

4. You application will be served at http://localhost:8000/

You can modify the local port (current, `8000`) running the server with an extra parameter:

`python manage.py runserver 0.0.0.0:LOCALPORT`

(`python3 manage.py runserver 0.0.0.0:LOCALPORT` if your default is python2)

## Run locally using Docker

1. Install Docker Desktop

2. Run `dockker-compose up -d` from the application folder

3. You application will be served at http://localhost:8000/

You can modify the local port (current, `8000`) changing `docker-compose.yml`

```yml
ports:
    - 'LOCALPORT:8000'
```

## Usage


You can request any URL using:

`http://your.server/?url=https://your.url/request/`

Once started your server, try for example, fetching [http://ip-api.com/json/8.8.8.8](http://ip-api.com/json/8.8.8.8):

`http://localhost:8000/?url=http://ip-api.com/json/8.8.8.8`

Sample result:

```json
{"as":"AS15169 Google LLC","city":"Mountain View","country":"United States","countryCode":"US","isp":"Level 3 Communications","lat":37.4229,"lon":-122.085,"org":"Google Inc.","query":"8.8.8.8","region":"CA","regionName":"California","status":"success","timezone":"America/Los_Angeles","zip":"94043"}
```

## Deployment to Heroku

### Install Heroku client

This command line interface (CLI) helps to do some tasks related to Heroku. 

You can install this tool following [the official guide](https://devcenter.heroku.com/articles/heroku-cli#download-and-install). 

The main steps are:

1.- For MacOS, install Homebrew and run
`brew install heroku/brew/heroku`

2.- In Ubuntu/Debian based systems, install SnapCraftand run
`sudo snap install --classic heroku`

3.- For windows, download and execute the installer.

### Create a Heroku Account 

Create an account in Heroku.com to login (https://signup.heroku.com/)


### Login into Heroku

You need an accout in Heroku.com to login.

`heroku login [--interactive]`

### Register your application in Heroku

1. Manual registration:
    1. After registation, go to https://dashboard.heroku.com/
    2. Create a new application using the button [Add] (https://dashboard.heroku.com/new-app)
2. Using Heroku CLI:
    1. Run in your project:
    `heroku apps:create your-app-name`
3. Edit `ALLOWED_HOSTS` in `corsproxy/settings.py`: 
    
```python
ALLOWED_HOSTS = [
    'localhost',
    'your-app-name.herokuapp.com'
]
```

### Asociate your repository with Heroku

Optionally, register your application as a python/django project:

`heroku buildpacks:set heroku/python`

Also, if you registered the applciation **using the web dashboard**, run this command, using the **app name** you previously registered in Heroku

`heroku git:remote -a your-app-name`

### Deploy your application

`git push heroku master`


Now your application is published at `http://your-app-name.herokuapp.com/`

