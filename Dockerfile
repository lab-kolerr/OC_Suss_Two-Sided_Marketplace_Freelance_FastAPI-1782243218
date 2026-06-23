FROM python:3.10-slim AS base
WORKDIR /app

FROM base AS builder
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM base
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]