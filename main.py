from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
from PIL import Image
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = YOLO("modelo_vocales.pt")

@app.post("/predecir")
async def predecir_sena(file: UploadFile = File(...)):
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data)).convert("RGB")
    resultados = model(image)

    nombres = resultados[0].names

    top5_indices = resultados[0].probs.top5
    top5_confianzas = resultados[0].probs.top5conf.tolist()

    top5 = []
    for i, conf in zip(top5_indices, top5_confianzas):
        top5.append({
            "letra": nombres[i],
            "confianza": round(conf * 100, 2)
        })

    return {
        "mejor_letra": top5[0]["letra"],
        "mejor_confianza": top5[0]["confianza"],
        "top5": top5
    }