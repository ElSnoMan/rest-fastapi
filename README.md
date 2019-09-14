# rest-fastapi
Python REST APIs with FastAPI

## Get Started

1. Run the API server

    ```bash
    $ uvicorn main:app --reload
    ```

2. Hit the API by going to

    * http://localhost:8000/items/5?q=somequery
   
3. View the docs

    * http://localhost:8000/docs
    
    or
    
    * http://localhost:8000/redoc

## What does it use?

* FastAPI
* Uvicorn - webserver
* Pydantic - type checking, schema and model definition, etc.
