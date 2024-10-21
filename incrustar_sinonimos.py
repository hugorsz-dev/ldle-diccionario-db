# Abrir archivos
from io import open; 
# Importar - exportar JSON
import json; 
#

# Importación de archivos
diccionario_archivo=open ("diccionario_sin_etiquetas_con_conjugaciones.json", "rb")
diccionario_json = json.load (diccionario_archivo)
diccionario_archivo.close()

sinonimos_archivo=open ("sinonimos.json", "rb")
sinonimos_json = json.load (sinonimos_archivo)
sinonimos_archivo.close()

print (sinonimos_json[0])


def eliminarCadenaArray (array, cadena):
    for i in range(len(array)-1): 
        if array[i]==cadena:
            array.pop(i)
    return array
# caminos, camiones, intelectuales, usuarios, 

def pasarASingular (cadena):
    if cadena[len(cadena)-2:] == "es":
        return cadena[:len(cadena)-2:];
    elif cadena[len(cadena)-1:] == "s":
        return cadena[:len(cadena)-1:];
    else: return False;


contador_errores =0;
contador_palabras =0;
for linea in sinonimos_json:
    
    for palabra in linea: 
        for sinonimo in eliminarCadenaArray(linea, palabra):
            contador_palabras = contador_palabras +1;
             # Intento normal
            try:
                diccionario_json[palabra[0]][palabra][0]["sinonimos"].append(sinonimo)
            except:
                # Intento plural
                try:
                    diccionario_json[palabra[0]][pasarASingular(palabra)][0]["sinonimos"].append(sinonimo)
                except: 
                    # Intento redir
                    try:
                        diccionario_json[palabra[0]][diccionario_json[palabra[0]][palabra][0]['redir']][0]["sinonimos"].append(sinonimo)
                    except:
                        contador_errores = contador_errores +1
                        print (contador_errores,"Error en:", palabra)
            
print (contador_errores, "/", contador_palabras)

# Corregir pena , formas con "a", erratas como "ángel" 

guardado_diccionario_json=open ("diccionario_sin_etiquetas_con_conjugaciones_sinonimos.json", "w", encoding="utf-8")   
 
json.dump(diccionario_json, guardado_diccionario_json, ensure_ascii=False, indent=4)

guardado_diccionario_json.close()