### -----------------------------
### 1. Commands to Run
### -----------------------------
### 1. Build the Docker image:
###    docker build -t fastapi-docker-app .
###
### 2. Run the container:
###    docker run -d -p 8000:8000 fastapi-docker-app
###
### 3. Test it in your browser:
###    http://localhost:8000/docs (Swagger UI)


### -----------------------------
### 2. Testing CRUD via Postman
### -----------------------------

### POST - Create an Item
### URL: http://localhost:8000/items/1
### Method: POST
### Body (JSON):
### {
###   "name": "Pen",
###   "description": "Blue ink pen"
### }

### GET - Read the Item
### URL: http://localhost:8000/items/1
### Method: GET

### PUT - Update the Item
### URL: http://localhost:8000/items/1
### Method: PUT
### Body (JSON):
### {
###   "name": "Pen",
###   "description": "Updated description"
### }

### DELETE - Remove the Item
### URL: http://localhost:8000/items/1
### Method: DELETE


### -----------------------------
### 3. Testing CRUD via CURL
### -----------------------------

### CREATE
### curl -X POST "http://localhost:8000/items/1" \
###      -H "Content-Type: application/json" \
###      -d '{"name": "Pen", "description": "Blue ink pen"}'

### READ
### curl http://localhost:8000/items/1

### UPDATE
### curl -X PUT "http://localhost:8000/items/1" \
###      -H "Content-Type: application/json" \
###      -d '{"name": "Pen", "description": "Updated description"}'

### DELETE
### curl -X DELETE http://localhost:8000/items/1
