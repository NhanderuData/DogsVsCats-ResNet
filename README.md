# API_ResNet – API de Classificação de Imagens 

API RESTful para classificação de imagens usando um modelo ResNet treinado. Desenvolvida em Python com FastAPI, permite enviar imagens e receber previsões do modelo. 
Tecnologias Utilizadas 

* Python 3.10+ 
* PyTorch 
* FastAPI 
* Uvicorn 
* Pillow (para processamento de imagens)

## Estrutura do Projeto 

├── app.py                
├── Dockerfile  
├── requirements.txt  
├── model/       
│   ├── model_loader.py           
│   ├── modelo_resnetv4.pth                 
│   ├── preprocess.py           
│   └── predict.py         
└── __pycache__/     
 
## Exemplo de Requisição   

curl -X POST "http://127.0.0.1:8000/predict" \ 
  -F "file=@caminho/para/sua_imagem.jpg" 

## Exemplo de Resposta JSON

{ 
  "prediction_index": 1,  
  "class_name": "dog",  
  "probabilities": [  
    [  
      0.00029792750137858093,  
      0.9997020363807678  
    ]  
  ]  
}  

### Notas 

Notas

* O modelo ResNet utilizado está salvo em model/modelo_resnetv4.pth. 
* As imagens enviadas são pré-processadas em model/preprocess.py. 
* A lógica de inferência está em model/predict.py. 
