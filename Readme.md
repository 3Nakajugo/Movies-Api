# Movie API

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [Python 3.7](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


```

## Running the server

From within the `app-folder` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.


Status Codes
201 - created
200 - ok
404 - Not found
400 - Bad request

## Documentation

https://documenter.getpostman.com/view/5689782/RzthRWyK

## End points

| End points  	       |  Method | Routes                        |
|---	               |---	     |---                            |
|Create a new movie    |POST     |/api/v1/movies                 |
|Get all moives        |GET      |/api/v1/movies                 |
|Get a specific movie  |GET      |/api/v1/movies/<int:movie_id>  |
|Edit a specific movie |PATCH    |/api/v1/movies/<int:movie_id>  |
|Delete a movie	       |DELETE   |/api/v1/movies/<int:movie_id>  |

### Author
Edna Nakajugo Margaret
