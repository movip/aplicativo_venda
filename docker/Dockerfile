FROM python:3.9-slim
WORKDIR /app
COPY app /app/
# Copiar o arquivo requirements.txt para o container
COPY docker/requirements.txt ./docker/
# Instalar as dependências do requirements.txt
RUN pip install --no-cache-dir -r ./docker/requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "index.py"]