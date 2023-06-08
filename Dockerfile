FROM python:3.11.2

WORKDIR /usr/src/api

COPY pyproject.toml ./

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-root

COPY . .

EXPOSE 8000
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]