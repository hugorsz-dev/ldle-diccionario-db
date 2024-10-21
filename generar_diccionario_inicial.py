#——————————————————————————————————————————————————
# Paquetes necesarios 
#
# Abrir archivos
from io import open; 
# Importar binarios
import pickle
# Exportar JSON
import json; 
# Ejecutar expresiones regulares
import re;
# Separar en sílabas
from separasilabas import  *
silabas = silabizer()
#__________________________________________________

#——————————————————————————————————————————————————
# Importación de archivos
#
archivo_definiciones=open ("definiciones", "rb")
#
definiciones = pickle.load(archivo_definiciones)
#
archivo_definiciones.close()
#__________________________________________________

"""
Separa la palabra en sílabas utilizando "sibilizador", esto será útil para separar la palabra en géneros masculino y femenino
"""
def silabizar (palabra):
    palabra = silabas(palabra)
    salida = []; 
    for letra in palabra: 
        salida.append(str(letra))

    return salida; 

"""
En base a una entrada "palabra, sufijo" devuelve el genero femenino y masculino de la palabra
"""
def multiGenero (texto):
    texto = texto.replace(" ", "")
    abreviatura = texto.split(",")[1]
    
    palabraMasculino = texto.split(",")[0]
    
    silabasPalabraMasculino = silabizar(palabraMasculino)
    palabraFemenino = "".join(silabasPalabraMasculino [0:(len(silabasPalabraMasculino)-1)])+abreviatura
    
    if abreviatura[0]==palabraMasculino[len(palabraMasculino)-1]:
        palabraFemenino= palabraMasculino[:-1]+abreviatura;
    
    # Abusón - abusóna 
    # Judío / ia -> not ío in palabraMasculino
    try:
        if "ó" in palabraFemenino[(len(palabraFemenino)-3):]\
        or "á" in palabraFemenino[(len(palabraFemenino)-3):]\
        or "é" in palabraFemenino[(len(palabraFemenino)-3):]\
        or "ú" in palabraFemenino[(len(palabraFemenino)-3):]:
            palabraFemenino=palabraFemenino[:(len(palabraFemenino)-3)]+ palabraFemenino[(len(palabraFemenino)-3):].replace("ó", "o").replace("á", "a").replace("é", "e").replace("ú", "u"); 
    except: 
        pass;   
    try:   
        if "ía" in palabraFemenino[-2:] or "ída" in palabraFemenino[-3:] or "ína" in palabraFemenino[-3:]:
            pass;
        else:
            palabraFemenino=palabraFemenino[:(len(palabraFemenino)-3)]+ palabraFemenino[(len(palabraFemenino)-3):].replace("í","i");  
    except: 
        pass; 
    """
    try:     
        if "í" in palabraMasculino[(len(palabraMasculino)-2):]:
            palabraFemenino=palabraFemenino[:(len(palabraFemenino)-3)]+ palabraFemenino[(len(palabraFemenino)-3):].replace("í", "i"); 
    except: 
        pass; 
    """
    # Muchacho - muchaccha
    
    if "ccha" in palabraFemenino:
        palabraFemenino = palabraFemenino.replace ("ccha", "cha")
        
    return {"m":palabraMasculino, "f":palabraFemenino}

"""
En base a una entrada "acomplexionado, da. bien" devolver:
- Forma verbal: "acomplexionado, da"
- Forma compleja: "bien acomplexionado, da"
"""

def multiCompuesta (texto):
    palabra = texto.split(".")[0];
    forma_compleja = texto.split(".")[1].replace(" ", "")+" "+palabra
    return {"palabra":palabra, "compuesta":forma_compleja}

"""
Estructura paginada de los datos, separados por letra (mayúscula o minúscula)
"""

diccionario_palabras = {
    "a": {}, "b": {}, "c": {}, "d": {}, "e": {}, "f": {}, "g": {}, "h": {}, "i": {},
    "j": {}, "k": {}, "l": {}, "m": {}, "n": {}, "ñ": {}, "o": {}, "p": {}, "q": {},
    "r": {}, "s": {}, "t": {}, "u": {}, "v": {}, "w": {}, "x": {}, "y": {}, "z": {},
    "A": {}, "B": {}, "C": {}, "D": {}, "E": {}, "F": {}, "G": {}, "H": {}, "I": {},
    "J": {}, "K": {}, "L": {}, "M": {}, "N": {}, "Ñ": {}, "O": {}, "P": {}, "Q": {},
    "R": {}, "S": {}, "T": {}, "U": {}, "V": {}, "W": {}, "X": {}, "Y": {}, "Z": {},
    "á": {}, "é": {}, "í": {}, "ó": {}, "ú": {}, "Á": {}, "É": {}, "Í": {}, "Ó": {}, 
    "Ú": {}, "-":{}
}

