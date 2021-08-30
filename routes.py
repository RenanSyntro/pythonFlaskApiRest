from flask import Flask, request
from flask.wrappers import Response
from werkzeug.wrappers import response
from user import insertUser

app = Flask("Youtube")

@app.route("/hellowold", methods=["GET"])
def hellowold():
    return ("Hello Wold")

@app.route("/registration/user", methods=["POST"])
def registrationuser():
    body = request.get_json()

    if ("name" not in body):
        return generateResponse(400, "The name parameter is mandatory")

    if ("email" not in body):
        return generateResponse(400, "The email parameter is mandatory")

    if ("password" not in body):
        return generateResponse(400, "The password parameter is mandatory")

    user = insertUser(body["name"], body["email"], body["password"])

    print(body)

    return generateResponse(200, "Created user", "user", user)

def generateResponse(status, message, content_name=False, content=False):
    response = {}
    response["status"] = status
    response["message"] = message

    if(content_name and content):
        response[content_name] = content

    return response

app.run()
