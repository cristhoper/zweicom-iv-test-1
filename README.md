# Desarrollo 1
En el siguiente repositorio, se encuentra la solucion al siguiente requerimiento

_En el lenguaje que prefiera escriba un servicio http que_:
* _Acepte un número como consulta._
* _Dado el número recibido, retorne el n-ésimo término de la sucesión de Fibonacci._

## Instalacion
La solución fue implementada en Python3.8 usando `virtualenv` en Linux.
Por esto, se deben instalar lo siguiente:
```shell script
$ sudo apt install python-virtualenv virtualenv
$ virtualenv venv --python=python3
$ . venv/bin/activate
(venv) $
```

Luego, para levantar el servicio:
```shell script
(venv) $ python app.py
```
Y para ejecutar los test unitarios:
```shell script
(venv) $ python test_app.py
```

## API
Esta api se accede a través de `http://localhost:8080`

|   |   |   |
|---|---|---|
| GET | `/fibonacci/{posicion}` | Retorna elemento de serie fibonacci  |
|   | `posicion`: tipo entero o string numerico    |


