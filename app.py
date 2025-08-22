from fastapi import FastAPI, File, UploadFile
import uvicorn 
from predict import predict_image

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    return await predict_image(file)

if __name__ == "__main__":
    # Inicia o servidor Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)