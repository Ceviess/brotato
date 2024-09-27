FROM python:3.10

WORKDIR /app

RUN pip install streamlit --break-system-packages

COPY src /src

# CMD ["streamlit", "run", "/src/main.py"]
CMD ["python", '/src/endless.py']