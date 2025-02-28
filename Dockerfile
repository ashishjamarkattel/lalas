 ## since i have mac
FROM --platform=linux/amd64 python:3.9 

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download Spacy and NLTK resources
RUN python -m spacy download en_core_web_sm
RUN python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('wordnet')"

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
