FROM loooooopng/mineru-ubuntu20.04-cuda12.2.2-ssh:v1

WORKDIR /app

COPY ./app /app

RUN conda run -n mineru pip install fastapi uvicorn python-multipart

EXPOSE 8000

CMD ["conda", "run", "-n", "mineru", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 