import io
from PIL import Image
import torch
from fastapi import UploadFile
from model.model_loader import load_model
from model.preprocess import transform

model, device = load_model()
class_names = ['cat', 'dog']  # Ajuste para duas classes

async def predict_image(file: UploadFile):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    image_tensor = transform(image).unsqueeze(0).to(device)
    
    with torch.no_grad():
        output = model(image_tensor)
        probabilities = torch.softmax(output, dim=1)
        predicted_class_idx = torch.argmax(probabilities, 1).item()
    
    return {
        "prediction_index": predicted_class_idx,
        "class_name": class_names[predicted_class_idx],
        "probabilities": probabilities.cpu().numpy().tolist()
    }


