# Use a lightweight Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files into the container
COPY . /app/

# Expose Flask's default port
EXPOSE 5000

# Set the command to run the Flask app (change to your entry point file)
CMD ["python", "app.py"]