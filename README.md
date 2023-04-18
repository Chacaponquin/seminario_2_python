<p align="center"><img align="center" src="https://res.cloudinary.com/chaca-sa/image/upload/v1679027493/328169508_122397193933692_2960493904923070018_n_vxtlez.jpg" style="width: 300px"/></p>

# Proyecto "Gato Matias"

## 😀 Objetivos del trabajo
- Lograr que **Amaya** no deje espacios en blanco innecesarios
- Conseguir que **Hector** y **José** no cometan faltas de ortografía en los comentarios
- Aprobar RA **(opcional)**


> ### 😹 Chistecillo
> Qué es un chino con capucha? Un capuchino

## 🕛 Antes de empezar
- Abrir la consola Anaconda **(poner Anaconda Prompt en el buscador de Windows)**
- Crear un entorno virtual **en caso de no haber creado uno**
 
  ```bash
  conda create -n <nombre_entorno>
  ```

- Activar con **conda** el entorno virtual en caso de tenerlo
  
  ```bash
  conda activate <nombre_entorno>
  ```

- Instalar las librerías (`rich`)

  ```bash
  pip install -r requirements.txt
  ```


> ### 😹 Chistecillo
> Qué hace una vaca en la carretera? Vacaminando

## ⚠️Advertencias de la estructura
- Si se quiere mostrar por consola algún error se creó una función `show_error` que se puede importar así:

  ```python
  from src.utils import show_error
  ```
- Lo mismo ocurre si se quiere mostrar por consola algún mensaje con alguna respuesta con la función `show_success` que se puede importar así:

  ```python
  from src.utils import show_success
  ```

> ### 😹 Chistecillo
> Qué es un café recién salido de la cárcel? Un expreso

## 🤖 Minitutorial de Git (parte 2)

Debido a la vagancia extrema que hay en este equipo se vuelve a trabajar todo el mundo en la misma rama

- Paso -1 (Solo hay que hacerlo una vez): clonar el repositorio. Se abre la consola en la carpeta donde se quiera clonar y se escribe
  
  ```bash
  git clone <url_repositorio>
  ```

- Paso 0:
  Actualizar el código. Como estamos trabajando en la misma rama si quieren se puede actualizar el código por si otra persona puso algo nuevo se vea en el códgo que tienes en tu PC

  ```bash
  git pull
  ```

- Paso 1:
  Añadir todos los cambios en los códigos existentes y archivos nuevos

  ```bash
  git add .
  ```

- Paso 2:
  Crear el commit. Que es como un punto de control del código nuevo. **Opcionalmente puede tener un mensage**

  ```bash
  git commit -m "Quiero aprobar RA"
  ```

- Paso 3:
  Pushear los cambios para que se suban a Github

  ```bash
  git push
  ```
  
> ### 😹 Chistecillo
> Un día quise ligarme a una programadora. Pero no se de java 

## 💻 Tareas

Tareas de este biutiful team

### 🧑‍🚀 Tareas de José **(En la clase Point)** 
- ⭕ Añade un método constructor para crear puntos fácilmente. Si no se recibe una coordenada, su valor será cero.
- ⭕ Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y).
- ⭕ Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
- ⭕ Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
- ⭕ Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla **(Con la fórmula que se encuentra en eñ PDF)**.

### 🐈 Tareas de Amaya **(En la clase Rectangle)**
- ⭕ Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
- ⭕ Añade al rectángulo un método llamado base que muestre la base.
- ⭕ Añade al rectángulo un método llamado altura que muestre la altura.
- ⭕ Añade al rectángulo un método llamado área que muestre el área.

### 🦍 Tareas de Héctor
- ⭕ Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
- ⭕Consulta a que cuadrante pertenecen el punto A, C y D.
- ⭕ Consulta los vectores AB y BA.
- ⭕ Consulta la distancia entre los puntos 'A y B' y 'B y A'.
- ⭕ Determina cuál de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
- ⭕ Crea un rectángulo utilizando los puntos A y B.

> ### 😹 Chistecillo
> Van dos ciegos por la calle. Uno mira al cielo y dice "Ojalá lloviera" y el otro dice "Ojalá yo también"

## 🧪 Test
Para el proyecto del Gato Matias vamos a poner testing a los métodos para que se pueda comprobar los resultados de los métodos sin tener que estar arrancando la aplicación una y otra vez.
En Python hay varias opciones, pero es más fácil utilizar `unittest` que es un módulo que viene incluido en Python y no hay que descargarlo
Cuando aprendimos hacer test en **Java** era una tortura pero aquí es mucho más fácil a mi parecer. Aquí hay un ejemplo:

> ### ⚠️ Advertencia
> Poner `test` delante del nombre de cada método para que se detecte (no sean como yo que estuve 1 hora sin saber por qué no salía)

```python
import unittest


# se declara la clase y se dice que herede de `unittest.TestCase` para indicar que es un caso de test
class TestSum(unittest.TestCase):
    # cada método de test debe estar con la palabra test delante para que sea detectado
    def test_sum(self):
      realValue = sum([1, 2, 3])
      expectedValue = 6
      
      # Se espera que la suma del array de como resultado 6
      self.assertEqual(realValue, expectedValue, "Should be 6")

    # se pueden declarar tantos test cases como se quiera
    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

# indica que cuando se llame a este archivo especificamente se ejecutaran todos los tests
if __name__ == '__main__':
    unittest.main()
```

### Llamar al test
Hay que ir a la terminal y poner:
```bash
python test/<nombre_archivo>.py
```
En nuestro caso por ejemplo, para ejecutar los tests de la clase `Point`:
```bash
python test/PointTest.py
```
**Pycharm puede ejecutarlo de distintas formas hasta con distintas interfaces pero ya hay que buscar como se hace especificamente**

### Links para ver más cosas de `unitest`
- [https://www.digitalocean.com/community/tutorials/python-unittest-unit-test-example](https://www.digitalocean.com/community/tutorials/python-unittest-unit-test-example)
- [https://realpython.com/python-testing/](https://realpython.com/python-testing/)
- [https://www.freecodecamp.org/news/how-to-write-unit-tests-for-python-functions/](https://www.freecodecamp.org/news/how-to-write-unit-tests-for-python-functions/)