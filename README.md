# Mozio-Django-RESTAPI

*BACKEND/PYTHON CODING PROJECT:*

*Mozio Backend*

 - Build a JSON REST API with CRUD operations for Provider (name, email, phone number, language and currency) and ServiceArea (name, price, geojson information)
Create a specific endpoint that takes a lat/lng pair as arguments and return a list of all polygons that include the given lat/lng. The name of the polygon, provider's name, and price  - should be returned for each polygon. This operation should be FAST.
 - Use unit tests to test your API;
 - Write up some API docs (using any tool you see fit);
 - Create a Github account (if you don’t have one), push all your code and share the link with us;
 - Deploy your code to a hosting service of your choice. Mozio is built entirely on AWS, so bonus points will be awarded for use of AWS.
*Prompt:*

As Mozio expands internationally, we have a growing problem that many transportation suppliers we'd like to integrate cannot give us concrete zip codes, cities, etc that they serve.

To combat this, we'd like to be able to define custom polygons as their "service area" and we'd like for the owners of these shuttle companies to be able to define and alter their polygons whenever they want, eliminating the need for mozio employees to do this boring grunt work.

## Versions
 - Python 3.10
 - Django 4.0
 - Postgres 14.1
 - Postgis 3

## Running the Project
In development environmet, it's recommended use docker-compose:

```
docker-compose -f docker-compose.dev.yml up --build -d
```
or using local server:

```
python manage.py runserver
```

## CRUD Provider

Send a REQUEST to /api/provider/

For creation or update, use the data format:
 ```
 {
  "name": "test user",
  "email": "test@testuser.com",
  "phone": "+55989899",
  "language": "pt-br",
  "currency": "usd"
}
 ```

## CRUD Service Area

Send a REQUEST to /api/service_area/

For creation or update, use the data format:
```
{
        "name": "test",
        "price": 25.0,
        "area": "SRID=4326;POLYGON ((10 20, 20 20, 20 10, 10 10, 10 20))",
        "provider": 1
    }
```
There is a filter in GET list request, that can be used with a query parameter called 'coordinates'.
Example use:
```
request GET /api/service_area/?coordinates=21.1,21.1 

```

See an example [demo here](https://mozio-test-api.herokuapp.com/)

See an [Swagger documentation here](https://mozio-test-api.herokuapp.com/swagger/)
