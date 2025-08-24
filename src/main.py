from http import HTTPStatus

from flask import Flask, render_template, request, redirect, flash
from requests import post

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z'

API_URL = "http://localhost:8000/"


@app.route("/", methods=["GET", "POST"])
def root():
    if request.method == "GET":
        return render_template("sign.html")
    if "sign-in" in request.form:
        return "Logou"
    data = {
        "username": request.form.get("username"),
        "password": request.form.get("password"),
        "first_name": request.form.get("first_name"),
        "last_name": request.form.get("last_name"),
        "email": request.form.get("email"),
        "phone": request.form.get("phone"),
        "role": "client",
    }
    response = post(f"{API_URL}users", json=data)
    if response.status_code == HTTPStatus.CREATED:
        user = response.json()
        return redirect(f'/home/{user['username']}')
    flash(response.json()['detail'])
    return redirect('/')


@app.route('/home/<username>')
def home(username: str):
    return username

