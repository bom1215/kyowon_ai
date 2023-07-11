import openai
import yaml
import os
import time
from PIL import Image
import pandas as pd
import urllib.request as req

with open('api.yaml') as f:
    api = yaml.load(f, Loader=yaml.FullLoader)
#key = api["image_key"]
key = api["openai.api_key"]
openai.api_key=key

print("requested")

def create_image(text):
  """
  주어진 text를 이용하여 이미지 생성
  Parameter:
    text : 이미지로 생성할 텍스트
  return
    이미지 경로
  """
  new_text=text+",2d illust drawing"
  response = openai.Image.create(
    prompt=new_text,
    n=1,
    size="256x256" #1024x1024, 512x512, 256x256
  )
  image_url = response['data'][0]['url']
  
  #print(image_url)
  return image_download(image_url,text)

def image_download(url,text):
  """
  url로부터 이미지를 다운로드하는 함수
  Parameter
    text : 해당 이미지에 대한 텍스트
  return
    이미지 경로
  """
  name="./images/"+text+".jpg" #저장될 이미지 파일 이름
  #os.system("curl "+url+"> "+name)
  download = req.urlretrieve(url,name)
  #img = Image.open(name) #이미지 확인하기 
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
  create_image("천문학자는 별을 보지 않는다")
  #csv2image()