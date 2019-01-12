'''ENTRY POINT OF THE APP'''
from app import create_app

configName= 'development'
app = create_app(configName)

@app.route('/')
def index():
    return "Welcome"

if __name__ == "__main__":
    app.run(debug=True)
    