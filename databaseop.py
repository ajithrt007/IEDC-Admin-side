import pymongo

#function to connect to the mongo db
def connect_to_mongodb(conn_string):
    try:
        mongodb_client = pymongo.MongoClient(conn_string)
        print("Connection to mongodb successfull")
        return mongodb_client
    except Exception as e:
        print("Error while connecting!")
        print(e)
        exit()

#increment the number of visitors
def increase_visitorcount(mongodb_client):
    db = mongodb_client['sitedetails']
    collection = db['vismisvistor']
    result = collection.find_one({"identification":"count"})
    curr_score = result['Visitors']
    curr_score += 1
    condition = {"identification": "count"}
    setscore = {"$set": {"Visitors": curr_score}}
    try:
        collection.update_one(condition, setscore)
    except:
        print("Error while Updating the visitors")
        exit()

#to get all the class names and current scores
def desc_sorted_classnames(mongodb_client):
    db = mongodb_client['classes']
    collection = db['classandmarks']
    records = collection.find().sort('Score', pymongo.DESCENDING).limit(24)
    return records

#to add to the class score
def add_class_score(mongodb_client, class_name, score):
    db = mongodb_client['classes']
    collection = db['classandmarks']
    result = collection.find_one({"Class": class_name})
    curr_score = result['Score']
    curr_score += score
    condition = {"Class": class_name}
    setscore = {"$set": {"Score": curr_score}}
    try:
        collection.update_one(condition, setscore)
        print("Score updated for "+class_name)
    except:
        print("Error while updating class score when played by class"+class_name)
        exit()