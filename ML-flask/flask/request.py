
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Age':0,'Gender':1, 'Total_Bilirubin':7,'Direct_Bilirubin':5,'Alkaline_Phosphotase':187,'Alamine_Aminotransferase':64,"Aspartate_Aminotransferase":68, 'Total_Proteins':10,'Albumin':3,'Albumin_and_Globulin_Ratio':1})

print(r.json())
