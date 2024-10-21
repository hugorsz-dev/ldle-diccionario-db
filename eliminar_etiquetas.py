# Sustituir cadenas de etiqueta (opcional) 



"""
SOLUCIONAR TEMA DEL "\"
"""

from io import open; 
archivo_diccionario_json = open ("diccionario.json", "r");
diccionario_json = archivo_diccionario_json.readlines()[0]; 


diccionario_json = diccionario_json.replace ("{.extrafont3} ", "")
diccionario_json = diccionario_json.replace ("{extrafont3} ", "")
diccionario_json = diccionario_json.replace ("{.sans-b} ", "")
diccionario_json = diccionario_json.replace ("{.sans-b}.", "")
diccionario_json = diccionario_json.replace ("{.sans-b}", "")
diccionario_json = diccionario_json.replace ("{.extrafont-it}", "")
diccionario_json = diccionario_json.replace ("{.extrafont}", "")
diccionario_json = diccionario_json.replace ("{.sans}", "")
diccionario_json = diccionario_json.replace ("{sans}", "")
diccionario_json = diccionario_json.replace ("[ǁ]", "")
diccionario_json = diccionario_json.replace ("[**", "**")# diccionario_json = diccionario_json.replace ("[**", " **") 
diccionario_json = diccionario_json.replace ("**]", "**")
diccionario_json = diccionario_json.replace ("\\", "")


for i in range(64):
    cadena = "["+str(i+1)+".]"
    diccionario_json = diccionario_json.replace(cadena,"")

for i in range(64):
    cadena = "["+str(i+1)+"]"
    diccionario_json = diccionario_json.replace(cadena,"")

#⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹
def numeroASuperindice (numero):
    if numero == "0": return "⁰";
    elif numero == "1": return "¹";
    elif numero == "2": return "²";
    elif numero == "3": return "³";
    elif numero == "4": return "⁴";
    elif numero == "5": return "⁵";
    elif numero == "6": return "⁶";
    elif numero == "7": return "⁷";
    elif numero == "8": return "⁸";
    elif numero == "9": return "⁹";
    elif numero == "−": return "⁻"
    elif numero == "+": return "+"
    elif numero == "n": return "ⁿ"
    elif numero == "x": return "x"
  
def sustituirIndiceSuperIndice (cadena):
    
    cadena = list(cadena)
    recoger = False;
    
    for i in range(len(cadena)): 
        
        if recoger == True and cadena[i]!="^": 
            cadena[i] = numeroASuperindice(cadena[i])
     
        if cadena[i] =="^": 
            if recoger == True: recoger = False;
            elif recoger == False: recoger = True;
    cadena = ''.join(cadena)  
    return cadena.replace("^", "");

diccionario_json = sustituirIndiceSuperIndice(str(diccionario_json))    

guardado_diccionario_json=open ("diccionario_sin_etiquetas.json", "w", encoding="utf-8")   
guardado_diccionario_json.write (diccionario_json)

print ("Fin de la eliminación")