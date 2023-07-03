from distutils.log import INFO
from hashlib import new
import pymongo
import re
import yaml
import pandas as pd
import os.path
from os import path

def read_files():
    with open('api.yaml') as f:
        db_key = yaml.load(f, Loader=yaml.FullLoader)

    client = pymongo.MongoClient(db_key['mongo_client'])

    #fill - db이름으로 채우기
    db = client.fill
    collection = db.fill 

    print("database")
    title="data/학교생활-초급.csv"
    df = pd.read_csv(title) 
    
    for i in range(0,len(df)):
        sen=df.loc[i,'sentence']
        word=df.loc[i,'word']

        if path.exists("./images/"+sen+".jpg"):
            df.loc[i,'sen_img']="./images/"+sen+".jpg"
            df.loc[i,'word_img']="./images/"+word+".jpg"

            sen_img = df.loc[i,'sen_img']
            word_img = df.loc[i,'word_img']
            topic='학교생활'
            doc = {'topic':topic,'sentence':sen,'word':word,'sen_img':sen_img,'word_img':word_img}
            collection.insert_one(doc)

    df.to_csv("./data/학교_초급.csv")

if __name__ == '__main__':
    read_files()