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

def calcularFyD(claseAcero, coeficiente):
    if claseAcero == 'S235':
        return 235/coeficiente
    elif claseAcero == 'S275':
        return 275/coeficiente
    elif claseAcero == 'S355':
        return 355/coeficiente
    else:
        return 450/coeficiente

def calcularXLT(fi, Esblt):
    if 1 / (fi + (fi * fi - Esblt * Esblt)**0.5) > 1 : 
        return 1
    else:
        return 1 / (fi + (fi * fi - Esblt * Esblt)**0.5)

def calcularEsbLim(claseAcero):
    if claseAcero == 'S235':
        return 93.9
    elif claseAcero == 'S275':
        return 86.8
    elif claseAcero == 'S355':
        return 76.4
    else:
        return 67.9

def calcularCurvaPandeoY(claseAcero):
    if claseAcero == 'S450':
        return "a0"
    else:
        return "a"

def calcularCurvaPandeoZ(claseAcero):
    if claseAcero == 'S450':
        return "a0"
    else:
        return "b"

def calcularXy(curvaPandeoY):
    if curvaPandeoY == "a0":
        return 0.98
    elif curvaPandeoY == "a":
        return 0.97
    elif curvaPandeoY == "b":
        return 0.96
    elif curvaPandeoY == "c":
        return 0.94
    else:
        return 0.91

def calcularXz(curvaPandeoZ):
    if curvaPandeoZ == "a0":
        return 0.27
    elif curvaPandeoZ == "a":
        return 0.25
    elif curvaPandeoZ == "b":
        return 0.24
    elif curvaPandeoZ == "c":
        return 0.22
    else:
        return 0.20


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
        #Recogemos los valores introducidos por la aplicacion
        tipoAcero = post_data["name"]
        claseAcero = post_data["tipoAcero"]
        coeficiente = float(post_data["coeficiente"])

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
        Fyd = calcularFyD(claseAcero, coeficiente)

        #Calculo de resistencias
        resN = calcularResN(Fyd, a)
        resMy = calcularResMy(fCompr, Wel, Wpl, Fyd)
        resMz = calcularResMz(fCompr, Welz, Wplz, Fyd)

        resN = (round(resN, 1))
        resMy = (round(resMy, 1))
        resMz = (round(resMz, 1))

        response_object['message'] ='Data added!'
        return jsonify({'Resistencia N' : resN, 'Resistencia My' : resMy, 'Resistencia Mz' : resMz})
    else:
        
        response_object = {'status':'success'}
        response_object['message'] ='Data added!'
        return jsonify(response_object)
        

@cross_origin
@app.route("/PandeoLateral", methods=['POST', 'GET'])
def getPandeoLateral():
    if request.method == "POST":
        
        response_object = {'status':'success'}
        post_data = request.get_json()
        #Recogemos los valores introducidos por la aplicacion
        tipoAce = post_data["name"]
        claseAcero = post_data["tipoAcero"]
        coeficiente = float(post_data["coeficiente"])
        resNecN = float(post_data["resNecN"])
        L = float(post_data["L"])
        Blt = float(post_data["Blt"])
        C1 = float(post_data["C1"])
        k2 = float(post_data["K2"])
        E = float(post_data["E"])
        G = float(post_data["G"])
        Lc = L * Blt

        #Pasamos de la E y G recibida (Gpa) a E y G (Mpa)
        E = E * 1000
        G = G * 1000

        df = pd.read_excel('Excel.xlsx', header = None,  sheet_name='IPE', skiprows=6, usecols = "B:AP")
        is_TipoAcero = df.loc[:, 1] == tipoAce
        df_TipoAcero = df.loc[is_TipoAcero]

        #Extraigo los datos necesarios para calculo del Pandeo Lateral.
        a = df_TipoAcero.iloc[0][8]
        Wel = df_TipoAcero.iloc[0][20]
        Wpl = df_TipoAcero.iloc[0][21]
        Welz = df_TipoAcero.iloc[0][25]
        Wplz = df_TipoAcero.iloc[0][26]
        h = df_TipoAcero.iloc[0][3]
        b = df_TipoAcero.iloc[0][4]
        tf = df_TipoAcero.iloc[0][6]  
        tw = df_TipoAcero.iloc[0][5]
        hi = df_TipoAcero.iloc[0][9]  
        iz = df_TipoAcero.iloc[0][27]
        It = df_TipoAcero.iloc[0][29]
        Iz = df_TipoAcero.iloc[0][24]

        fCompr = flexCompr(tipoAce)
        Fyd = calcularFyD(claseAcero, coeficiente)
        hdb = h/b
        alfaLT = 0
        curva = 'a'
        if hdb > 2:
            alfaLT = 0.34
            curva = 'b'
        else:
            alfaLT = 0.21

        #Calculo z,f
        zf = resNecN * 1000 / Fyd / tw
        if zf > hi:
            zf = hi
        alaComp = (zf + hi) / 2
        #Calculo de Iz,f
        izf = (tf*(b**3)/12/(tf*b + alaComp * tw / 3))**0.5

        resMy = calcularResMy(fCompr, Wel, Wpl, Fyd)

        #Calculamos MLTw MLTv y MCR
        Mltw = Wel * 1000.0 * (3.1416**2) * E / (Lc * 100.0 / iz)**2 * C1 / 1000000.0
        Mltv = (G * E * It * 10000 * Iz * 10000)**0.5 * 3.1416 * C1 / Lc / 1000000000
        Mcr = ((Mltw**2 + Mltv**2))**0.5 * k2
        Esblt = (resMy * coeficiente / Mcr)**0.5
        fi = 0.5 * (1 + alfaLT*(Esblt - 0.2) + Esblt**2)
        xlt = calcularXLT(fi, Esblt)
        MbRd = xlt * resMy

        #Redondeamos a un decimal
        Mltw = (round(Mltw, 1))
        Mltv = (round(Mltv, 1))
        Mcr = (round(Mcr, 1))
        Esblt = (round(Esblt, 1))
        fi = (round(fi, 1))
        xlt = (round(xlt, 1))
        MbRd = (round(MbRd, 1))

        response_object['message'] ='Data added!'
        return jsonify({'Mltw' : Mltw, 'Mltv' : Mltv, 'Mcr' : Mcr, 'Esblt' : Esblt, 'fi' : fi, 'xlt' : xlt, 'MbRd' : MbRd })
    else:
        
        response_object = {'status':'success'}
        response_object['message'] ='Data added!'
        return jsonify(response_object)

