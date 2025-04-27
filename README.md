# Flask Microservice Demo

## ¿Que cambios se ralizaron?


Cambiamos el yml con el uso de una variable común para no repetir la declaración de que permite debuggear el entorno del servicio, y se elimino el contenedor aggregate y se utilizo su lógica dentro del contenedor de Backend


## ¿Por qué se realizaron lo cambios?


Se realizaron los cambios debido a que la función 'detail' se puede utilizar dentro de la lógica de 'Backend', esto reduciendo el tiempo de ejecución, de recursos y de complejidad

## Running it

You need docker and docker-compose. Follow your OS instructions for doing that.  The docker images start with Alpine and install Python3. The only dependencies in Python are Flask, Faker, and requests.

## Testing it

With the docker-compose running and postman, try the following URLS:

### A bunch of raw orders:

http://localhost:5000/orders?count=10

```json
[
    {
        "cust": "Mr. James Edwards",
        "id": 1,
        "items": [
            88,
            2,
            38,
            59,
            52,
            95,
            32,
            68,
            17
        ]
    },
    {
        "cust": "Sarah Taylor",
        "id": 2,
        ...and so on...
    }
    ...and so on...
]
```

### An order detail

http://localhost:5000/detail/5

Notice how the "items" element has been replaced with a list of item details.

```json
{
    "cust": "John Martinez",
    "id": 6,
    "items": [
        {
            "desc": "synthesize plug-and-play interfaces",
            "id": 72
        },
        {
            "desc": "target open-source action-items",
            "id": 18
        },
        {
            "desc": "grow dynamic web services",
            "id": 86
        },
        {
            "desc": "synthesize plug-and-play interfaces",
            "id": 72
        },
        {
            "desc": "streamline synergistic e-commerce",
            "id": 37
        }
    ]
}
```

### Customer name search

http://localhost:5000/custSearch/Dan

You can now hit this URL directly with a GET to perform a search by partial customer name. A space is just '%20'. This calls the underlying custSearch endpoint for the orders microservice, but takes the name and forms a JSON payload which is possibly a more familiar way to send data to a microservice for it to operate on rather than doing it through parameters.  Again Flask makes this absurdly simple.


### Test the search in the data microservice

POST http://localhost:5001/custSearch

*Note the port of the orders microservice here! This isn't the backend!*

Make sure to use a POST and to set "Content-Type: application/json" in the "headers" and to put something like `{"name": "Daniel"}` in the "body".  You'll get a list of order where the "cust" field contains the search parameter. The customer names are randomly generated, so you might want to try something simple.
