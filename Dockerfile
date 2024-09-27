FROM python:3.10

# Update package lists and install necessary tools
RUN apt update && \
    apt install -y ffmpeg

WORKDIR /app

RUN pip install streamlit --break-system-packages

COPY src /src

CMD ["streamlit", "run", "/src/main.py"]