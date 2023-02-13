from flask import request

from server import app
from server.service import wine_service


@app.post("/wine")
def create_wine():
    wine = request.get_json()
    error = wine_service.create_wine(wine)
    if error is not None:
        return error, 400
    return wine, 201


@app.get("/wine")
def get_wine():
    wine = wine_service.show_wine()
    return wine
