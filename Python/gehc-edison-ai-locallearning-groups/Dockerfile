FROM python:3.6.10-alpine3.11
WORKDIR /usr/groups
COPY ./ ./
RUN apk add build-base openldap-dev python2-dev python3-dev
RUN pip install -r requirements.txt
RUN echo "Starting groups API"
EXPOSE 5000
CMD ["python","src/groups/api.py"]