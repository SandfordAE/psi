# PSI setup

PSI is a Django SaaS website template.  
This stack is achieved by leveraging DaisyUI/Tailwind, Htmx, Neon Postgres, AllAuth, Git and more.

The goal of this project is to create a reusable template/boileLrplate SaaS for building out different SaaS products quickly.  
When completed this site will span multiple products and give you a solid foundation to sell your services from.

&nbsp;  

## Getting Started

- ### Create a basic Django instance

#### Setup the working directories and cloning the project

Open your terminal of choice and navigate to your work folder.

```bash
cd ~/Development/Websites
```

Make a new project directory and enter it.  
We'll call this one "psi".

```bash
mkdir psi
```

```bash
cd psi
```

- We should now have a new directory at  ```/home/san/Desktop/Development/Websites/psi/``` to work out of.

&nbsp;  

Create a Git-Clone folder for an on hand copy of the project.

```bash
mkdir Git-Clones
```

- ***We can change this later for my own repo***

Enter the folder and clone the "CFE" repository for an offline reference.

```bash
cd Git-Clones
```

```bash
git clone https://github.com/codingforentrepreneurs/SaaS-Foundations
```

Back out of the folder.

```bash
cd ..
```

&nbsp;  

#### Create a Virtual Environment

From the ```~/Development/Websites/psi``` folder.

- *Linux/macOS*

Create the "virtual environment".

```bash
python -m venv VENV
```

Activate the environment.

```bash
source VENV/bin/activate
```

Our terminal should now look like this.  

- *with (VENV) active*  
```┌──(VENV)─(san@TC-Arch)-[~/…/Development/Websites/psi/src]```  
```└─$```

- Simply type "deactivate" to exit VENV.  
```┌──(san@TC-Arch)-[~/Desktop/Development/Websites/psi]```  
```└─$```

&nbsp;  

### Prepare System files

We will need to create a....

- requirements.txt
- .env  
- .gitignore
- Dockerfile

&nbsp;  

#### Import the files from our cloned project

*NB there are raw copies of these files at the base of this page.*

To create  - ```~/Development/psi/requirements.txt```

```bash
sudo cp ~/Development/psi/Git-Clone/requirements.txt ~/Development/psi/requirements.txt
```

To create  - ```~/Development/psi/.env```

```bash
sudo cp ~/Development/psi/Git-Clone/.env.sample ~/Desktop/Django/.env
```

To create  - ```~/Development/psi/.gitignore```

```bash
sudo cp ~/Development/psi/Git-Clone/.gitignore ~/Desktop/Django/.gitignore
```

