from flask import Flask, make_response

app = Flask("PortfolioAPI")

@app.route("/projects")
def projects():
    projectsList = {"projects" : [{"name": "akash"}]}
    res = make_response(projectsList,200)
    res.headers["Access-control-allow-origin"] = "*"
    return res

app.run()