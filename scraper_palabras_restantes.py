"""
# Abrir archivos
from io import open; 
# Importar - exportar JSON
import json; 
import pickle;
from proyectoDiccionario.generar_diccionario_inicial import agregarPalabraDiccionario

archivo_definiciones=open ("definiciones", "rb")
#
definiciones = pickle.load(archivo_definiciones)
#
archivo_definiciones.close()


# Importación de archivos
diccionario_archivo=open ("diccionario_sin_etiquetas_con_conjugaciones_sinonimos_y_redirecciones.json", "rb")
diccionario_json = json.load (diccionario_archivo)
diccionario_archivo.close()

# Verificación de integridad de todas las palabras 

todas_palabras_archivo = open ("0_palabras_todas_no_conjugaciones.txt", "r")
todas_palabras= todas_palabras_archivo.readlines()

contador =0; 

palabras_no_registradas=[];

for palabra in todas_palabras:
    try:
        diccionario_json[palabra[0]][palabra.strip().replace("\n", "")]
    except: 
        try:
            diccionario_json[palabra[0]][diccionario_json[palabra[0]][palabra][0]['redir']]
            
        except:
            contador = contador +1;
            palabras_no_registradas.append(palabra.replace("\n", ""))

print ("Errores totales", contador)

print (palabras_no_registradas)
"""
from bs4 import BeautifulSoup
import requests, sys
from datetime import datetime
import re

from separasilabas import  *
silabas = silabizer()


def agregarPalabraDiccionario (palabra, origen, definicion, formas_compuestas, envios): 

    [
        {
            "palabra": "filisteísmo",
            "origen": [],
            "sinonimos": [],
            "definicion": "m. Condición de  **filisteo** (persona de espíritu vulgar).",
            "formas_compuestas": [],
            "envios": []
        }
    ]
    
    
# Cargar formas verbales faltantes 
# verbos = [ "abarse", "abolir", "acaecer", "acontecer", "adir", "agredir", "amanecer", "anochecer", "apedrear", "arrecir", "asaborir", "atañer", "atardecer", "aterir", "aperturar", "apalizar", "antagonizar", "balbucir", "blandir", "cellisquear", "chaparrear", "chispear", "clarear", "clarecer", "colorir", "concernir", "clicar", "descolorir", "diluviar", "empedernir", "encelajarse", "fucilar", "garantir", "garuar", "gotear", "granizar", "harinear", "helar", "interrelacionar", "lloviznar", "manir", "marcear", "mayear", "mollinar", "mollir", "molliznar", "molliznear", "nevar", "neviscar", "obstar", "orvallar", "oscurecer", "pasar", "pintear", "preterir", "pringar", "refocilar", "relampaguear", "resultar", "suceder", "tardecer", "transgredir", "trapear", "tronar", "usucapir", "ventar", "ventear", "ventiscar", "ventisquear", "zaracear" ] 
# Cargar palabras faltantes

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
def acepciones(palabra):
    
    try:
        request = requests.get(f'https://dle.rae.es/{palabra}', headers=HEADER)
        soup = BeautifulSoup(request.text, 'lxml')
        
        word_text = [a.text for a in soup.find_all(attrs={'class':'f'})]
        palabra_salida = word_text
        
        aceps_text = [a.text for a in soup.find_all(attrs={'class':'j'})]
        definicion = [re.sub(r'\b\d{1,2}\.\s?', '', texto) for texto in aceps_text]
        
        origin_text = [a.text for a in soup.find_all(attrs={'class':'n2'})]
        origen = origin_text
        
        send_text = [a.text for a in soup.find_all(attrs={'class':'b'})]
        envios = send_text
        
        # Si tiene redir, append  uno. 
        redir_word = [a.text for a in soup.find_all(attrs={'class':'n1'})]
        
        
        return {
            "palabra":palabra_salida,
            "definicion":definicion,
            "origen":origen,
            "envios":envios,
            "formas_compuestas": []
            
        };
    
    
    
    except Exception as e:
        print(f"Error al obtener las acepciones de '{palabra}': {e}")
        return

print (acepciones("ligatorio"))
    
