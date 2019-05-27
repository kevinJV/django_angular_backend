FROM python:3.7
ENV PYTHONUNBUFFERED 1
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD [ "python", "manage.py", "runserver" ,"0.0.0.0:5000"]