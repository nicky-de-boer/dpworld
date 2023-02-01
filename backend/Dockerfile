FROM python:3.7
WORKDIR /backend
COPY src .
RUN pip install -r requirements
EXPOSE 8020
COPY src .
CMD ["gunicorn", "wsgi:app", "-w 2", "-b 0.0.0.0:8020", "-t 30"]