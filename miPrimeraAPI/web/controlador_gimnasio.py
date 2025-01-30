from __future__ import print_function
from bd import obtener_conexion
import sys

def insertar_gimnasio(nombre, descripcion, precio,foto):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO gimnasio(nombre, descripcion, precio,foto) VALUES (%s, %s, %s,%s)",
                       (nombre, descripcion, precio,foto))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret = {"status": "Failure" }
        code=200
        conexion.commit()
        conexion.close()
    except:
        print("Excepcion al insertar un gimnasio", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def convertir_gimnasio_a_json(gimnasio):
    d = {}
    d['id'] = gimnasio[0]
    d['nombre'] = gimnasio[1]
    d['descripcion'] = gimnasio[2]
    d['precio'] = gimnasio[3]
    d['foto'] = gimnasio[4]
    return d

def obtener_gimnasio():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, precio,foto FROM gimnasio")
            gimnasio = cursor.fetchall()
            gimnasiojson=[]
            if gimnasio:
                for gimnasio in gimnasio:
                    gimnasiojson.append(convertir_gimnasio_a_json(gimnasio))
        conexion.close()
        code=200
    except:
        print("Excepcion al obtener los gimnasio", file=sys.stdout)
        gimnasiojson=[]
        code=500
    return gimnasiojson,code

def obtener_gimnasio_por_id(id):
    gimnasiojson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            #cursor.execute("SELECT id, nombre, descripcion, precio,foto FROM gimnasio WHERE id = %s", (id,))
            cursor.execute("SELECT id, nombre, descripcion, precio,foto FROM gimnasio WHERE id =" + id)
            gimnasio = cursor.fetchone()
            if gimnasio is not None:
                gimnasiojson = convertir_gimnasio_a_json(gimnasio)
        conexion.close()
        code=200
    except:
        print("Excepcion al recuperar un gimnasio", file=sys.stdout)
        code=500
    return gimnasiojson,code


def eliminar_gimnasio(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM gimnasio WHERE id = %s", (id,))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un gimnasio", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def actualizar_gimnasio(id, nombre, descripcion, precio, foto):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE gimnasio SET nombre = %s, descripcion = %s, precio = %s, foto=%s WHERE id = %s",
                       (nombre, descripcion, precio, foto,id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un gimnasio", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code
