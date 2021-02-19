FROM python:3-alpine
RUN mkdir /app
WORKDIR /app
RUN pip install flask
COPY main.py /app

EXPOSE 5000
CMD ["python", "main.py"]
