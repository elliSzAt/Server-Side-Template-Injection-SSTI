from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    template = """
    <html>
        <body>
            <h1>Welcome to Trongdeptrai's website!</h1>
            <h2>M thích mưa hay thích sấm chớp</h2>
            <p>{{ message }}</p>
        </body>
    </html>
    """
    message = request.args.get('message', '')
    return render_template_string(template, message=message)

if __name__ == '__main__':
    app.run(debug=True)
