# Import Flask
from flask import Flask, render_template
from flask_mysqldb import MySQL

# Main app
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'trixs_db'  

mysql = MySQL(app)

# Set route default
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("Select * FROM tb_produk")
    data = cur.fetchall()
    cur.close()
    return render_template("index.html", tb_produk=data)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/daftar")
def daftar():
    return render_template("daftar.html")

@app.route("/produk1")
def produk1():
    return render_template("produk1.html")

# Debung, untuk automatic update server
if __name__ == "__main__":
    app.run(debug=True)