"""
Agrega la palabra al diccionario, verificando el género y creando una doble entrada si existe masculino y femenino
Verifica que una palabra no tenga varios significados, y si los contiene, asignarlos por orden dentro de un array

La inclusión de la palabra implica QUE: comprende todo lo que hay entre los primeros "[" y "]" 
y no tiene "*"

"""
def agregarPalabraDiccionario (palabra, origen, definicion, formas_compuestas, envios):
    
    """
    El procesamiento del nombre de cada palabra es importante, pues aporta información fundamental de la estructura del JSON
    """
    #ojo
    if "^" not in palabra and "," not in palabra and "." not in palabra:
        diccionario_palabras[palabra[0]][palabra] = [{"palabra": palabra, "origen":origen, "sinonimos":[], "definicion": definicion, "formas_compuestas":formas_compuestas, "envios":envios}]
    
    #amigo,ga
    if "," in palabra and "^" not in palabra and "." not in palabra:
        diccionario_palabras[palabra[0]][multiGenero(palabra)["m"]] = [{"palabra":palabra,"definicion": definicion, "origen":origen, "sinonimos":[], "formas_compuestas":formas_compuestas, "envios":envios}]
        #if multiGenero(palabra)["f"] not in diccionario_palabras[palabra[0]]:
        try:
            diccionario_palabras[palabra[0]][multiGenero(palabra)["f"]].append({"redir":multiGenero(palabra)["m"]});   
        except:
            diccionario_palabras[palabra[0]][multiGenero(palabra)["f"]] = [{"redir":multiGenero(palabra)["m"]}]   
       
    #cosa^1^
    if "^" in palabra and "," not in palabra and "." not in palabra:
        posicion = int(palabra[(palabra.find("^") + 1):(palabra.rfind("^"))])
        palabra = palabra[:(palabra.find("^"))];
            
        if posicion>1:
            diccionario_palabras[palabra[0].lower()][palabra.lower()].append({"palabra":palabra, "origen":origen, "sinonimos":[], "definicion": definicion, "formas_compuestas":formas_compuestas, "envios":envios})
        else:
            diccionario_palabras[palabra[0].lower()][palabra.lower()] = [{"palabra": palabra, "origen":origen, "sinonimos":[], "definicion": definicion, "formas_compuestas":formas_compuestas, "envios":envios}]
    
    #gato^1^, ta
    if "^" in palabra and "," in palabra and "." not in palabra:
        posicion = int(palabra[(palabra.find("^") + 1):(palabra.rfind("^"))])
        palabra = re.sub(r'[0-9^]', '', palabra) # quitar ^ y numeros
        if posicion>1:
            diccionario_palabras[palabra[0].lower()][multiGenero(palabra)["m"].lower()].append({"palabra":palabra, "origen":origen, "sinonimos":[], "definicion": definicion, "formas_compuestas":formas_compuestas, "envios":envios})
            # Agregado recientemente - si hay palabras en femenino precedentes, las introduce. Si no, las crea
            try: 
                diccionario_palabras[palabra[0].lower()][multiGenero(palabra)["f"].lower()].append({"redir":multiGenero(palabra)["m"]})
            except:
                diccionario_palabras[palabra[0].lower()][multiGenero(palabra)["f"].lower()] = [{"redir":multiGenero(palabra)["m"]}]  
        else: 
            diccionario_palabras[palabra[0].lower()][multiGenero(palabra)["m"].lower()] = [{"palabra":palabra, "origen":origen, "sinonimos":[], "definicion": definicion, "formas_compuestas":formas_compuestas, "envios":envios}]
            if multiGenero(palabra)["f"].lower() not in diccionario_palabras[palabra[0]]: diccionario_palabras[palabra[0].lower()][multiGenero(palabra)["f"].lower()] = [{"redir":multiGenero(palabra)["m"]}]   

    # bute. de
    if "^" not in palabra and "," not in palabra and "." in palabra:
        diccionario_palabras[multiCompuesta(palabra)["palabra"][0]][multiCompuesta(palabra)["palabra"]]= [{"palabra": multiCompuesta(palabra)["compuesta"], "origen":origen, "sinonimos":[], "definicion": definicion, "formas_compuestas":formas_compuestas, "envios":envios}]

    # acomplexionado, da. bien \~.
    if "^" not in palabra and "," in palabra and "." in palabra:
        diccionario_palabras[multiCompuesta(palabra)["palabra"][0]][multiGenero(multiCompuesta(palabra)["palabra"])["m"]] = [{"palabra":multiCompuesta(palabra)["compuesta"],"definicion": definicion, "origen":origen, "sinonimos":[], "formas_compuestas":formas_compuestas, "envios":envios}]
        if multiGenero(multiCompuesta(palabra)["palabra"])["f"] not in diccionario_palabras[palabra[0]]: diccionario_palabras[multiCompuesta(palabra)["palabra"][0]][multiGenero(multiCompuesta(palabra)["palabra"])["f"]] = [{"redir":multiGenero(palabra)["m"]}] 
    
    # Tato^2^. el
    if "^" in palabra and "," not in palabra and "."  in palabra:
        posicion = int(palabra[(palabra.find("^") + 1):(palabra.rfind("^"))])
        palabra = re.sub(r'[0-9^]', '', palabra) # quitar ^ y numeros
        if posicion>1:
            diccionario_palabras[multiCompuesta(palabra)["palabra"][0].lower()][multiCompuesta(palabra)["palabra"].lower()].append({"palabra": multiCompuesta(palabra)["compuesta"], "origen":origen, "sinonimos":[], "definicion": definicion, "formas_compuestas":formas_compuestas, "envios":envios}) 
        else: 
            diccionario_palabras[multiCompuesta(palabra)["palabra"][0].lower()][multiCompuesta(palabra)["palabra"].lower()]= [{"palabra": multiCompuesta(palabra)["compuesta"], "origen":origen, "sinonimos":[], "definicion": definicion, "formas_compuestas":formas_compuestas, "envios":envios}]


