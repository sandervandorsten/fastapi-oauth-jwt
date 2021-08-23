# FastAPI application with Oauth2 login using JWT

Example application containing an [Oauth2](https://oauth.net/2/) login flow using [JWT](https://jwt.io). 
The application was built for educational purposes to test and demonstrate the use of Oauth2 and JWT in a python based backend application. 

It uses some security measures which have not been tested extensively, hence this project **should not be considered for production**.

## Inspiration
- The example application is based upon the official [FastAPI security tutorial](https://fastapi.tiangolo.com/tutorial/security/). 
- The folder structure is based upon [Tiangolo's full-stack-fastapi-postgresql](https://github.com/tiangolo/full-stack-fastapi-postgresql) FastAPI deployment. 

## Installation using docker-compose
```zsh
docker-compose up -d --build
```
This opens up an API on localhost on port `8083`. 
- base url: [http://localhost:8083/](http://localhost:8083/)
- docs url: [http://localhost:8083/docs](http://localhost:8083/docs)