from email import header
from flask import Flask, render_template, url_for, request, redirect, json, jsonify, Blueprint
from flask_cors import CORS, cross_origin
import pandas as pd

#2 -> IPE 240 - IPE 400 HE 280 A -> HE 300 A 
def flexCompr(tipoMetal):
    if tipoMetal == 'IPE 240' or tipoMetal == 'IPE 270' or tipoMetal == 'IPE 300' or tipoMetal == 'IPE 330' or tipoMetal == 'IPE 360' or tipoMetal == 'IPE 400' or tipoMetal == 'HE 280 A' or tipoMetal == 'HE 300 A' :
        return 2
    else:
        return 1 

def calcularResN(Fyd, a):
    return Fyd * a / 10

def calcularResMy(fCompr, Wel, Wpl, Fyd):
    if fCompr >= 4:
        return 0
    elif fCompr >= 3:
        return Wel * Fyd / 1000
    else :
        return Wpl * Fyd / 1000

def calcularResMz(fCompr, Welz, Wplz, Fyd):
    if fCompr >= 4:
        return 0
    elif fCompr >= 3:
        return Welz * Fyd / 1000
    else :
        return Wplz * Fyd / 1000

app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': 'http://localhost'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'
#CORS_ORIGIN_ALLOW_ALL = True

@cross_origin
@app.route("/data", methods=['GET'])
def getExcel():
    excel = {}
    with open("Excel2.csv", "r") as f:
        datos = f.readlines()
        excel['Tipos'] = list(filter(lambda x: len(x.strip())>0, datos[0].split(";")))
        i = 1
        for tipo in excel['Tipos']:
            excel[tipo] = list(filter(lambda x: len(x.strip())>0, datos[i].split(";")))
            i = i+1
    return jsonify(excel)
@cross_origin
@app.route("/dataentry", methods=['POST', 'GET'])
def getResistencias():
    if request.method == "POST":
        
        response_object = {'status':'success'}
        post_data = request.get_json()
        tipoAcero = post_data["name"]

        print(tipoAcero)

        df = pd.read_excel('Excel.xlsx', header = None,  sheet_name='IPE', skiprows=6, usecols = "B:AP")

        is_TipoAcero = df.loc[:, 1] == tipoAcero
        df_TipoAcero = df.loc[is_TipoAcero]

        #Extraigo los datos necesarios para calculo de resistencias.
        a = df_TipoAcero.iloc[0][8]
        Wel = df_TipoAcero.iloc[0][20]
        Wpl = df_TipoAcero.iloc[0][21]
        Welz = df_TipoAcero.iloc[0][25]
        Wplz = df_TipoAcero.iloc[0][26]
        fCompr = flexCompr(tipoAcero)
        #Fyd es constante para todos los tipos de Acero
        Fyd = 275/1.05
        resN = calcularResN(Fyd, a)
        resMy = calcularResMy(fCompr, Wel, Wpl, Fyd)
        resMz = calcularResMz(fCompr, Welz, Wplz, Fyd)

        resN = (round(resN, 1))
        resMy = (round(resMy, 1))
        resMz = (round(resMz, 1))

        print(resN,resMy,resMz)
        response_object['message'] ='Data added!'
        return jsonify({'Resistencia N' : resN, 'Resistencia My' : resMy, 'Resistencia Mz' : resMz})
        #return jsonify(resN)
    else:
        
        response_object = {'status':'success'}
        response_object['message'] ='Data added!'
        return jsonify(response_object)

if __name__ == '__main__':
    app.run(debug=True)