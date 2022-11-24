from flask import Flask, flash, redirect, render_template, request, session, abort
 
app = Flask(__name__)

# Ruta dinámica con param "name" - sin definir tipo
@app.route("/")
@app.route("/hello")
@app.route("/hello/<name>")
def hello(name = ""):
    return f"Hola {name}!"

@app.route("/user")
@app.route("/user/<string:user>")
def user(user = ""):
    return f"Hola usuario {user}!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5011, debug = True)