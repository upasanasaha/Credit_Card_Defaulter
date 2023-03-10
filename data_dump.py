import pymongo
import pandas as pd
import json
from predictor.config import mongo_client

DATA_FILE_PATH="/config/workspace/UCI_Credit_Card.csv"
DATABASE_NAME="credit_card"
COLLECTION_NAME="payments"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    #Convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True,inplace=True)
    json_record = list(json.loads(df.T.to_json()).values())

    #Changing float to int values:
    json_record_int=[]
    for i in range(len(json_record)):
        x=json_record[i]
        for key in x:
            x[key]=int(x[key])
        json_record_int.append(x)
    print(json_record_int[0])
    #insert converted json record to mongo db
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record_int)