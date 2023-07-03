import openai
import yaml
import os
import time
from PIL import Image
import pandas as pd

with open('api.yaml') as f:
    api = yaml.load(f, Loader=yaml.FullLoader)
key = api["image_key"]

openai.api_key=key
print("requested")

def create_image(text):
  new_text=text+",2d illust drawing"
  response = openai.Image.create(
    prompt=new_text,
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']

  #print(image_url)
  return image_download(image_url,text)

def image_download(url,text):
  name="./images/"+text+".jpg" #저장될 이미지 파일 이름
  os.system("curl "+url+"> "+name)

  img = Image.open(name) #이미지 확인하기 
  return name 

def csv2image():
  title="data/학교생활-초급.csv"
  df = pd.read_csv(title)  

  df['sen_img']='0'
  df['word_img']='0'
  print(df)
  for i in range(0,len(df)):
    sen=df.loc[i,'sentence']
    word=df.loc[i,'word']
    df.loc[i,'sen_img']=create_image(sen)
    df.loc[i,'word_img']=create_image(word)

  df.to_csv(title,index=False)
  
if __name__ == '__main__':
  csv2image()