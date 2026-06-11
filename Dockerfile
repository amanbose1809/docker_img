FROM python
WORKDIR /src
COPY python.py .
RUN pip install flask
EXPOSE 5500
CMD python python.py
