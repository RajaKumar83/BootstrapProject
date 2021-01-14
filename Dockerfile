FROM python:alpine
WORKDIR /usr/app
COPY ./ ./
RUN pip install -r requirements.txt 
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]