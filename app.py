from distutils.log import debug
from flask import Flask

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return "My CI CD Pipeline has been eatablished."

if __name__=="__main__":
    app.run(debug=True)

