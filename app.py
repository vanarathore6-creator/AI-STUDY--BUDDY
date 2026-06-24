from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    q = request.form['question'].lower()

    if "operator" in q:
        return "Operator C language me +, -, *, / jaise symbols hote hain."

    elif "python" in q:
        return "Python ek high-level programming language hai."

    elif "html" in q:
        return "HTML web pages banane ke liye use hoti hai."

    elif "loop" in q:
        return "Loop ek statement ko baar-baar execute karne ke liye use hota hai."

    elif "h2o" in q:
        return "H2O pani (water) ka chemical formula hai."

    else:
        return "Sorry, mujhe is question ka answer nahi aata."

if __name__ == "__main__":
    app.run(debug=True)