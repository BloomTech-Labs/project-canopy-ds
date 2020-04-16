FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt ./

ARG module_name="src.main"
ENV MODULE_NAME=${module_name}

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY ./app /app