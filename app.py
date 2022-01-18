from emmett import App
from emmett.tools import service

app = App(__name__)

def getUsers():
    users = []
    for index in range(1, 1001):
        strIndex = str(index)
        firstName = "FirstName" + strIndex
        lastName = "LastName" + strIndex
        framework = "Python (Emmett)"
        users.append({
            "index": index,
            "FirstName": firstName,
            "LastName": lastName,
            "age": 25,
            "framework": framework,
        })
    return users

@app.route("/")
async def index():
    return "Hello, World!"

@app.route("users", methods='get')
@service.json
async def users():
    return getUsers()
