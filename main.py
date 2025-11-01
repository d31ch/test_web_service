# main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(
    title="Recruto Greeting Service",
    description="Сервис для приветствия Recruto",
    version="1.0.0"
)

@app.get("/", response_class=HTMLResponse)
async def greet_user(name: str = "Recruto", message: str = "Давай дружить"):
    """
    Приветствует пользователя с переданными параметрами
    
    Args:
        name: Имя для приветствия (по умолчанию "Recruto")
        message: Сообщение (по умолчанию "Давай дружить")
    """
    greeting = f"Hello {name}! {message}!"
    
    # Возвращаем красивый HTML ответ
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Recruto Greeting</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            .greeting-card {{
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                text-align: center;
            }}
            h1 {{
                color: #333;
                font-size: 2.5em;
                margin-bottom: 20px;
            }}
            .highlight {{
                color: #667eea;
                font-weight: bold;
            }}
            .parameters {{
                margin-top: 30px;
                padding: 20px;
                background: #f8f9fa;
                border-radius: 10px;
                text-align: left;
            }}
            .url-example {{
                background: #e9ecef;
                padding: 10px;
                border-radius: 5px;
                font-family: monospace;
                margin-top: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="greeting-card">
            <h1>Hello <span class="highlight">{name}</span>! <span class="highlight">{message}</span>!</h1>
            
            <div class="parameters">
                <h3>Параметры запроса:</h3>
                <p><strong>name:</strong> {name}</p>
                <p><strong>message:</strong> {message}</p>
                
                <h3>Примеры использования:</h3>
                <div class="url-example">
                    /?name=Recruto&message=Давай дружить
                </div>
                <div class="url-example">
                    /?name=John&message=Welcome
                </div>
                <div class="url-example">
                    /?name=Мир&message=Привет
                </div>
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