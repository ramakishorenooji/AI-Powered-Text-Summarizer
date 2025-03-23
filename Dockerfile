# Use official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the FastAPI port (Render will map it dynamically)
EXPOSE 8000

# Start FastAPI (Fixing CMD syntax)
CMD uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

