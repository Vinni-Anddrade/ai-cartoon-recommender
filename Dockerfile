# Imagem base oficial e leve do Python
FROM python:3.12-slim

# Impedir buffering no log (importante para Cloud Run)
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho dentro do container
WORKDIR /app

# Instalar dependências do sistema (somente o essencial)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar dependências primeiro (melhora cache do Docker)
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos da aplicação
COPY . .

# Expor porta padrão usada pelo Cloud Run
EXPOSE 8080

# Streamlit precisa rodar no host 0.0.0.0 e na porta definida por $PORT
CMD ["streamlit", "run", "app.py", "--server.port=$PORT", "--server.address=0.0.0.0"]
