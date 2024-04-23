from flask import Flask,jsonify
from core import app



def test_ready_endpoint():

    client = app.test_client()

    response = client.get('/')

    assert response.status_code == 200

    data = response.get_json()
    assert 'status' in data
    assert 'time' in data

def test_error_handling_fyle_error():

    client = app.test_client()

    response = client.get('/nonexistent_route')

    assert response.status_code == 404

    data = response.get_json()
    assert data['error'] == 'NotFound'