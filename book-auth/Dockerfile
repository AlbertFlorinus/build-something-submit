# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /book-auth
# Copy source code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 4000

# Run the service
CMD ["python", "app-auth.py"]