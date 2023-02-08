
<h2 align="center">Django Rest Framework API Scraping Amazon and Ebay Products</h2>



Fitur:
- **Scraping Products**: Copy product url from Amazon or Ebay into api request and will get response with product name, price, image_url.
- **Display Todal Scraping Product**: Display total data Scraping group by marketplace (Amazon and Ebay Products) and filter by date, range date, dan month (number:1-12).


Technology:
- **Django**
- **Django REST Framework**
- **Sqlite3**
- **Requests**
- **Beautifulsoup4**
- **lxml**
- **Gunicorn**
- **Docker**
- **Docker-Compose**
- **Nginx**
- **Github Action (CI/CD)**
- **AWS EC2**
___

# Installation
## Requirement
1. python3 (required)
2. libxml2 and libxslt (required), check this installation <a href="https://lxml.de/installation.html" >documentation.</a>
3. docker and docker-compose (only optional when deploying production using docker)
4. gunicorn and nginx (only optional when deploying production without docker)
    
## Quick start
    Clone this repository
    cd be_api

    Option 1 (running on host) Development
        1. Create virtual environment variables, "virtualenv venv" (If you don't have virtualenv, pip install virtualenv)
        2. Run virtual environment (linux: "source venv/bin/activate", windows: "venv/Scripts/activate")
        3. Install dependencies, "pip install -r requirements.txt"
        4. Setup environment variables, copy file `.env.example` to `.env` and setup configuration.
        5. Migration, "python3 manage.py migrate"
        6. Run service, "python3 manage.py runserver"
        7. To run tests (unit and integration), "python3 manage.py test --settings=be_api.test_settings"

    Option 2 (running on container)
        1   Setup environment variables, copy file `.env.example` to `.env` and setup configuration.
        2.  Run service, "docker-compose up -d", when you run it for the first time, it will create an image first, then create a container.
        3.  Migration, "docker-compose exec api /bin/sh python3 manage.py migrate && python3 manage.py runserver"
        4.  Stop service, "docker-compose down"
    
        Note: To prevent data from being lost during shutdown, a mounting process has been carried out between the database in the container and the location in the host directory (in the db directory in this project). `./db/db.sqlite3:/app/db.sqlite3`

Database testing <a href="#" >downlaod.</a>

## Continuous integration (CI) / Continuous  deployment/delivery (CD)
    Generate the SSH key on server. Adding the Public Key to authorized_keys. Setting github action environment variables on SSH_PRIVATE_KEY, SSH_HOST and SSH_USERNAME.

    Stage/Job 1 (Testing)
    1. Install python3-pip
    2. Check out repository
    3. Install requirements
    4. Setup Env
    5. Execute tests

    Stage/Job 2 (Deploy to Prodution)
    1. Install SSH Key
    2. Adding Known Hosts
    3. Deploy to Server
        - Pull repository
        - Gracefully reload the workers service

## Production
    1. Install dependencies required: libxml2 and libxslt, "sudo apt-get install libxml2-dev libxslt-dev python-dev"
    2. Install nginx, "sudo apt-get install nginx"
    3. Clone this repository, "git clone this repository and cd be_api" 
    4. Create virtual environment variables,  "virtualenv venv" (If you don't have virtualenv, pip install virtualenv)
    5. Run virtual environment, "source venv/bin/activate"
    6. Install dependencies, "pip install -r requirements.txt"
    7. Install gunicorn, "pip install gunicorn"
    8. Setup environment variables
    10. Configure Gunicorn
    11. Configure Nginx to Proxy Pass to Gunicorn

## API Documentation
    - Scraping Product
        POST: http://localhost:8000/api/scrap
        Payload:
        {
            "url":""
        }

    - Total Scraping Product
        GET: http://localhost:8000/api/scrapped/total
        GET: http://localhost:8000/api/scrapped/total?date={yyyy-mm-dd}
        GET: http://localhost:8000/api/scrapped/total?date_start={yyyy-mm-dd}&date_end={yyyy-mm-dd}
        GET: http://localhost:8000/api/scrapped/total?month={1-12}
    
Postman Export collections <a href="#" >download</a>

## DEMO
    Host: