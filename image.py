import openai
import yaml
import os
import time
from PIL import Image

def create_image(text):
  with open('key.yaml') as f:
    api = yaml.load(f, Loader=yaml.FullLoader)
  key = api["openai_key"]

  openai.api_key=key
  print("requested")

  response = openai.Image.create(
    prompt=text,
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']

  #print(image_url)
  image_download(image_url,text)

def image_download(url,text):
  name=text+".jpg" #저장될 이미지 파일 이름
  os.system("culr"+url+"> "+name)

  img = Image.open(name) #이미지 확인하기  