# Use lite python image
FROM python:3.10-slim

# Set up working dir
WORKDIR /app

# Create modules
RUN mkdir -p modules

# Copy files
COPY modules/make_request.py ./modules/
COPY modules/service_parser.py ./modules/
COPY requirements.txt .
COPY mini_sherlock.py .
COPY services.json .
COPY README.md .
COPY LICENSE .

# Run pip3
RUN pip install --no-cache-dir -r requirements.txt

# Launch app
ENTRYPOINT ["python", "mini_sherlock.py"]