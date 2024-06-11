# LibraryApp

## Required software

* Docker/Docker Desktop
* Postman (optional, for testing endpoints)

## Local setup

### Navigate to directory where project is cloned and run following command
```docker-compose -f LibraryApp/docker-compose.yml -p libraryapp up -d```

### Create Superuser and fill required data
```python manage.py createsuperuser```
