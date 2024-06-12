# LibraryApp

## Required software

* Docker/Docker Desktop
* Postman (optional, for testing endpoints)

## Local setup

### Navigate to directory where project is cloned and run following command
```docker-compose -f LibraryApp/docker-compose.yml -p libraryapp up -d --wait```
#### After initial build of containers, to start again all containers, in case of failure in initial run, you can execute following commands
```docker-compose down```
```docker-compose -f LibraryApp/docker-compose.yml -p libraryapp up -d```


## API endpoints guide

- **GET `/authors`**: Retrieve a list of all authors.
  - Parameters: None

- **GET `/authors/{id}`**: Retrieve author with provided ID.
  - Parameters:
    - `id`: Author's ID

- **GET `/authors/top`**: Retrieve a list of authors with the most written books, limited to 5.
  - Parameters: None

- **POST `/authors`**: Create author.
  - Parameters:
    - `name`: Author's name
    - `birth_date`: Author's birthdate (in format yyyy-mm-dd)

- **PUT `/authors/{id}`**: Update author with provided ID.
  - Parameters:
    - `name`: Author's name
    - `birth_date`: Author's birthdate (in format yyyy-mm-dd)

- **DELETE `/authors/{id}`**: Delete author with provided ID.
  - Parameters:
    - `id`: Author's ID

- **GET `/books`**: Retrieve a list of all books.
  - Parameters: None

- **GET `/books/{id}`**: Retrieve book with provided ID.
  - Parameters:
    - `id`: Book's ID

- **GET `/books/recent`**: Retrieve a list of books written within last year.
  - Parameters: None

- **GET `/books/search`**: Retrieve a list of books whose title or description contains provided string. 
  - Parameters:
    - `query`: String

- **GET `/authors/{id}/books`**: Retrieve a list of books that were written by the author with provided ID. 
  - Parameters:
    - `id`: Author's ID

- **POST `/books`**: Create book.
  - Parameters:
    - `title`: Author's title
    - `description`: Book's description
    - `published_date`: Book's publication date (in format yyyy-mm-dd)
    - `author`: Book's author's ID

- **PUT `/books/{id}`**: Update book with provided ID.
  - Parameters:
    - `title`: Book's title
    - `description`: Book's description
    - `published_date`: Book's publication date (in format yyyy-mm-dd)
    - `author`: Book's author's ID

- **DELETE `/books/{id}`**: Delete book with provided ID.
  - Parameters:
    - `id`: Book's ID
