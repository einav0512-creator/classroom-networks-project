import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # קריאת קובץ ה-JSON
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # בניית טבלת HTML מתוך הנתונים
        html = """
        <html>
        <head><title>Classroom Networks Project</title></head>
        <body>
            <h1>רשימת פרויקטים וסטודנטים</h1>
            <table border="1" cellpadding="5" cellspacing="0" dir="rtl">
                <tr>
                    <th>מזהה (ID)</th>
                    <th>שם הסטודנט</th>
                    <th>כיתה</th>
                    <th>שם הפרויקט</th>
                </tr>
        """
        
        for student in data.get('students', []):
            html += f"""
                <tr>
                    <td>{student.get('id')}</td>
                    <td>{student.get('name')}</td>
                    <td>{student.get('class')}</td>
                    <td>{student.get('project')}</td>
                </tr>
            """
            
        html += """
            </table>
        </body>
        </html>
        """
        return html
    except Exception as e:
        return f"שגיאה בטעינת הנתונים: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)