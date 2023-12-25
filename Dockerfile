FROM python:3.10.12

# Set the working directory in the container
WORKDIR /MyApp

# Copy the local codebase to the container
COPY app ./app
COPY data ./data
COPY requirements.txt ./requirements.txt

# Install any dependencies
RUN pip install -r requirements.txt --no-cache-dir

# Define the command to run ETL script
CMD ["python", "-m", "app.main"]
