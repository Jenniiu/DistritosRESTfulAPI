#imagem base Python
FROM python:3.9-slim

#diretório
WORKDIR /app

#copiar código
COPY . .

#instalação de dependências
RUN pip install --no-cache-dir -r requirements.txt

#porta
EXPOSE 8000

#execução
CMD ["uvicorn", "project_api.main:app", "--host", "0.0.0.0", "--port", "8000"]

#docker build -t distritos-api .
#docker run -d -p 8000:8000 distritos-api