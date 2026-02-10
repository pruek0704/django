FROM python:3.14-slim
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# ก๊อปปี้ไฟล์ requirements ไปวางในเครื่อง container แล้วสั่งติดตั้ง
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY src /src
WORKDIR /src
CMD ["gunicorn", "--bind", ":8888", "superlists.wsgi:application"]