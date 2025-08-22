# Usa uma imagem base leve com Python
FROM python:3.10-slim

# Evita interações durante instalação
ENV DEBIAN_FRONTEND=noninteractive

# Instala dependências do sistema (necessárias para torch, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências e instala
COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# Expõe a porta da API
EXPOSE 8000

# Comando para rodar a aplicação (ajuste se o seu arquivo não for app.py)
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]


