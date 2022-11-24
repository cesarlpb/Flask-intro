from flask import Flask, render_template, request
 
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

@app.route("/products")
@app.route("/products/<string:_category>")
@app.route("/products/<string:_category>/<int:_id>")
def products(_category = "", _id = 1):
    return render_template("routes.html", category=_category, id=_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5011, debug = True)