#I Hate Ironing Tech Test
##Setup

To build the django application (incl. migrations and fixture loading), run the following:

```make setup```

##Execution

To run the web application using the Django dev server, run the folowing:

```make run```

Go to the folowing url:

```http://127.0.0.1:8000/order```

Search for order id **34992**

##Tests
To run the test suite, run the following:

```make test```

To run the flake8 linter, run the following:

```make lint```