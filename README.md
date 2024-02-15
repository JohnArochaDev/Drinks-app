# Drinks-App

Overview
- The drinks app is being created for drink makers and drinkers alike. It's made to educate and ensure that all parties, events and even casual drinks are enjoyed to the fullest. Displaying ingredients, instructions, and being able to save personal favorites is a tool that everyone would find helpful. Now this is meant to be tool and not be abused so please use this tool and drink Responsibly....but Drink !


User Stories
  - As a user, I want the ability to sign up.
  - As a user, I want the ability to sign in. 
  - As a user, I want the ability to sign out.
  - As a user, I want the ability to favorite recipes, and add them to a list.
  - As a user, I want the ability to view all of my recipes in a list. 
  - As a user, I want the ability to read more details of individual recipes. 
  - As a user, I want the ability to delete the recipes in my list. 
  - As a user, I want the ability to delete list 
  - As a user, I want the ability to view the ingredients of the recipes
  - As a user, I want the ability to read all of the recipes I have favorited. 
  - As a user, I want the ability to view different versions of my selected recipes
    
a detailed list of the functionality of your application, told through a user's perspective
Wireframes / Screenshots

## Screenshots
![image](main_app/static/images/home.png)
![image](main_app/static/images/detail.png)
![image](main_app/static/images/home.png)
## Entity Relationship Diagrams
![image](main_app/static/images/ERD.png)

asgiref==3.7.2
boto3==1.34.25
botocore==1.34.25
certifi==2023.11.17
charset-normalizer==3.3.2
distlib==0.3.8
dj-database-url==2.1.0
Django==5.0.1
django-environ==0.11.2
filelock==3.13.1
gunicorn==21.2.0
idna==3.6
jmespath==1.0.1
packaging==23.2
platformdirs==4.1.0
psycopg2==2.9.9
psycopg2-binary==2.9.9
python-dateutil==2.8.2
requests==2.31.0
s3transfer==0.10.0
six==1.16.0
sqlparse==0.4.4
typing_extensions==4.9.0
urllib3==2.0.7
virtualenv==20.25.0
whitenoise==6.6.0



pip install -r requirements.txt
pip install django
python manage.py collectstatic --no-input
python manage.py migrate