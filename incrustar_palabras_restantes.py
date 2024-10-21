# Abrir archivos
from io import open; 
# Importar - exportar JSON
import json; 
import pickle;

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



