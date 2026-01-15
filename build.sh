#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. ติดตั้งของที่ต้องใช้ทั้งหมด (ตามรายชื่อใน requirements.txt)
pip install -r requirements.txt

# 2. รวบรวมไฟล์ CSS/รูปภาพ ไปกองรวมกันที่เดียว (เพื่อให้ WhiteNoise หาเจอ)
python manage.py collectstatic --no-input

# 3. สร้างตารางใน Database (สำคัญมาก! ถ้าไม่ทำ เว็บจะ Error หาตารางไม่เจอ)
python manage.py migrate    