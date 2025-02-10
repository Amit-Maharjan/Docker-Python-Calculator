# Base image
FROM python:3.9-slim

# Working directory
WORKDIR /application

# Copy application files
COPY main.py . 
COPY history.txt . 

# Run command
CMD ["python", "main.py"]
