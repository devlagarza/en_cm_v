# Investigacion Operativa

**Integrantes del grupo:**

✔️ *Alejo Torres*

✔️ *Gonzalo Guaimas*

✔️ *Santiago San Miguel*

## Modelo de Transporte

En este repositorio se incluyen los codigos fuentes de cada uno de los 3 metodos de resolucion del modelo de transporte, basados en los datos del problema de los silos y molinos en el libro de THAJA 7ma edicion

### Metodo de la Esquina Noreste

<img width="397" alt="image" src="https://user-images.githubusercontent.com/80418452/173443365-106d768e-54bc-4c21-b4eb-ce394a5eb3ff.png">


### Medoto del Costo mínimo 

<img width="393" alt="image" src="https://user-images.githubusercontent.com/80418452/173443408-45a18c58-a264-4671-927e-f6475765a387.png">


### Metodo de Voguel

<img width="418" alt="image" src="https://user-images.githubusercontent.com/80418452/173443325-7bc8869b-c918-4891-bdc3-8edf03347603.png">


## Como ejecutar el codigo

1. Clonar el repositorio en la rama indicada

```bash
git clone -b AlejoTorres2001/path --single-branch https://github.com/AlejoTorres2001/invop_transporte.git

```
3. Crear un entorno virtual de python (recomiendo pipenv)

```bash
pipenv shell

```
tambien es posible utilizar virtualenv o anaconda

5. instalar pandas

```bash
pipenv install pandas 

or

pip install pandas

or 

conda install pandas

```

6. ejecutar un script

```bash
python3 ./src/{{file-name}}.py

```
![image](https://user-images.githubusercontent.com/80418452/173444148-7080d8ee-b2f5-4ffd-97dd-8d39368b55f0.png)
