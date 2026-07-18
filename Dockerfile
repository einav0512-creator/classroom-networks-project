# הגדרת בסיס ל-Python
FROM python:3.9-slim

# הגדרת תיקיית עבודה
WORKDIR /app

# העתקת קבצי הדרישות והתקנתם
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# העתקת כל קבצי הקוד
COPY . .

# הרצת האפליקציה
CMD ["python", "app.py"]