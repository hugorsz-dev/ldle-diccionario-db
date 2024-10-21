# Abrir archivos
from io import open; 
# Importar - exportar JSON
import json; 
#
import re;

# Importación de archivos
diccionario_archivo=open ("diccionario_sin_etiquetas_con_conjugaciones_sinonimos_y_redirecciones.json", "rb")
diccionario_json = json.load (diccionario_archivo)
diccionario_archivo.close()

# Eliminar registros redundantes
for letra in diccionario_json:
    for palabra in diccionario_json[letra]:
        try:
            if diccionario_json[letra][palabra][0]["origen"] == [] \
            and diccionario_json[letra][palabra][0]["sinonimos"] == [] \
            and diccionario_json[letra][palabra][0]["formas_compuestas"] == [] \
            and diccionario_json[letra][palabra][0]["envios"] == [] \
            and isinstance(diccionario_json[letra][palabra][0]["definicion"], str) \
            and diccionario_json[letra][palabra][1]["redir"] in diccionario_json[letra][palabra][0]["definicion"]  \
            and len(diccionario_json[letra][palabra][0]["definicion"]) < 20:
               diccionario_json[letra][palabra].pop(0);
        except: 
            pass

# Corregir fallos de formato ** **
contador =0;
for letra in diccionario_json:
    for palabra in diccionario_json[letra]:
        try:
            sustitucion_bloque = []
            for bloque in diccionario_json[letra][palabra][0]["formas_compuestas"]:
                sustitucion_forma_compuesta = {"expresion":"","significado": [] }

                sustitucion_forma_compuesta["expresion"] = (re.sub(r'(\w+)\*\*', r'\1 **', bloque["expresion"])).replace(" **s", "**s").replace(" o **", " o ** ").replace("*","").replace(".]","")
                sustitucion_forma_compuesta["significado"]  = bloque["significado"]
                sustitucion_bloque.append(sustitucion_forma_compuesta)
                
            diccionario_json[letra][palabra][0]["formas_compuestas"] = sustitucion_bloque
        
        except:
            pass
        

# Corregir errores de disposición en algunas formas compuestas:   
for letra in diccionario_json:
    for palabra in diccionario_json[letra]:
        try:
            sustitucion_bloque = []
            for bloque in diccionario_json[letra][palabra][0]["formas_compuestas"]:
                sustitucion_forma_compuesta = {"expresion":"","significado": [] }

                if (len(bloque["expresion"])<10 or palabra in bloque["significado"][0] and not palabra+"*" in bloque["significado"][0] and not palabra+"s*" in bloque["significado"][0] ):
                    #
                    #print ((bloque["significado"][0])[indice_limite_significado+1:].replace("]","").strip())
                    sustitucion_forma_compuesta["expresion"] = bloque["expresion"] +" " + (bloque["significado"][0].split(".")[0]).replace("*","")
                    sustitucion_forma_compuesta["significado"] = bloque["significado"]
                    
                    indice_limite_significado = ((bloque["significado"][0]).index("."))
                    sustitucion_forma_compuesta["significado"][0] = (bloque["significado"][0])[indice_limite_significado+1:].replace("]","").strip()
                    
                    sustitucion_bloque.append(sustitucion_forma_compuesta)
                else:
                    sustitucion_forma_compuesta["expresion"] = bloque["expresion"]
                    sustitucion_forma_compuesta["significado"] = bloque["significado"]
                    sustitucion_bloque.append(sustitucion_forma_compuesta)
                    
            diccionario_json[letra][palabra][0]["formas_compuestas"] = sustitucion_bloque
        
        except:
            pass


 
# TODO: Si hay un "." en las expresiones, a partir de este las cogerá el primer término siguiente. 
# TODO: Un paréntesis ( debe terminer con otro ) y si es asi, concentrar en un solo registro
# TODO: Registros vacíos que deben desecharse. 
for letra in diccionario_json:
    for palabra in diccionario_json[letra]:
        try:
            sustitucion_bloque = []
            for bloque in diccionario_json[letra][palabra][0]["formas_compuestas"]:
                sustitucion_forma_compuesta = {"expresion":"","significado": [] }

                if "." in bloque["expresion"]:
                    indice_limite_expresion = ((bloque["expresion"]).index("."))
                    sustitucion_forma_compuesta["expresion"] =  (bloque["expresion"].split(".")[0])
                    print  (bloque["expresion"].split(".")[0])
                    print (bloque["expresion"][indice_limite_expresion+1:] + bloque["significado"][0])
                    sustitucion_forma_compuesta["significado"][0] = bloque["expresion"][indice_limite_expresion+1:] + bloque["significado"][0]
                    #sustitucion_forma_compuesta["expresion"] = sustitucion_forma_compuesta["expresion"].split(".")[0]
                    #sustitucion_forma_compuesta["significado"][0] = bloque["expresion"][indice_limite_expresion+1:]+bloque["significado"][0]
                    sustitucion_bloque.append(sustitucion_forma_compuesta)
                else:
                    sustitucion_forma_compuesta["expresion"] = bloque["expresion"]
                    sustitucion_forma_compuesta["significado"] = bloque["significado"]
                    sustitucion_bloque.append(sustitucion_forma_compuesta)
                    
            diccionario_json[letra][palabra][0]["formas_compuestas"] = sustitucion_bloque
        
        except:
            pass
 
print (diccionario_json["p"]["pie"])  
 
guardado_diccionario_json=open ("diccionario_sin_etiquetas_con_conjugaciones_sinonimos_redirecciones_sin_redundancias.json", "w", encoding="utf-8")   
 
json.dump(diccionario_json, guardado_diccionario_json, ensure_ascii=False, indent=4)

guardado_diccionario_json.close()  