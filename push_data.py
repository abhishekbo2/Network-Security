import os
import sys
import pandas as pd
import numpy as np
import pymongo
import certifi
import json
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.Log.logger import logging

ca = certifi.where()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    
    def push_data_to_mongodb(self, database, collection, records):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_clint = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_clint[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

if __name__ == "__main__":
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "Abhi"
    collection = "Network data"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_converter(file_path= FILE_PATH)
    print(records)
    no_of_records = networkobj.push_data_to_mongodb(database= DATABASE, collection=collection, records=records)
    print(no_of_records)

    

    