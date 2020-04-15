FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
ARG module_name="src.main"
ENV MODULE_NAME=${module_name}
COPY ./app /app