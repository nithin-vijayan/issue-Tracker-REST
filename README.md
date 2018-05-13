# issue-Tracker-REST
REST API for tracking and assigning issues to Users

### Repo requires redis server running as message broker to work as expected

Use ```brew install redis``` in OSX for installing redis

# Setup:

All the required packages are defined in requirements.txt

1. Clone the repository to you local system ```git clone git@github.com:nithin-vijayan/issue-Tracker-REST.git```

2. Create and activate virutual env using ```virtualenv <venv-name>``` then ```source <venv-name>/bin/activate```

3. run  ```pip install -r requirements.txt```  for installing all the required packages.

4. Set following env variables or define them in .env file at the root of Project
```
SECRET_KEY=8f72*-eih5h-h2(!-f7rp&%9+s0t-(0n_c&%o-s@q2ob=4^a6r
DEBUG=True
ALLOWED_HOSTS=127.0.0.1
EMAIL_HOST=<server>
EMAIL_HOST_USER=<username>
EMAIL_HOST_PASSWORD=<password>
EMAIL_PORT=<port>
REPORT_SCHEDULE_SECONDS=0
REPORT_SCHEDULE_MINUTES=0
REPORT_SCHEDULE_HOURS=24
ASSIGN_REPORT_SCHEDULE=12
DATABASE_URL=<postgres-db-url>
```

EMAIL_HOST - server from which django will send email
EMAIL_PORT - port number for mail server
EMAIL_HOST_USER - username of mail account
EMAIL_HOST_PASSWORD - account password
ASSIGN_REPORT_SCHEDULE -( in Minutes )Controls when to trigger email after issue is asigned
DATABASE_URL - postgres db url if not using sqllite in non debug


REPORT_SCHEDULE_HOURS, REPORT_SCHEDULE_MINUTES and REPORT_SCHEDULE_SECONDS together controls the interval to trigger consolidated report of all issues to assignees.<br/> Reports will be triggered in such a way that interval will be sum of these 3 parmeters
eg:
REPORT_SCHEDULE_SECONDS=20
REPORT_SCHEDULE_MINUTES=30
REPORT_SCHEDULE_HOURS=12
Above case report will be triggered with and interval of 12 hours 30 minutes and 20 seconds 

5. Run  ```python manage.py migrate``` to run necessary DB migrations

6. Run  ```python manage.py createsuperuser``` for creating a user in db

7. Activate virtual env in 3 seperate tabs and run the following from project root<br/>
```python manage.py runserver``` - for running dev server for api endpoints<br/>
```celery -A issueTrackerREST beat -l info ``` - for running celery beat server for scheduling tasks<br/>
```celery -A issueTrackerREST worker -l info``` -  running celery worker for running scheduled tasks<br/>

##### Assignee will be notified via email used to signup once the issue is assigned, This delay is adjusted via ASSIGN_REPORT_SCHEDULE


##### Assignees will recieve a consolidated report of all issues assigned periodically as per the intervals set in configuration

##### User level permissions permit only the creator of an issue to Modify or delete the issue. Rest of the users will get a permission error



# Endpoints

#### Obtaining auth token

###### Use : Returns user auth token
Method : POST
Url : /api/user/get_auth_token/
Auth : None
Header : { 
    "Content-Type": "application/json"
    }
Payload : { "username": <username> , "password": <password> }
Response : {"token":"5e45c4c213ca51ff49dc929120cde0fbf1d68180"}

#### Issues CRUD endpoint

##### All issue CRUD endpoints requires Token auth. Auth token should be specified in Header


###### Use : Returns all issues
Method : GET
Url : /api/issue/
Auth : Token auth
Header : { 
        "Content-Type": "application/json", 
        "Authorization": "Token b960c34bc063d6ff7706e678531487ca0972a099" 
    }
Response : [
    {"id":13,"created_by":"nithin","title":"New issue 101","description":"Please take care of this ticket","status":"open","assigned_to":"anotheruser"},
    {"id":14,"created_by":"nithin","title":"New issue 101","description":"Please take care of this ticket","status":"open","assigned_to":"anotheruser"}
    ]

###### Use : Returns issue by id
Method : GET
Url : /api/issue/<id>/
Auth : Token auth
Header : { 
        "Content-Type": "application/json", 
        "Authorization": "Token b960c34bc063d6ff7706e678531487ca0972a099" 
    }
Response : {"id":13,"created_by":"nithin","title":"New issue 101","description":"Please take care of this ticket","status":"open","assigned_to":"anotheruser"}

###### Use : Create new issue
Method : POST
Url : /api/issue/
Auth : Token auth
Header : { 
        "Content-Type": "application/json", 
        "Authorization": "Token b960c34bc063d6ff7706e678531487ca0972a099" 
    }
Payload : { "title":"New issue 102","description":"Please take care of this ticket","status":"open","assigned_to":"anotheruser"}
Response : {"id":14,"created_by":"nithin","title":"New issue 102","description":"Please take care of this ticket","status":"open","assigned_to":"anotheruser"}

assigned_to must be a valid existing username

###### Use : Update an issue
Method : PUT
Url : /api/issue/<id>/
Auth : Token auth
Header : { 
        "Content-Type": "application/json", 
        "Authorization": "Token b960c34bc063d6ff7706e678531487ca0972a099" 
    }
Payload : { "title":"New issue 102","description":"Please take care of this ticket asap","status":"open","assigned_to":"newAssignee"}
Response : {"id":14,"created_by":"nithin","title":"New issue 102","description":"Please take care of this ticket asap","status":"open","assigned_to":"newAssignee"}

assigned_to must be a valid existing username

###### Use : Delete an issue
Method : DELETE
Url : /api/issue/<id>/
Auth : Token auth
Header : { 
        "Content-Type": "application/json", 
        "Authorization": "Token b960c34bc063d6ff7706e678531487ca0972a099" 
    }
Payload : None
Response : 2xx OK from server

# Output:

![Alt text](images/token.png?raw=true "Get Token by username password")
Get Token by username password


![Alt text](images/get.png?raw=true "Get issue by id")
Get issue by id


![Alt text](images/create.png?raw=true "Create new issue")
Create new issue


![Alt text](images/update.png?raw=true "Update issue by id")
Update issue by id


![Alt text](images/notoken.png?raw=true "Get issue without auth")
Get issue without auth