@cross_origin
@app.route("/PandeoCompresion", methods=['POST', 'GET'])
def getPandeoCompresion():
    if request.method == "POST":
        
        response_object = {'status':'success'}
        post_data = request.get_json()
        #Recogemos los valores introducidos por la aplicacion
        tipoAce = post_data["name"]
        claseAcero = post_data["tipoAcero"]
        coeficiente = float(post_data["coeficiente"])       
        L = float(post_data["L"])
        By = float(post_data["By"])
        Bz = float(post_data["Bz"])
        resNecN = float(post_data["resNecN"])

        df = pd.read_excel('Excel.xlsx', header = None,  sheet_name='IPE', skiprows=6, usecols = "B:AP")
        is_TipoAcero = df.loc[:, 1] == tipoAce
        df_TipoAcero = df.loc[is_TipoAcero]

        #Extraigo los datos necesarios para calculo del Pandeo Lateral.
        a = df_TipoAcero.iloc[0][8]
        iz = df_TipoAcero.iloc[0][27]
        iy = df_TipoAcero.iloc[0][22]

        fCompr = flexCompr(tipoAce)
        Fyd = calcularFyD(claseAcero, coeficiente)
        resN = calcularResN(Fyd, a)
        
        Lky = L * By * 1000
        Lkz = L * Bz * 1000

        lambday = Lky / (iy * 10)
        lambdaz = Lkz / (iz * 10)

        esbLim = calcularEsbLim(claseAcero)

        curvaY = calcularCurvaPandeoY(claseAcero)
        curvaZ = calcularCurvaPandeoZ(claseAcero)

        xy = calcularXy(curvaY)
        xz = calcularXz(curvaZ)

        lambdaRedy = lambday / esbLim
        lambdaRedz = lambdaz / esbLim

        Ncry = (3.1416 / lambday)**2 * a * 21000
        Ncrz = (3.1416 / lambdaz)**2 * a * 21000

        print(xy, xz, resN)
        Nbrdy = resN * xy
        Nbrdz = resN * xz

        interacy = resNecN / Nbrdy
        interacz = resNecN / Nbrdz

        #Redondeamos los resultados
        Lky = (round(Lky, 1))
        Lkz = (round(Lkz, 1))
        lambday = (round(lambday, 1))
        lambdaz = (round(lambdaz, 1))
        lambdaRedy = (round(lambdaRedy, 2))
        lambdaRedz = (round(lambdaRedz, 2))
        xy = (round(xy, 2))
        xz = (round(xz, 2))
        Ncry = (round(Ncry, 1))
        Ncrz = (round(Ncrz, 1))
        Nbrdy = (round(Nbrdy, 1))
        Nbrdz = (round(Nbrdz, 1))
        interacy = (round(interacy, 2))
        interacz = (round(interacz, 2))

        response_object['message'] ='Data added!'
        return jsonify({'Lky' : Lky, 'Lkz' : Lkz, 'lambday' : lambday, 'lambdaz' : lambdaz, 'lamRedY' : lambdaRedy, 
        'lamRedZ' : lambdaRedz, 'curvaY' : curvaY, 'curvaZ' : curvaZ, 'xy' : xy, 'xz' : xz, 'Ncry' : Ncry , 
        'Ncrz' : Ncrz, 'Nbdrdy' : Nbrdy, 'Nbdrdz' : Nbrdz, 'interaccion y' : interacy, 'interaccion z' : interacz})
    else:
        
        response_object = {'status':'success'}
        response_object['message'] ='Data added!'
        return jsonify(response_object)

if __name__ == '__main__':
    app.run(debug=True)