"""
Arroja las coincidencias de dos rangos
"""

def encontrar_rango(texto, patron_inicio, patron_fin):
    patron = re.compile(r'%s(.*?)%s' % (re.escape(patron_inicio), re.escape(patron_fin)), re.DOTALL)
    coincidencias = patron.findall(texto)
    return coincidencias

"""
Esta función se usa en este código para verificar la existencia de un rango determinado
"""

def encontrarPrimerRango (texto, patron_inicio, patron_fin):
    try:
        return encontrar_rango(texto, patron_inicio, patron_fin)[0]
    except: 
        return None

"""
Arroja la coincidencia en un rango
"""
def rangoDesdeHasta (texto, signoInicial, signoFinal=None):
    if signoFinal:
        posicionInicial = texto.find(signoInicial)
        posicionFinal = texto.find (signoFinal)
        return texto[(posicionInicial+1):(posicionFinal+1)].strip()
    else:    
        posicion = texto.find(signoInicial)
        return texto[:(posicion+1)].strip()

"""
BORRAR: Aplica la función strip a todos los elementos de un array
"""

def stripArray (array):
    nuevoArray = []
    for elemento in array:
        nuevoArray.append(elemento.strip())
    return nuevoArray

"""
BORRAR: Elimina ciertos caracteres del array
"""
def eliminarCaracteresArray (array, caracteres):
    salida = []
    for elemento in array:
        for caracter in caracteres: 
            elemento = elemento.replace(caracter, "")
        salida.append(elemento)
    return salida


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



"""
Recorrer el diccionario e introducir las palabras en sus registro_formas_compuestass
"""

