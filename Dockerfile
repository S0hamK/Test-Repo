# 1. Python
# 2. packages
# 3.  app.py,demo.py,requirements.txt

FROM python:3
WORKDIR /usr/scr/app
COPY requirements.txt  ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["streamlit","run", "app.py"]