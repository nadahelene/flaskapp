# Use base image

FROM python:3.8-alpine

# Data of the image 
LABEL version ="1.0" maintainer="HELENE NADARASSIN <helenepdy@gmail.com>"

# Install Flask needded by python app

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# copy python file

COPY ./app.py /app.py

# copy html file contained in templates to the image 
WORKDIR /templates
COPY . /templates

# run the application, command executed at the starting of the container 

ENTRYPOINT [ "python" ]
CMD ["app.py" ]

