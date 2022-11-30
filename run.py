from app import app

# decorador
# endpoint
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Si esta aqui el programa principal, ejecutalo
if __name__ == "__main__":   
    app.run(debug = True)
    
