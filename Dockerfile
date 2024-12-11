# app/Dockerfile

FROM python:3.13-slim-bookworm AS builder
ENV PATH=/root/.local:/root/.local/bin:/install:$PATH
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install --user --upgrade -r requirements.txt
COPY app.py /app/app.py


FROM python:3.13-slim-bookworm AS app
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/app.py /app/app.py
ENV PATH=/root/.local:/root/.local/bin:$PATH
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
EXPOSE 8501 # unless default was changed
WORKDIR /app
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]