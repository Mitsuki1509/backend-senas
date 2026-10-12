# 🧠 Backend - Traductor de Lenguaje de Señas YOLO

Este es el microservicio de Inteligencia Artificial para el proyecto de Traducción de Lenguaje de Señas. Está construido con **FastAPI** y utiliza un modelo de clasificación profunda **YOLOv8-Nano-Cls** preentrenado y ajustado para reconocer las letras del abecedario.

## 🚀 Tecnologías
* **Python 3.x**
* **FastAPI & Uvicorn** (Servidor de alto rendimiento)
* **Ultralytics** (Inferencia de YOLOv8)
* **Pillow** (Procesamiento de imágenes)

## ⚙️ Cómo probar el código desde cero (Guía de Instalación)

Si acabas de clonar o descargar este proyecto desde GitHub, sigue estos pasos exactos para hacerlo funcionar en tu computadora:

### Paso 1: Agregar el Modelo de IA
Por restricciones de peso, el modelo entrenado no se sube a GitHub (está en el `.gitignore`). 
* Consigue tu archivo **`modelo_vocales.pt`** (descargado de tu Google Drive o Colab).
* Pégalo directamente en la raíz de esta carpeta, justo al lado del archivo `main.py`.

### Paso 2: Crear y Activar un Entorno Virtual
Es una buena práctica usar un entorno virtual para no mezclar las librerías con las de tu computadora. Abre la terminal en esta carpeta y ejecuta:

**En Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\activate
```
*(Sabrás que funcionó porque verás la palabra `(venv)` al inicio de tu terminal).*

**En Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar las dependencias
Con el entorno virtual activado, dile a Python que instale todas las librerías necesarias ejecutando:
```bash
pip install -r requirements.txt
```

### Paso 4: Encender el servidor
Una vez que termine la instalación, levanta la API de FastAPI con este comando:
```powershell
python -m uvicorn main:app --reload
```

## 📡 Uso y Endpoints

* La API estará corriendo localmente en: `http://127.0.0.1:8000`
* **Probar sin Frontend:** Puedes probar que la IA funciona entrando a la documentación automática interactiva en **`http://127.0.0.1:8000/docs`**. Desde ahí puedes subir una imagen de prueba directamente al endpoint `/predecir`.
* **Endpoint Principal (`POST /predecir`)**: Recibe un archivo de imagen (`file`) y devuelve un JSON con la mejor coincidencia y el Top 5 de probabilidades matemáticas extraídas del tensor de YOLO.