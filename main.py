# main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from urllib.parse import unquote
import uvicorn

app = FastAPI(
    title="Recruto Greeting Service",
    description="Сервис для приветствия Recruto",
    version="1.0.0"
)

@app.get("/", response_class=HTMLResponse)
async def greet_user(name: str = "Recruto", message: str = "Давай дружить"):
    # FastAPI автоматически декодирует %20 в пробелы!
    greeting = f"Hello {name}! {message}!"
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Recruto Greeting</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                background: #f0f2f5;
            }}
            .greeting {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                text-align: center;
            }}
            .url-example {{
                background: #e9ecef;
                padding: 10px;
                border-radius: 5px;
                font-family: monospace;
                margin: 10px 0;
            }}
        </style>
    </head>
    <body>
        <div class="greeting">
            <h1>{greeting}</h1>
            <p><strong>Полученные параметры:</strong></p>
            <p>name: {name}</p>
            <p>message: {message}</p>
            
            <div style="margin-top: 30px; text-align: left;">
                <h3>Правильные форматы ссылок:</h3>
                
                <div class="url-example">
                    /?name=Recruto&message=Давай%20дружить
                </div>
                
                <div class="url-example">
                    /?name=Recruto&message=Давай+дружить
                </div>
                
                <p>Или используйте форму ниже:</p>
                <form method="get">
                    <input type="text" name="name" value="{name}" placeholder="Имя">
                    <input type="text" name="message" value="{message}" placeholder="Сообщение" style="width: 200px;">
                    <button type="submit">Отправить</button>
                </form>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/api/greet")
async def greet_api(name: str = "Recruto", message: str = "Давай дружить"):
    """
    API endpoint возвращающий JSON
    """
    return {
        "greeting": f"Hello {name}! {message}!",
        "parameters": {
            "name": name,
            "message": message
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "Recruto Greeting Service"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",  # Доступ снаружи
        port=8000,
        reload=True  # Автоперезагрузка при изменениях

    )
