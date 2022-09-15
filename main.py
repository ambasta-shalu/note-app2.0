from flask import Flask, jsonify, request
from db.Database import *


app = Flask(__name__)
db = Database()


@app.route("/")
def welcome():
    return "Hello! Welcome to Note2.0 \nBy Shalu Ambasta ❤"



@app.route("/notes", methods=['GET'])
def getAllNote():
    data = db.readAll()
    return jsonify({"Notes" : data})



@app.route("/notes/<int:note_id>", methods=["GET"])
def getNote(note_id):
    data = db.readOne(note_id)
    return jsonify({"Note" : data})



@app.route("/notes", methods=['POST'])
def addNote():
    data  = request.get_json()
    print(data)
    db.create(data["title"], data["description"])
    return "Added"


@app.route("/notes/<int:note_id>", methods=["PUT"])
def updateNote(note_id):
    print(note_id)
    data = request.get_json()
    db.update(note_id, data["title"], data["description"])
    return "Updated"
   


@app.route("/notes/<int:note_id>", methods=["DELETE"])
def deleteNote(note_id):
    db.delete(note_id)
    return "Deleted"



if __name__ == "__main__":
    app.run(debug=True, port=7777, use_reloader = True)
