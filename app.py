from flask import Flask
import os
from dotenv import load_dotenv
from routes.tareas import tareas_bp

#Load all the .env credentials
load_dotenv()

def create_app(): # Function to create the app
    # App instance
    app=Flask(__name__)
    
    #Register blueprint
    app.register_blueprint(tareas_bp, url_prefix="/tareas")
    
    return app
    
app = create_app()

if __name__ == "__main__":
    # Get the Port
    port = int(os.getenv("PORT",8000))

    # Run the application 
    app.run(host="0.0.0.0", port=port, debug=True)