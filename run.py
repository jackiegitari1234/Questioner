'''ENTRY POINT OF THE APP'''
from app import create_app

config_name= 'development'
app = create_app(config_name)

@app.route('/')
def index():
    return "Welcome"

if __name__ == "__main__":
    app.run(debug=True)
    