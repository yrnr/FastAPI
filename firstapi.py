from fastapi import FastAPI
import pandas as pd
import matplotlib.pyplot as plt
from starlette.responses import StreamingResponse

app = FastAPI() 

@app.get("/myfirstapi")       
def hello():
    return {"aadi_deva" : "namastubhyam"}

@app.get("/my-first-api")
def hello(name: str):
  return {'Hello ' + name + '!'} 

@app.get("/say-hello-api")
def hello(name = None):
    if name is None:
        text = 'Hello you!'
    else:
        text = 'Hello ' + name + '!'
    return text

@app.get("/get-iris")
def get_iris():
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)
    return iris

@app.get("/plot-iris")
def plot_iris():
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)
    plt.scatter(iris['sepal_length'], iris['sepal_width'])
    plt.savefig('iris.png')
    file = open('iris.png', mode="rb")
    return StreamingResponse(file, media_type="image/png")