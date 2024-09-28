FROM python:3.9-slim

WORKDIR /app

RUN pip install streamlit --break-system-packages

COPY src /src

CMD ["streamlit", "run", "/src/main.py"]