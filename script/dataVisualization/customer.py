import numpy as np
import pandas as pd
import csv
import json, ast
from pymongo import MongoClient
from pandas import Series, DataFrame

client = MongoClient("mongodb://efrata.xyz:27019")
db = client.ecommerceDB
cursor = db.customer.find()
df = pd.DataFrame(list(cursor))
df.plot();
#print df
