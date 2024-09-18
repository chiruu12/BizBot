FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV PINECONE_API_KEY="your-pinecone-api-key"
ENV COHERE_API_KEY="your-cohere-api-key"
ENV PINECONE_INDEX_NAME="your-pinecone-index-name"
ENV FOLDER_PATH = "your-folder-path"

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "ui.py"]