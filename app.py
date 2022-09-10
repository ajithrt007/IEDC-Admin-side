from flask import Flask, render_template, request, jsonify, url_for, redirect
from databaseop import connect_to_mongodb, increase_visitorcount, desc_sorted_classnames, add_class_score

app = Flask(__name__)
mongodb_client = connect_to_mongodb("mongodb+srv://anandhus:anandhu%40mongo@cluster0.lzunamf.mongodb.net/?retryWrites=true&w=majority")
classes = ['R2A', 'R2B', 'R4A', 'R4B', 'R6', 'T2A', 'T2B', 'T4A', 'T4B', 'T6A', 'T6B', 'M2A', 'M2B', 'M4A', 'M4B', 'M6', 'B2', 'B4', 'B6', 'P4', 'P6', 'U2', 'U4', 'U6', 'other']


@app.route("/")
def home():
    increase_visitorcount(mongodb_client)
    sorted_records = desc_sorted_classnames(mongodb_client).limit(5)
    data = []
    for record in sorted_records:
        tempdict = {}
        tempdict["Class"] = record["Class"]
        tempdict["Score"] = record["Score"] 
        data.append(tempdict)
    return render_template("user.html", sorted_records = data)

@app.route("/intermediate")
def interm():
    return render_template("error-page.html")

# @app.route("/intermediate", methods=['POST'])
# def interm_selectclass():
#     classname = request.form.get('class')
#     print(classname)
#     return redirect(url_for('game', classname = classname))

@app.route('/game')
def notgame():
    return render_template("error-page.html")

@app.route("/game/<classname>")
def game(classname):
    # if classname not in classes:
    #     return redirect(url_for('interm_selectclass'))
    return render_template("error-page.html")

@app.route("/score")
def addscore():
    class_name = request.args.get('class')
    # if class_name == "other":
    #     return jsonify({"status":"success"})
    # score = int(request.args.get('score'))
    # add_class_score(mongodb_client, class_name, score)
    # file = open("log.txt","a")
    # file.write(class_name+":"+score+"\n")
    # file.close()
    # return jsonify({"status":"success"})
    ip_addr = request.remote_addr
    db = mongodb_client['hack']
    collection = db['ipaddress']
    gotip = {"Class":class_name, "ipaddress": ip_addr}
    collection.insert_one(gotip)
    file = open('ipaddress.txt', 'a')
    file.write("ip address:" + ip_addr+ " class:"+class_name+"\n")
    return render_template("error-page.html", moonjikko = 1)

if __name__ == "__main__":
    #mongodb_client = connect_to_mongodb("mongodb+srv://anandhus:anandhu%40mongo@cluster0.lzunamf.mongodb.net/?retryWrites=true&w=majority")
    #classes = ['R2A', 'R2B', 'R4A', 'R4B', 'R6', 'T2A', 'T2B', 'T4A', 'T4B', 'T6A', 'T6B', 'M2A', 'M2B', 'M4A', 'M4B', 'M6', 'B2', 'B4', 'B6', 'P4', 'P6', 'U2', 'U4', 'U6', 'other']
    app.run(debug=False, host='0.0.0.0', port="8080")
