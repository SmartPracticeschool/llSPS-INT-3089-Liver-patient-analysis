
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Age':44,'Gender':1, 'Total_Billirubin':8,"Aspartate_Aminotransferase":68, 'Total_Protiens':9})

print(r.json())
