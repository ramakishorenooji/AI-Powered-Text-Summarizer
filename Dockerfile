# Use official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose required ports
EXPOSE 8000 8501

# Start both FastAPI and Streamlit using a process manager
CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port 8000 & streamlit run src/app.py --server.port=8501 --server.address=0.0.0.0"]
