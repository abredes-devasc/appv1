FROM python
ADD requirements.txt /
ADD app.py /
RUN pip install -r requirements.txt
EXPOSE 5050
CMD python3 app.py