for bloque in definiciones:
    
    palabra =""; # Donde se guardará la palabra
    
    origen =[]; # Donde se guardará el origen de la palabra, separado en líneas.
    limiteOrigen=None; # Donde se almacenará la distancia del origen para delimitar la fuente de la definición
    
    fuenteDefinicion= ""; # Aquello que va desde el origen hasta el final de la palabra
    
    definicion = []; # Las acepciones de la palabra
    
    envios = []; # Los envíos de la palabra delimitados por "[➤]" 
    
    fuenteFormasCompuestas = []; # La fuente a través de la que se conseguirán las formas compuestas, cada una con su respectiva definición independiente
    formas_compuestas = [] # Las formas compuestas procesadas
    
    # Extracción de la palabra [**PALABRA**], pues en todas las entradas son iguales. 
    
    try:
        palabra = encontrar_rango (bloque, "**", "**")[0].replace("*", "")
    except: 
        print ("Error en la extracción de la PALABRA en el siguiente bloque:")
        print (bloque)
        
    # Extracción del origen (), que se divide en [♦]
    
    # Para evitar posibilidades de error al encontrar el origen, spliteamos el bloque sin separadores
    
    bloqueCortado = bloque
    
    if "[■]" in bloque and "[➤]" in bloque:
        bloqueCortado = bloqueCortado.split("[■]") [0]    
    if "[■]" in bloque and "[➤]" not in bloque:
        bloqueCortado = bloqueCortado.split("[■]") [0]
    if "[■]"  not in bloque and "[➤]" in bloque:
        bloqueCortado = bloqueCortado.split("[➤]") [0]
        
    # Dado que esta cadena "([ǁ]{.extrafont3}" esta presente en algunas acepciones y también usa paréntesis, se usa como delimitador también 
    if "([ǁ]{.extrafont3}" in bloque: 
        bloqueCortado = bloqueCortado.split ("([ǁ]{.extrafont3}")[0]
    
    # Todas las formas en que puede aparecer el origen: 
    
    if (encontrarPrimerRango(bloqueCortado,"(", "*)")) \
    or (encontrarPrimerRango(bloqueCortado, "(", "')")) \
    or (encontrarPrimerRango(bloqueCortado, "(", "')")) \
    or (encontrarPrimerRango(bloqueCortado, "**]", ").")) \
    or (encontrarPrimerRango(bloqueCortado, "**]", "). m")) \
    or (encontrarPrimerRango(bloqueCortado, "**]", "). f")):
        origen = (rangoDesdeHasta(bloque, "]",")").split(". [♦]"))
        limiteOrigen= (len(encontrarPrimerRango(bloque, "[", "]"))+2 + len (rangoDesdeHasta(bloque, "]",")"))+2)
    
    # Extracción de las definiciones. 
    # La definición es aquello que se encuentra a partir del origen
    
    if limiteOrigen:
        fuenteDefinicion = bloque[limiteOrigen:].strip()
    else: 
        limitePalabra = len (encontrarPrimerRango(bloque, "[", "]"))+2;
        fuenteDefinicion =bloque [limitePalabra:].strip()
    
    # Cambiar los \~ por las palabras propiamente
    
    origen = [cadena.replace("\\~ ", re.sub(r'[0-9^]', '', palabra.replace (",", "‚")))+" " for cadena in origen]
    origen = [cadena.replace("\\~", re.sub(r'[0-9^]', '', palabra.replace (",", "‚")))+" " for cadena in origen]
    fuenteDefinicion = fuenteDefinicion.replace("\\~ ", re.sub(r'[0-9^]', '', palabra.replace (",", "‚")))
    fuenteDefinicion = fuenteDefinicion.replace("\\~", re.sub(r'[0-9^]', '', palabra.replace (",", "‚")))
    
    # fuenteDefinicion = fuenteDefinicion.replace("\\\\~", re.sub(r'[0-9^]', '', palabra.replace (",", "‚")))

    # OPCIONAL: Cambiar índices ascii a superíndices
    fuenteDefinicion = sustituirIndiceSuperIndice(fuenteDefinicion)
    
    # OPCIONAL: Cambiar las comillas dobles (confundibles con el formato JSON) por dobles simples
    fuenteDefinicion = fuenteDefinicion.replace ('"', "''" )

    # Extracción de acepciones:

    auxiliarFuenteDefinicion = fuenteDefinicion
    
    # Recoger definición íntegramente
    if "[■]" in bloque and "[➤]" in bloque:
        fuenteDefinicion = fuenteDefinicion.split("[■]") [0] 
    if "[■]" in bloque and "[➤]" not in bloque:
        fuenteDefinicion = fuenteDefinicion.split("[■]") [0]
    if "[■]"  not in bloque and "[➤]" in bloque:
        fuenteDefinicion = fuenteDefinicion.split("[➤]") [0]
    
    if "([ǁ]{.extrafont3}" in bloque: 
        fuenteDefinicion = fuenteDefinicion.replace ("([ǁ]{.extrafont3} ", "(")
    
    # Recoger formas compuestas y envíos
    
    if "[■]" in bloque and "[➤]" in bloque:
        try:
            fuenteFormasCompuestas = re.split(r'\[⚫\]|\[⚪\]|\[ǁ\]|\[☐\]', auxiliarFuenteDefinicion.split("[■]")[1].split("[➤]") [0].replace("\xa0",""))
            envios= auxiliarFuenteDefinicion.split("[➤]")[1].replace("'","").split(",")
        except:
            print ("PRIMER CASO")
            print ("ERROR EN:", fuenteDefinicion)
            print ("EN BLOQUE:", bloque)
            
        # ERRATAS EN ESTE CASO
        try: 
            if "{.sans}. f" in auxiliarFuenteDefinicion.split("[➤]")[1] \
            or "{.sans}. (" in auxiliarFuenteDefinicion.split("[➤]")[1] \
            or "{.sans}. m" in auxiliarFuenteDefinicion.split("[➤]")[1] \
            or "{.sans}. l" in auxiliarFuenteDefinicion.split("[➤]")[1]:
                print (auxiliarFuenteDefinicion.split("[➤]")[1]);
        except: 
            pass
    
    if "[■]" in bloque and "[➤]" not in bloque:
        try:
            fuenteFormasCompuestas = re.split(r'\[⚫\]|\[⚪\]|\[ǁ\]|\[☐\]', auxiliarFuenteDefinicion.split("[■]")[1].replace("\xa0",""))
        except:
            print ("SEGUNDO CASO")
            print ("ERROR EN:", fuenteDefinicion)
            print ("EN BLOQUE:", bloque)
            
    if "[■]"  not in bloque and "[➤]" in bloque:
        try:
            envios= auxiliarFuenteDefinicion.split("[➤]")[1].replace("'","").split(",")
        except:
            print ("TERCER CASO")
            print ("ERROR EN:", fuenteDefinicion)
            print ("EN BLOQUE:", bloque)
            
        # ERRATAS EN ESTE CASO
        try: 
            if "{.sans}. f" in auxiliarFuenteDefinicion.split("[➤]")[1] \
            or "{.sans}. (" in auxiliarFuenteDefinicion.split("[➤]")[1] \
            or "{.sans}. m" in auxiliarFuenteDefinicion.split("[➤]")[1] \
            or "{.sans}. l" in auxiliarFuenteDefinicion.split("[➤]")[1]:
                print (auxiliarFuenteDefinicion.split("[➤]")[1]);
        except: 
            pass
    
    if "{.sans-b}" in fuenteDefinicion \
    or "[⚪]" in bloque \
    or "[⚫]" in bloque: 
        definicion = re.split(r'\[⚫\]|\[⚪\]|\[ǁ\]', fuenteDefinicion)
    else: 
        definicion = fuenteDefinicion
    
    # Procesar las formas compuestas
    # ([cadena.replace("[", " ").replace("]","").strip().rsplit('{.sans}',1) for cadena in formas_compuestas]),
    
    empezar = False;
    registro_formas_compuestas = {"expresion": "", "significado":[]}
    
    for entrada in fuenteFormasCompuestas:         
        if "{.sans}" in entrada:   
            if empezar:
                formas_compuestas.append(registro_formas_compuestas)
                registro_formas_compuestas = {"expresion": "", "significado":[]}
            
            if len (entrada.rsplit("{.sans}",1)[1])>3:
                registro_formas_compuestas["expresion"] = entrada.rsplit("{.sans}",1)[0]
                registro_formas_compuestas["significado"].append (entrada.rsplit("{.sans}",1)[1])
            else:
                registro_formas_compuestas["expresion"] = entrada.split("{.sans}",1)[0]
                registro_formas_compuestas["significado"].append (entrada.split("{.sans}",1)[1])   
        else: 
            registro_formas_compuestas["significado"].append (entrada)
        
        # Ajustes estéticos 
        registro_formas_compuestas["significado"] = ([cadena.strip() for cadena in registro_formas_compuestas["significado"]])
        registro_formas_compuestas["significado"] = [cadena[1:] if cadena.startswith(".") else cadena for cadena in registro_formas_compuestas["significado"]]
               
        empezar = True;
        
        
    if registro_formas_compuestas["expresion"]!="":
        formas_compuestas.append(registro_formas_compuestas)
        

    # Introducir los datos
    
    agregarPalabraDiccionario(palabra,
                              stripArray(eliminarCaracteresArray(origen, "()[]")), 
                              definicion,
                              formas_compuestas,
                              stripArray([cadena.replace('*', '').replace("]", "").replace("[", "").replace(".","") for cadena in envios]));


with open("diccionario.json", "w", encoding="utf-8") as archivo:
    json.dump(diccionario_palabras, archivo, ensure_ascii=False)
        
print ("Diccionario inicial generado correctamente") 