Or you can copy this boilerplate one provided by [GitHub](https://github.com/github/gitignore/blob/main/Python.gitignore).

- *Make sure you add the VENV to the new .gitignore file.*

&nbsp;

To create  - ```~/Development/psi/Dockerfile```

```bash
sudo cp ~/Development/psi/Git-Clone/Dockerfile ~/Desktop/Django/Dockerfile
```

&nbsp;  

#### Install Requirements.txt

If we were unable to clone the file we can also use the "echo" command to to manually create it..

```bash
echo "Django>=5.0,<5.1
gunicorn
python-decouple
psycopg[binary]
dj-database-url
requests
whitenoise
django-allauth[socialaccount]
django-allauth-ui
django-widget-tweaks
stripe" 
> requirements.txt
```

With our VENV active,  
Upgrade pip (Optional).

```bash
pip install --upgrade pip
```

Install the contents of requirements.txt

```bash
pip install -r requirements.txt
```

&nbsp;  

#### Prepare the ".env" file

We will be using Django Decouple to utilize our .env file.  
But first we need to populate the values of the file.

Create a new ```DJANGO_SECRET_KEY``` for ```~/Development/Websites/psi/core/settings.py```

- *Here' are 3 different ways to do the same thing....*

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

- *or*

```bash
openssl rand -base64 64
```

- *or*

```bash
python -c 'import secrets; print(secrets.token_urlsafe(64))'
```

All are acceptable ways to generate a new key.

Once you have this value, add update `DJANGO_SECRET_KEY` value within the  ```~/Development/Websites/psi/.env``` file.

&nbsp;  

### New project and SuperUser

#### Django-admin startproject

From the ```~/Development/Websites/psi``` folder.

Enter the src directory we created.

```bash
cd src
```

With our VENV active,  
We can now start a new project called core.

```bash
django-admin startproject core .  
```

- *N.B. The dot at the end means create it in this directory.*

&nbsp;  

#### Run Migrations

```bash
python manage.py makemigrations
```

- *and then.*

```bash
python manage.py migrate
```

Create a Superuser.

```bash
python manage.py createsuperuser
```

&nbsp;  

#### Run the Server

```bash
python manage.py runserver 8888
```

And if we navigate to the site @.

```bash
http://localhost:8888
```

We should be ready to roll

&nbsp;  

### Provision 3rd Party services

#### Neon

We will need an API key for our database.

- [NeonDB](https://kirr.co/eu0b31) Account & Postgres Database with an API key

1. Sign up with [Neon](https://kirr.co/eu0b31) to create an account.
1. Get or create a PostgresDB Secret API Key (Dashboard > Developers > API keys > *Secret key* )
1. Update *dotenv* (`.env`) file with the value `DATABASE_URL` with your key.

#### Stripe

Same will go for our payment provider

- Create a Stripe Account

1. Sign up on [Stripe.com](https://www.stripe.com) for an account
1. Get or create a Stripe Secret API Key (Dashboard > Developers > API keys > *Secret key* )
1. Update *dotenv* (`.env`) file with the value `STRIPE_SECRET_KEY` with your key.

&nbsp;  

### First Views, Urls, Models and Templates

#### First view

```~/Development/Websites/psi/src/core/views.py```

Create the file

```bash
touch ~/Development/Websites/psi/src/core/views.py
```

Insert the function using the "echo" command.

```bash
echo 'from django.shortcuts import render
from django.http import HttpResponse 
from visits.models import PageVisit

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": (page_qs.count() * 100 / qs.count()),
        "total_visit_count": qs.count(),
    }

    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)
' > ~/Development/Websites/psi/src/core/views.py
```

#### First url route

```~/Development/Websites/psi/src/core/urls.py```
should already exist.  
Insert the function using the "echo" command.

```bash
echo 'from django.contrib import admin
from django.urls import path

from .views import home_page_view

urlpatterns = [
    path("", home_page_view),
    path('admin/', admin.site.urls),
]
' > ~/Development/Websites/psi/src/core/urls.py
```

&nbsp;  

#### First Template

First of all we'll need a templates folder as per convention.

```bash
cd src
```

Create the folders

```bash
mkdir templates
```

That gives us the
```~/Development/Websites/psi/src/templates```
that we need.  
We'll also be in need of a
```~/Development/Websites/psi/src/snippets```
folder.

```bash
mkdir templates/snippets
```

With our folders created now we need to create the templates,  
To get us started we'll just create 3 simple Html pages.

1. base.html
1. src/templates/home.html
1. welcome-user-msg.html

&nbsp;  

##### Create the templates

- Once again we'll use the "echo" command to to manually create them..

###### Our base.html at ```src/templates/base.html```

```bash
echo '<!DOCTYPE html>
<html>
    <head>
        <title>{% block head_title %}SaaS Template{% endblock head_title %}</title>
    </head>
    <body>

        {% block content %}
        <h1>{{ page_title }}</h1>
        {% endblock content %}

    </body>
</html>
' > ~/Development/Websites/psi/src/templates/base.html
```

&nbsp;

###### Our home.html at ```src/templates/home.html```

```bash
echo '
{% extends "base.html" %}

{% block head_title %} {{ block.super }} - {{ page_title }} {% endblock head_title %}


{% block content %}
    <h1>{{ page_title }}</h1>
    <p>Hello Again!</p>

    {% include "snippets/welcome-user-msg.html" %}

    <p> Page Visits: {{ page_visit_count }} </p>
    <p> Total Visits: {{ percent }} % </p>
    <p> Total Visits: {{ total_visit_count }} </p>
    <p>User:  {{ request.user }} </p>
    <p>Method: {{ request.method }} </p>
    <p>Is Authenticated: {{ request.user.is_authenticated }}</p>

{% endblock content %}
' > ~/Development/Websites/psi/src/templates/home.html
```

&nbsp;

###### Our welcome-user-msg.html at ```src/templates/snippets/welcome-user-msg.html```

```bash
echo '<div>
    {% if request.user.is_authenticated %}
    You are a user 
    {% else %} 
    You are not a user 
    {% endif %}
</div>' > ~/Development/Websites/psi/src/templates/snippets/welcome-user-msg.html
```

&nbsp;  

##### Templates "BASE_DIR" --> settings\.py

In order for Django to be able to find our templates we will need to make some configurations within our Settings\.py file.  
Located at ```~/Development/Websites/psi/src/core/settings.py```.  
On ```Line 57``` we should edit it to point to our folders.

```bash
        'DIRS': [BASE_DIR / "templates"],
```

&nbsp;  

***

&nbsp;  

- With that now completed we should have a basic but working shell of a django website.

- If we run the server we should see working examples of Django's Template Inheritance, Conditions, & Include functionality.

&nbsp;  

***

#### First Model

In order to demonstrate the development of a model we will create a new app.

##### Create our first app

```bash
python manage.py startapp visits
```

&nbsp;

We should now have our new app fleshed out at ```/home/san/Desktop/Development/Websites/psi/src/visits/```  
with a new ```models.py``` file within it.

&nbsp;

Once agin using echo" copy and paste this to terminal

```bash
echo 'from django.db import models

# Create your models here.
class PageVisit(models.Model):
    # db -> table
    # id -> hidden -> primary key -> autofield -> 1, 2, 3, 4, 5
    path = models.TextField(blank=True, null=True) # col
    timestamp = models.DateTimeField(auto_now_add=True) # col
' > ~/Development/Websites/psi/src/visits/models.py
```

&nbsp;

In order for Django to be able to find our new app and its configurations we' wi'll need to make some more configurations within our Settings\.py file.  
Located at ```~/Development/Websites/psi/src/core/settings.py```.  
This time it'll be to the "INSTALLED_APPS" section.  
somewhere around  ```Line 40``` we should add the app to the existing list.

```bash
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'visits',
]
```

&nbsp;

##### Run migrations again

```bash
python manage.py makemigrations
```

- *and then.*

```bash
python manage.py migrate
```

We should have a nice baseline app that we can start to prepare for deployment.

&nbsp;

## Git & preparing for Github

### Initiate Git within our working directory

From within our ```~/Development/Websites/psi``` folder run the command..

```bash
git init
```

- And then we should run

```bash
git branch -m main
```

### Set our local Git identity

```bash
  git config --global user.email "you@example.com"
```

- *Replacing you email*

```bash
  git config --global user.name "Your Name"
```

- *And replacing you username*

&nbsp;

### First Commit

Now when we run ```git status``` we should get some output.

```bash
git status
```

- *Then*

```bash
git add --all
```

- *And*

```bash
git commit -m "Very First Commit Msg"
```

&nbsp;

### First push to GitHub

At this stage we will need to go to [GitHub](https://github.com/) and create a new repo called psi.

Once thats done we will need to link our project to the newly created repo.

```bash
git remote add origin https://github.com/SandfordAE/psi.git
```

And now that our project is linked to Github we should be able to push it with the command,

```bash
 git push -u origin main
```

And now if we check within the repo on GitHub we should see our code there.

&nbsp;

&nbsp;

## Prepare our code for deployment

ALLOWED_HOSTS

Django Decouple

1:48:01

```bash

```

```bash

```

```bash

```

```bash

```

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

***

***

***

***

***

***

***

***

## =============================

Much more coming soon!

### Pull Vendor Static Files

```bash
python manage.py vendor_pull
```

```js

































## Your First HTML Webpage with Python Functions

## Rendering HTML Documents

## Using Django Templates

## Django Template Inheritance, Conditions, & Include

## Store and Retrieve Data Part 1

## Store and Retrieve Data Part 2

## Push to GitHub via Git

## Prepare for Production Environment

## Deploy Django to Railway with Docker Containers

## The Hard Way to Manage Environment Variables

## dotenv and Python Decouple to Manage Environment Variables




## Provision a Serverless PostgreSQL Database with Neon

## Integrate PostgreSQL with Django

## Neon in Production + Database Branching

## Styling with CDN for TailwindCSS and Flowbite

## Configure Django Static Files in Dev

## Download Url to Local File Helper Function

## Custom Django Management Command to Pull Vendor Files

## Missing Args with Container Build in Railway

## Configure Django to use Email with Gmail

## Django Admin User + User Passwords

## Django Login View Logic

## HTML Login Form and Template

## Register Users the Hard Way

## Configure Django AllAuth

## User Email Verification with Django AllAuth

## Better UI for Django AllAuth

## Navbar Links for Auth

## Login with GitHub via Django AllAuth

## Password Protected Page with Django Sessions

## User-required Pages via login_required Decorator

## Staff User Required

## User Profile View

## User Permissions and has_perm

## User Permissions in Django Templates

## Groups & Group-level Permissions

## Custom Permissions for Django Users

## Groups and Permissions within Subscriptions

## Syncing Subscription Groups and Permissions

## Sync User Subscription with the User Group Part 1

## Sync User Subscription with the User Group Part 2

## Getting Started with Stripe

## Django Customer Model

## Override Django Save to Create Stripe Customer

## DjangoAll Auth Signal to Confirm Django Stripe Customers

## Our Django Subscription Model as a Stripe Product

## Subscription Price Model

## Manage Prices in Django Admin with Tabular Inlines

## Featured and Ordered Pricing

## Subscription Pricing View & Template

## Pricing Table based on QuerySets

## Pricing Interval Toggle Views

## A Django Session Based Checkout Process

## Stripe Checkout Session

## Stripe Checkout Finalize View in Django

## Successful Purchase to User Subscription Model

## Auto Cancel Subscription on New Plan

## Adding Subscription Billing Period Dates

## User Subscription Status Field

## User Subscription View and Refresh

## User Subscription Cancel View

## Cancel Dangling User Subscriptions

## Custom Django Management Command with Arguments

## Subscription Refresh Utility Function

## Custom Django Model QuerySets and Model Managers

## Filtering Django Models with Datetime Objects

## Hello World from GitHub Actions

## Testing Django Basics with GitHub Actions

## Environment Variables in GitHub Actions

## Github Actions Secrets for Database URL

## Branch Neon DB for Django Tests

## Scheduled Production Worker with Django Neon Stripe and GitHub Actions

## A Better Landing Page with Flowbite

## Using the SaaS Theme to Fix Missing Tailwind Classes

## Dashboard View

## Decouple Dashboard






















```

***

## Create New System Files

Some standard files needed to get most Django projects up and running.

### Create a ".gitignore"

- *For now we'll just create the file and we can edit it as we go.*

```bash

# Ignore our virtual environment
VENV/

# ignore vendor static files
src/staticfiles/vendors

# ignore local static file root
# or "local cdn"
local-cdn/

# ignore VSCode Workspace file
*.code-workspace

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
.pdm.toml
.pdm-python
.pdm-build/

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/


# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*
.pnpm-debug.log*

# Diagnostic reports (https://nodejs.org/api/report.html)
report.[0-9]*.[0-9]*.[0-9]*.[0-9]*.json

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Directory for instrumented libs generated by jscoverage/JSCover
lib-cov

# Coverage directory used by tools like istanbul
coverage
*.lcov

# nyc test coverage
.nyc_output

# Grunt intermediate storage (https://gruntjs.com/creating-plugins#storing-task-files)
.grunt

# Bower dependency directory (https://bower.io/)
bower_components

# node-waf configuration
.lock-wscript

# Compiled binary addons (https://nodejs.org/api/addons.html)
build/Release

# Dependency directories
node_modules/
jspm_packages/

# Snowpack dependency directory (https://snowpack.dev/)
web_modules/

# TypeScript cache
*.tsbuildinfo

# Optional npm cache directory
.npm

# Optional eslint cache
.eslintcache

# Optional stylelint cache
.stylelintcache

# Microbundle cache
.rpt2_cache/
.rts2_cache_cjs/
.rts2_cache_es/
.rts2_cache_umd/

# Optional REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# Yarn Integrity file
.yarn-integrity

# dotenv environment variable files
.env
.env.development.local
.env.test.local
.env.production.local
.env.local

# parcel-bundler cache (https://parceljs.org/)
.cache
.parcel-cache

# Next.js build output
.next
out

# Nuxt.js build / generate output
.nuxt
dist

# Gatsby files
.cache/
# Comment in the public line in if your project uses Gatsby and not Next.js
# https://nextjs.org/blog/next-9-1#public-directory-support
# public

# vuepress build output
.vuepress/dist

# vuepress v2.x temp and cache directory
.temp
.cache

# Docusaurus cache and generated files
.docusaurus

# Serverless directories
.serverless/

# FuseBox cache
.fusebox/

# DynamoDB Local files
.dynamodb/

# TernJS port file
.tern-port

# Stores VSCode versions used for testing VSCode extensions
.vscode-test

# yarn v2
.yarn/cache
.yarn/unplugged
.yarn/build-state.yml
.yarn/install-state.gz
.pnp.*

```

***

### Create the "Dockerfile"

- *For now we'll just create the file and we can edit it as we go.*

```bash
# Set the python version as a build-time argument
# with Python 3.12 as the default
ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}

# Create a virtual environment
RUN python -m venv /opt/venv

# Set the virtual environment as the current location
ENV PATH=/opt/venv/bin:$PATH

# Upgrade pip
RUN pip install --upgrade pip

# Set Python-related environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install os dependencies for our mini vm
RUN apt-get update && apt-get install -y \
    # for postgres
    libpq-dev \
    # for Pillow
    libjpeg-dev \
    # for CairoSVG
    libcairo2 \
    # other
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Create the mini vm's code directory
RUN mkdir -p /code

# Set the working directory to that same code directory
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /tmp/requirements.txt

# copy the project code into the container's working directory
COPY ./src /code

# Install the Python project requirements
RUN pip install -r /tmp/requirements.txt

ARG DJANGO_SECRET_KEY
ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}

ARG DJANGO_DEBUG=0
ENV DJANGO_DEBUG=${DJANGO_DEBUG}

# database isn't available during build
# run any other commands that do not need the database
# such as:
RUN python manage.py vendor_pull
RUN python manage.py collectstatic --noinput
# whitenoise -> s3

# set the Django default project name
ARG PROJ_NAME="SaasTemp"

# create a bash script to run the Django project
# this script will execute at runtime when
# the container starts and the database is available
RUN printf "#!/bin/bash\n" > ./paracord_runner.sh && \
    printf "RUN_PORT=\"\${PORT:-8000}\"\n\n" >> ./paracord_runner.sh && \
    printf "python manage.py migrate --no-input\n" >> ./paracord_runner.sh && \
    printf "gunicorn ${PROJ_NAME}.wsgi:application --bind \"0.0.0.0:\$RUN_PORT\"\n" >> ./paracord_runner.sh

# make the bash script executable
RUN chmod +x paracord_runner.sh

# Clean up apt cache to reduce image size
RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Run the Django project via the runtime script
# when the container starts
CMD ./paracord_runner.sh

```

### Create a new .env file

- *For now we'll just create the file and we can edit it as we go.*

```bash
sudo cp ~/Desktop/Django/Git-Clone/.env.sample ~/Desktop/Django/.env
```

```bash
cat .env
```

- *Output* should look like this

```python
Values include:
- `DJANGO_DEBUG=1`
- `DJANGO_SECRET_KEY=""`
- `DATABASE_URL=""`
- `EMAIL_HOST="smtp.gmail.com"`
- `EMAIL_PORT="587"`
- `EMAIL_USE_TLS=True`
- `EMAIL_USE_SSL=False`
- `EMAIL_HOST_USER=""`
- `EMAIL_HOST_PASSWORD=""`
- `ADMIN_USER_EMAIL=""`
- `STRIPE_SECRET_KEY=""`

```

### Create a License agreement

Copy this command into a terminal within the src directory

```bash

echo "MIT License

Copyright (c) $(date +"%Y") SandfordAE

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE." > ~/Development/Websites/psi/src/LICENSE
```
