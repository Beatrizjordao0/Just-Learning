import os

import mysql.connector
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "apenas-desenvolvimento")


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "igreja"),
    )


@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"].strip().lower()
    password = request.form["password"]

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT email, senha FROM obreiros WHERE email = %s",
            (email,),
        )
        user = cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

    if user and check_password_hash(user["senha"], password):
        session["user_email"] = user["email"]
        return redirect(url_for("schedule_page"))

    return render_template("login.html", error="E-mail ou senha inválidos."), 401


@app.route("/register", methods=["GET", "POST"])
def register_page():
    if request.method == "GET":
        return render_template("cadastro.html")

    email = request.form["email"].strip().lower()
    password_hash = generate_password_hash(request.form["password"])
    name = request.form["name"].strip()
    department = request.form["department"].strip()

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO obreiros (email, senha, nome, departamentos)
            VALUES (%s, %s, %s, %s)
            """,
            (email, password_hash, name, department),
        )
        conn.commit()
    finally:
        cursor.close()
        conn.close()

    session["user_email"] = email
    return redirect(url_for("department_page"))


@app.route("/department", methods=["GET", "POST"])
def department_page():
    email = session.get("user_email")
    if not email:
        return redirect(url_for("login_page"))

    if request.method == "POST":
        days_off = request.form["days_off"].strip()
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE obreiros SET dias_nao_pode = %s WHERE email = %s",
                (days_off, email),
            )
            conn.commit()
        finally:
            cursor.close()
            conn.close()
        return redirect(url_for("schedule_page"))

    return render_template("department.html", email=email)


@app.route("/schedule")
def schedule_page():
    email = session.get("user_email")
    if not email:
        return redirect(url_for("login_page"))
    return render_template("schedule.html", email=email)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login_page"))


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG") == "1")
