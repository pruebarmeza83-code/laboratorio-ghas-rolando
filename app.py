import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.get("/usuarios")
def buscar_usuario():
    nombre = request.args.get("nombre", "")
    conexion = sqlite3.connect("laboratorio.db")
    consulta = "SELECT * FROM usuarios WHERE nombre = '" + nombre + "'"
    filas = conexion.execute(consulta).fetchall()
    conexion.close()
    return {"usuarios": filas}
