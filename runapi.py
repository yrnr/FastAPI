import requests
from PIL import Image
import io

res = requests.get("http://127.0.0.1:8000/myfirstapi")
print(res.json())
print(res.text)
res = requests.get("http://127.0.0.1:8000/my-first-api?name=Aadideva")
print(res.json())
print(res.text)
res = requests.get("http://127.0.0.1:8000/say-hello-api")
print(res.json())
print(res.text)
res = requests.get("http://127.0.0.1:8000/say-hello-api?name=Diwaakara")
print(res.json())
print(res.text)
res = requests.get("http://127.0.0.1:8000/get-iris")
print(res.text)
res = requests.get('http://127.0.0.1:8000/plot-iris')
file = io.BytesIO(res.content)
im = Image.open(file)
im.show()