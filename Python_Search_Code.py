#Python_Search_Code


from flask import Flask, request, render_template;
import wikipedia;


'''
git clone https://github.com/projectmesa/mesa mesa_repo
cd mesa_repo
pip install `pwd`
'''


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        search = request.form["search"]

        result = wikipedia.summary(search, sentences=2)
        return f"<h1>{result}</h1>"


if __name__ == '__main__':
    app.run(debug=True)


