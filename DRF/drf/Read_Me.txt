//////////// Package Install //////////////////////

//django installation

pip install django

pip install djangorestframework

// To check version

django-admin --version


////////////// Django REST framework installation ////////////////

pip install djangorestframework

pip install markdown       # Markdown support for the browsable API.

pip install django-filter  # Filtering support


//////////////// MY SQL//////////////////

pip install mysql-connector-python



///////////////////////// Commands /////////////////////////////////


// After installing the necessary requirements let’s create a Django project and app
   
    django-admin startproject drf
    cd drf
    django-admin startapp signup
    ls
    python manage.py runserver

// Command for Existing Database to import in new created models.py 

    python manage.py inspectdb > models.pyc

// The first step is to create a new migration by running the makemigrations command.
    
    python manage.py makemigrations 
    python manage.py migrate

// create admin page and test it
    python manage.py createsuperuser
    python manage.py runserver      




////////////////// API URLS /////////////////

127.0.0.1:8000/star-wars/dep/  # get link (GET /star-wars/dep/)
127.0.0.1:8000/star-wars/org/  # get link (GET /star-wars/org/)
127.0.0.1:8000/star-wars/mod/  # get link (GET /star-wars/mod/)
127.0.0.1:8000/star-wars/user/ # get link (GET /star-wars/user/)



