FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt requirements.txt

# Specify app module
ARG module_name="src.main"
ENV MODULE_NAME=${module_name}

# Install project requirements
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# optional argument --no-cache-dir

COPY ./app /app