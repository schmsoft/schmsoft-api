#PREREQUISITE
To follow along setting up this app, ensure that you have the following:

<ul>
<li> docker
<li> docker-compose
</ul>

# SETUP

<ol>
<li>

### GETTING THE PROJECT

`git clone <repo-url>`
`cd <project-directory>`

</li>
<li>

### CREATE A DOCKER IMAGE

`docker-compose build`

</li>

<li>

### RUN API AND DB CONTAINERS

`docker-compose up`

</li>

<li>

### CONFIRM CONTAINERS ARE RUNNING

`docker ps -a`

You should see two containers running, namely.

<ul>
<li>schmsoft-api</li>
<li>schmsoft-api_db_1</li>
</ul>

</li>

<li>

###

`docker exec -it schmsoft-api ./manage.py makemigrations`

</li>

<li>

###

`docker exec -it schmsoft-api ./manage.py migrate`

</li>

<li>

### CREATE LOGIN CREDENTIALS

`docker exec -t schmsoft-api ./manage.py createsuperuser`

</li>

<li>

### RUN THE APP LOCALLY

<ul>

<li>
use the following address in your browser `http://localhost:8000`
</li>

<li>
use the credentials created in <strong> step 6 </strong>to login
</li>
</ul>

</li>

</ol>
