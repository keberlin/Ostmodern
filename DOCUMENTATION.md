List of available apis:

GET /api/starships - lists all starships
GET /api/starship/?id=<id> - list starship with id <id>
POST /api/starship - create a new starship
  must have the following fields within the POST data:
    'starship_class' - text
    'manufacturer' - text
    'length' - integer
    'hyperdrive_rating' - float
    'cargo_capacity' - integer
    'crew' - integer
    'passengers' - integer
DELETE /api/starship/?id=<id> - removes the starship with id <id>
GET /api/listings - lists all listings
GET /api/listing/?id=<id> - list listing with id <id>
POST /api/listing - create a new listing
  must have the following fields within the POST data:
    'name' - text
    'starship_type' - index to available starship
    'price' - float
DELETE /api/listing/?id=<id> - removes the listing with id <id>

Notes:
- In order to allow the use of the curl commands the django.middleware.csrf.CsrfViewMiddleware middleware has been disabled.
- requirements.in has been extended to include requests
- I've added a Django command to upload the initial set of starships from the https://swapi.co/documentation#starships website.
  Run python manage.py populate_starships to create starship entries in the DB
