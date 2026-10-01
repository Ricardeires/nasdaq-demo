from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NASDAQ DEMO</title>
        <style>
            body {
                background: #111827;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 40px 15px;
            }
            .box {
                max-width: 700px;
                margin: auto;
                background: #1f2937;
                padding: 30px;
                border-radius: 16px;
            }
            h1 { color: #60a5fa; }
            .ok {
                color: #4ade80;
                font-size: 22px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>NASDAQ DEMO</h1>
            <p class="ok">SISTEMA FUNCIONANDO</p>
            <p>Entorno de pruebas de estrategias Nasdaq</p>
            <p>Conexión Render + GitHub correcta</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
