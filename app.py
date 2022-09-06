from flask import Flask, render_template, request, jsonify, url_for, redirect
from databaseop import connect_to_mongodb, increase_visitorcount, desc_sorted_classnames, add_class_score

app = Flask(__name__)
mongodb_client = connect_to_mongodb("mongodb+srv://anandhus:anandhu%40mongo@cluster0.lzunamf.mongodb.net/?retryWrites=true&w=majority")
classes = ['R2A', 'R2B', 'R4A', 'R4B', 'R6', 'T2A', 'T2B', 'T4A', 'T4B', 'T6A', 'T6B', 'M2A', 'M2B', 'M4A', 'M4B', 'M6', 'B2', 'B4', 'B6', 'P4', 'P6', 'U2', 'U4', 'U6', 'other']


@app.route("/")
def home():
    increase_visitorcount(mongodb_client)
    return render_template("user.html")

@app.route("/intermediate")
def interm():
    return render_template("intermediate.html")

@app.route("/intermediate", methods=['POST'])
def interm_selectclass():
    classname = request.form.get('class')
    print(classname)
    return redirect(url_for('game', classname = classname))

@app.route('/game')
def notgame():
    return redirect(url_for('interm_selectclass'))

@app.route("/game/<classname>")
def game(classname):
    if classname not in classes:
        return redirect(url_for('interm_selectclass'))
    return render_template("game.html", classname = classname)

@app.route("/score")
def addscore():
    class_name = request.args.get('class')
    score = int(request.args.get('score'))
    add_class_score(mongodb_client, class_name, score)
    return jsonify({"status":"success"})


if __name__ == "__main__":
    #mongodb_client = connect_to_mongodb("mongodb+srv://anandhus:anandhu%40mongo@cluster0.lzunamf.mongodb.net/?retryWrites=true&w=majority")
    #classes = ['R2A', 'R2B', 'R4A', 'R4B', 'R6', 'T2A', 'T2B', 'T4A', 'T4B', 'T6A', 'T6B', 'M2A', 'M2B', 'M4A', 'M4B', 'M6', 'B2', 'B4', 'B6', 'P4', 'P6', 'U2', 'U4', 'U6', 'other']
    app.run(debug=True)