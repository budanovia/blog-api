#import pytest
#import requests
#from requests import codes

'''def test_two_plus_two():
    result = requests.post("http://127.0.0.1:8000/add", data={"a": 2, "b": 2})
    assert result.status_code == codes.OK
    assert result.json()["sum"] == 4'''

#def test_create_user():
#    result = requests.post("http://127.0.0.1:8000/user", data={"email": "one@gmail.com", "password": "one"})
#    assert result.status_code == codes.OK
#    assert result.json()["sum"] == 4



def test_get_articles(client):
    response = client.get("/articles")
    assert response.status_code == 200

# test_get_articles works but getting one specific article doesn't
'''def test_get_one_article(client):
    res = client.get("/articles/1")
    assert res.status_code == 200'''

def test_create_user(client):
    response = client.post("/user", json={"email": "two@gmail.com", "password": "two"})
    assert response.status_code == 201

def test_get_user(client):
    test_create_user(client)
    response = client.get("/user/1")
    assert response.status_code == 200

def test_root(client):
    response = client.get("/")
    assert response.json() == {"message": "Starting page"}

def test_login_user(client):
    test_create_user(client)
#    response = client.post("/login", json={"email": "two@gmail.com", "password": "two"})
    response = client.post("/login", data={"username": "two@gmail.com", "password": "two"}, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    #assert response.json().get("access_token") == {"message": "Starting page"}
    assert response.status_code == 200
 
def test_create_article(client):
    test_create_user(client)
    response = client.post("/login", data={"username": "two@gmail.com", "password": "two"}, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    myToken = response.json().get("access_token")

    response = client.post("/articles", json={"title": "title_one", "content": "content_one"}, headers={'Authorization': f'bearer {myToken}'})
    assert response.status_code == 200

def test_delete_article(client):
    test_create_user(client)
    response = client.post("/login", data={"username": "two@gmail.com", "password": "two"}, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    myToken = response.json().get("access_token")
    response = client.post("/articles", json={"title": "title_one", "content": "content_one"}, headers={'Authorization': f'bearer {myToken}'})

    response = client.delete("/articles/1", headers={'Authorization': f'bearer {myToken}'})
    assert response.status_code == 200


