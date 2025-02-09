from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")  # This defines the route for the main page (/)
def index():
    return render_template("index.html")  # Render the index.html template

if __name__ == "__main__":
    app.run(debug=True)  # Start the Flask development server (debug=True for automatic reloading)
