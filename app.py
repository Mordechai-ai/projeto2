from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = "hkjhaskjfhakjfhk"
app.permanent_session_lifetime = timedelta (hours=2)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/response", methods=["GET", "POST"])
def response():
    if request.method == "POST":
        return render_template("response.html", nome=request.form["pessoa"])
    else:
        return redirect(url_for("home"))


@app.route("/soma", methods=["GET", "POST"])
def soma():
    if request.method == "POST":
        return render_template("soma.html", n1=int(request.form.get('n1')), n2=int(request.form.get('n2')))
    else:
        return redirect(url_for("home"))


@app.route("/formulario", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nome"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("formulario.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        return redirect(url_for("formulario"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("formulario"))

@app.route("/go2marketform")
def go2marketform():
    return render_template("go2marketform.html")

@app.route("/go2mktprocessform", methods=["GET", "POST"])
def go2mktprocessform():
    if request.method == "POST":
        nom=request.form.get("nom")
        mai = request.form.get("mai")
        msg = request.form.get("msg")
        dados=[nom,mai,msg]
        session["dados"] = dados
        return redirect(url_for("go2response"))

    else:
        return redirect(url_for("go2marketform"))


@app.route("/go2response")
def go2response():
    if "dados" in session:
        dados = session["dados"]
        return render_template("go2response.html", dados=dados)




if __name__ == "__main__":
    app.run(debug=True)
