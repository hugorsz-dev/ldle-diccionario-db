# Abrir archivos
from io import open; 
# Importar - exportar JSON
import json; 
from copy import deepcopy
# Importación de archivos
diccionario_archivo=open ("diccionario_sin_etiquetas.json", "rb")
diccionario_json = json.load (diccionario_archivo)
diccionario_archivo.close()

output_diccionario_json = deepcopy(diccionario_json)

# Verbos extra 

diccionario_json["a"]["abarse"][0]["formas_verbales"] = {
    "no-personales":{
        "infinitivo":"abarse"
        }, 
     "imperativo": {
            "tú/vos": "ábate/abate",
            "usted": "ábese",
            "vosotros/vosotras": "abaos",
            "ustedes": "ábense"
        }

    }

diccionario_json["r"]["renegociar"] = [{
    "palabra":"renegociar",
    "definicion": "tr. Tratar entre dos o más personas o instituciones sobre un acuerdo, convenio o contrato previamente adoptado con el propósito de modificarlo.",
    "origen":[],
    "sinonimos":[],
    "formas_compuestas":[]}]

diccionario_json["r"]["reimplantar"] = [{
    "palabra":"reimplantar",
    "definicion": "tr. Volver a imhttps://www.youtube.com/watch?v=mRfnVIBZIvQplantar.",
    "origen":[],
    "sinonimos":[],
    "formas_compuestas":[]}]

diccionario_json["r"]["refinanciar"] = [{
    "palabra":"refinanciar",
    "definicion": "tr. Financiar nuevamente una deuda revisando las condiciones previas por las que se regía.",
    "origen":[],
    "sinonimos":[],
    "formas_compuestas":[]}]

diccionario_json["r"]["referenciar"] = [{
    "palabra":"referenciar",
    "definicion": ["tr. Mencionar algo o a alguien.", "Tomar como referencia algo. U. t. c. prnl."],
    "origen":["De *referencia*"],
    "sinonimos":[],
    "formas_compuestas":[]}]
   
diccionario_json["i"]["interrelacionar"] = [{
    "palabra":"interrelacionar",
    "definicion": ["tr. Poner en interrelación personas, cosas o fenómenos.", "prnl. Tener interrelación personas, cosas o fenómenos."] ,
    "origen":[],
    "sinonimos":[],
    "formas_compuestas":[]}]
   
diccionario_json["c"]["clicar"] = [{
    "palabra":"clicar",
    "definicion": "intr. En informática, hacer clic en una zona interactiva de la pantalla.",
    "origen":["Del ingl. *to click*."],
    "sinonimos":[],
    "formas_compuestas":[]}]

diccionario_json["a"]["aperturar"] = [{
    "palabra":"aperturar",
    "definicion": "tr. Abrir algo, especialmente una cuenta bancaria.",
    "origen":["De *apertura*"],
    "sinonimos":[],
    "formas_compuestas":[]}]

diccionario_json["a"]["apalizar"] = [{
    "palabra":"apalizar",
    "definicion": "tr. Dar una paliza a alguien.",
    "origen":[],
    "sinonimos":[],
    "formas_compuestas":[]}]

diccionario_json["a"]["antagonizar"] = [{
    "palabra":"antagonizar",
    "definicion": ["intr. Ser antagonista.", "tr. Bioquím. Dicho de un compuesto: Disminuir la actividad de otro."],
    "origen":["Der. regres. de *antagonista*, a partir del gr. ἀνταγωνίζεσθαι *antagōnízesthai* 'luchar en contra', 'oponerse'."],
    "sinonimos":[],
    "formas_compuestas":[]}]

"""
VERBOS QUE FALTAN POR CONJUGAR - LIMTIACIONES DE LA LIBRERÍA
verbos_no_se_conjugan = [ "abarse", "abolir", "acaecer", "acontecer", "adir", "agredir", "amanecer", "anochecer", "apedrear", "arrecir", "asaborir", "atañer", "atardecer", "aterir", "aperturar", "apalizar", "antagonizar", "balbucir", "blandir", "cellisquear", "chaparrear", "chispear", "clarear", "clarecer", "colorir", "concernir", "clicar", "descolorir", "diluviar", "empedernir", "encelajarse", "fucilar", "garantir", "garuar", "gotear", "granizar", "harinear", "helar", "interrelacionar", "lloviznar", "manir", "marcear", "mayear", "mollinar", "mollir", "molliznar", "molliznear", "nevar", "neviscar", "obstar", "orvallar", "oscurecer", "pasar", "pintear", "preterir", "pringar", "refocilar", "relampaguear", "resultar", "suceder", "tardecer", "transgredir", "trapear", "tronar", "usucapir", "ventar", "ventear", "ventiscar", "ventisquear", "zaracear" ] 
"""

"""
verbos_archivo=open ("esp_verbos.json", "rb")
verbos_json = json.load (verbos_archivo)
verbos_archivo.close()
"""
"""
Extrae la lista de formas verbales que deben redirigir  al infinitivo del verbo en concreto
"""
"""

# En base al campo "verbo" introducir en un objeto llamado "verbos" dentro del JSON del diccionario cada una de las formas verbales
# Y cada una de las formas verbales deben ser introducidas también al diccionario, con un redir al infinitivo

# Que si una palabra conjugada ya existe (cosa -> coser) la añada como "segunda entrada" en el diccionario
# repuesto -> reponer (etc)     
print (diccionario_json["c"]["cosa"])

contador_errores =0;

for formas_verbales in verbos_json:
    try:
        diccionario_json[formas_verbales["verbo"][0]][formas_verbales["verbo"]][0]["formas_verbales"]=formas_verbales
        for forma_verbal in arrayFormasVerbales(formas_verbales):
            try:    
                diccionario_json[forma_verbal[0]][forma_verbal].append({"redir": formas_verbales["verbo"]})
            except:
                diccionario_json[forma_verbal[0]][forma_verbal] = [{"redir": formas_verbales["verbo"]}]
    except:
        # Añadir un "se" al final del verbo, algunos verbos están introducidos así. 
        try: 
            diccionario_json[formas_verbales["verbo"][0]][formas_verbales["verbo"]+"se"][0]["formas_verbales"]=formas_verbales
            for forma_verbal in arrayFormasVerbales(formas_verbales):
                try: 
                    diccionario_json[forma_verbal[0]][forma_verbal].append({"redir": formas_verbales["verbo"]+"se"})
                except:
                    diccionario_json[forma_verbal[0]][forma_verbal] = [{"redir": formas_verbales["verbo"]+"se"}]
        except:
            contador_errores = contador_errores+1; 
            print ("Error:", formas_verbales["verbo"])

print ("Errores totales:", contador_errores )
"""

# Método para crear los verbos

# Print the conjugation ensuring UTF-8 encoding
# https://github.com/Benedict-Carling/spanish-conjugator
# Solo debe ser llamado "Conjugator(language="es") una vez. 
from mlconjug3 import Conjugator
conjugator = Conjugator(language='es');

#test_verb = conjugator.conjugate("arrellanarse")
#print(test_verb.iterate());

def conjugar_verbo (infinitivo, tiempo, modo, persona):

    salida ="-";
    try: 
        verb = conjugator.conjugate(infinitivo)
        salida = verb[tiempo] [modo][persona]  
    except: 
        pass;
    return salida;

#print (conjugar_verbo(infinitivo, "Indicativo", "Indicativo presente", "yo"))

def conjugar_verbo_todas_personas (infinitivo, tiempo, modo):    
 
    if "Indicativo pretérito perfecto compuesto" in modo:
        salida = { 
            "yo": "he "+conjugar_verbo (infinitivo, tiempo, modo,'yo'),
            "tú/vos": "has "+conjugar_verbo (infinitivo, tiempo, modo,'tú'),
            "él/ella": "ha "+conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "usted": "ha "+conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "nosotros/nosotras": "hemos "+conjugar_verbo (infinitivo, tiempo, modo,'nosotros'),
            "vosotros/vosotras": "habéis "+conjugar_verbo (infinitivo, tiempo, modo,'vosotros'),
            "ustedes": "han "+conjugar_verbo (infinitivo, tiempo, modo,'ellos'),            
            "ellos/ellas": "han "+conjugar_verbo (infinitivo, tiempo, modo,'ellos'),
        }
    elif "Indicativo pretérito pluscuamperfecto" in modo:
        salida = {
            "yo": "había "+conjugar_verbo (infinitivo, tiempo, modo,'yo'),
            "tú/vos": "habías "+conjugar_verbo (infinitivo, tiempo, modo,'tú'),
            "él/ella": "había "+conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "usted": "había "+conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "nosotros/nosotras": "habíamos "+conjugar_verbo (infinitivo, tiempo, modo,'nosotros'),
            "vosotros/vosotras": "habíais "+conjugar_verbo (infinitivo, tiempo, modo,'vosotros'),
            "ustedes":  "habían "+conjugar_verbo (infinitivo, tiempo, modo,'ellos'),
            "ellos/ellas":  "habían "+conjugar_verbo (infinitivo, tiempo, modo,'ellos'),
        }
    elif "pretérito anterior" in modo:
        salida = {
            "yo": "hube "+conjugar_verbo (infinitivo, tiempo, modo,'yo'),
            "tú/vos": "hubiste "+conjugar_verbo (infinitivo, tiempo, modo,'tú'),
            "él/ella": "hubo "+conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "usted": "hubo "+conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "nosotros/nosotras": "hubimos "+conjugar_verbo (infinitivo, tiempo, modo,'nosotros'),
            "vosotros/vosotras": "hubisteis "+conjugar_verbo (infinitivo, tiempo, modo,'vosotros'),
            "ustedes":  "hubieron "+conjugar_verbo (infinitivo, tiempo, modo,'ellos'),            
            "ellos/ellas":  "hubieron "+conjugar_verbo (infinitivo, tiempo, modo,'ellos'),
        }
        
    elif "Indicativo futuro perfecto" in modo: 
        salida = {
            "yo": "habré "+conjugar_verbo (infinitivo, tiempo, modo,'yo'),
            "tú/vos": "habrás "+conjugar_verbo (infinitivo, tiempo, modo,'tú'),
            "él/ella": "habrá "+conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "usted": "habrá "+conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "nosotros/nosotras": "habremos "+conjugar_verbo (infinitivo, tiempo, modo,'nosotros'),
            "vosotros/vosotras": "habréis "+conjugar_verbo (infinitivo, tiempo, modo,'vosotros'),
            "ustedes":  "habrán "+conjugar_verbo (infinitivo, tiempo, modo,'ellos'),            
            "ellos/ellas":  "habrán "+conjugar_verbo (infinitivo, tiempo, modo,'ellos'),
        }
    elif "Condicional perfecto" in modo: 
        salida = {
            "yo": "habría "+conjugar_verbo (infinitivo, tiempo, modo,'yo'),
            "tú/vos": "habrías "+conjugar_verbo (infinitivo, tiempo, modo,'tú'),
            "él/ella": "habría "+conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "usted": "habría "+conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "nosotros/nosotras": "habríamos "+conjugar_verbo (infinitivo, tiempo, modo,'nosotros'),
            "vosotros/vosotras": "habríais "+conjugar_verbo (infinitivo, tiempo, modo,'vosotros'),
            "ustedes":  "habrían "+conjugar_verbo (infinitivo, tiempo, modo,'ellos'),            
            "ellos/ellas":  "habrían "+conjugar_verbo (infinitivo, tiempo, modo,'ellos'),
        }
    elif "Subjuntivo pretérito perfecto" in modo: 
        salida = {
            "yo": "haya "+conjugar_verbo (infinitivo, tiempo, modo,'yo'),
            "tú/vos": "hayas "+conjugar_verbo (infinitivo, tiempo, modo,'tú'),
            "él/ella": "haya "+conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "usted": "haya "+conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "nosotros/nosotras": "hayamos "+conjugar_verbo (infinitivo, tiempo, modo,'nosotros'),
            "vosotros/vosotras": "hayáis "+conjugar_verbo (infinitivo, tiempo, modo,'vosotros'),
            "ustedes":  "hayan "+conjugar_verbo (infinitivo, tiempo, modo,'ellos'),            
            "ellos/ellas":  "hayan "+conjugar_verbo (infinitivo, tiempo, modo,'ellos'),
        }
    elif "Subjuntivo pretérito imperfecto 1" in modo: 
        salida = {
            "yo": conjugar_verbo (infinitivo, tiempo, modo,'yo')+" o "+conjugar_verbo (infinitivo, tiempo, "Subjuntivo pretérito imperfecto 2",'yo'),
            "tú/vos": conjugar_verbo (infinitivo, tiempo, modo,'tú')+" o "+conjugar_verbo (infinitivo, tiempo, "Subjuntivo pretérito imperfecto 2",'tú'),
            "él/ella": conjugar_verbo (infinitivo, tiempo, modo,'él')+" o "+conjugar_verbo (infinitivo, tiempo, "Subjuntivo pretérito imperfecto 2",'él'),
            "usted": conjugar_verbo (infinitivo, tiempo, modo,'él')+" o "+conjugar_verbo (infinitivo, tiempo, "Subjuntivo pretérito imperfecto 2",'él'),
            "nosotros/nosotras": conjugar_verbo (infinitivo, tiempo, modo,'nosotros')+" o "+conjugar_verbo (infinitivo, tiempo, "Subjuntivo pretérito imperfecto 2",'nosotros'),
            "vosotros/vosotras": conjugar_verbo (infinitivo, tiempo, modo,'vosotros')+" o "+conjugar_verbo (infinitivo, tiempo, "Subjuntivo pretérito imperfecto 2",'vosotros'),
            "ustedes":  conjugar_verbo (infinitivo, tiempo, modo,'ellos')+" o "+conjugar_verbo (infinitivo, tiempo, "Subjuntivo pretérito imperfecto 2",'ellos'),            
            "ellos/ellas": conjugar_verbo (infinitivo, tiempo, modo,'ellos')+" o "+conjugar_verbo (infinitivo, tiempo, "Subjuntivo pretérito imperfecto 2",'ellos'),
        }
    elif "Subjuntivo pretérito pluscuamperfecto 1" in modo: 
        salida = {
            "yo": "hubiera o hubiese "+conjugar_verbo (infinitivo, tiempo, modo,'yo'),
            "tú/vos": "hubieras o hubieses "+conjugar_verbo (infinitivo, tiempo, modo,'tú'),
            "él/ella": "hubiera o hubiese "+conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "usted": "hubiera o hubiese "+conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "nosotros/nosotras": "hubiéramos o hubiésemos "+conjugar_verbo (infinitivo, tiempo, modo,'nosotros'),
            "vosotros/vosotras": "hubierais o hubieseis "+conjugar_verbo (infinitivo, tiempo, modo,'vosotros'),
            "ustedes":  "hubieran o hubiesen "+conjugar_verbo (infinitivo, tiempo, modo,'ellos'),
            "ellos/ellas": "hubieran o hubiesen "+conjugar_verbo (infinitivo, tiempo, modo,'ellos')
        }
    elif "Subjuntivo futuro perfecto" in modo: 
        salida = {
            "yo": "hubiere "+conjugar_verbo (infinitivo, tiempo, modo,'yo'),
            "tú/vos": "hubieres "+conjugar_verbo (infinitivo, tiempo, modo,'tú'),
            "él/ella": "hubiere "+conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "usted": "hubiere "+conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "nosotros/nosotras": "hubiéremos "+conjugar_verbo (infinitivo, tiempo, modo,'nosotros'),
            "vosotros/vosotras": "hubiereis "+conjugar_verbo (infinitivo, tiempo, modo,'vosotros'),
            "ustedes":  "hubieren "+conjugar_verbo (infinitivo, tiempo, modo,'ellos'),            
            "ellos/ellas":  "hubieren "+conjugar_verbo (infinitivo, tiempo, modo,'ellos'),
        }
    elif not "Imperativo" in modo:
        salida = {
            "yo": conjugar_verbo (infinitivo, tiempo, modo,'yo'),
            "tú/vos": conjugar_verbo (infinitivo, tiempo, modo,'tú'),
            "él/ella": conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "usted": conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "nosotros/nosotras": conjugar_verbo (infinitivo, tiempo, modo,'nosotros'),
            "vosotros/vosotras": conjugar_verbo (infinitivo, tiempo, modo,'vosotros'),
            "ustedes":  conjugar_verbo (infinitivo, tiempo, modo,'ellos'),
            "ellos/ellas":  conjugar_verbo (infinitivo, tiempo, modo,'ellos'),
        }

    else:
        
        conjugacion = infinitivo[len(infinitivo)-2:];
        
        vos = conjugar_verbo (infinitivo, tiempo, modo,'tú');
        if conjugacion == "ir":
            vos = vos[:len(vos)-1]+"í"
        elif conjugacion == "er":
            vos = vos[:len(vos)-1]+"é"
        elif conjugacion == "ar":
            vos = vos[:len(vos)-1]+"á"
        
        salida = { 
            "tú/vos": conjugar_verbo (infinitivo, tiempo, modo,'tú') + "/" + vos,
            "usted": conjugar_verbo (infinitivo, tiempo, modo,'él'),
            "vosotros/vosotras": conjugar_verbo (infinitivo, tiempo, modo,'vosotros'),
            "nosotros/nosotras": conjugar_verbo (infinitivo, tiempo, modo,'nosotros'),
            "ustedes": conjugar_verbo (infinitivo, tiempo, modo,'ellos'),
        }
        
    return salida;
   


def formas_no_personales_vebo (infinitivo):
    verb = conjugator.conjugate(infinitivo);
    salida = {};
    salida ["infinitivo"] = infinitivo;
    salida ["participio"] = verb["Participo"] ["Participo Participo"];
    
    if infinitivo[-2:] != "se":
        salida ["infinitivo-compuesto"] = "haber "+ verb["Participo"] ["Participo Participo"];
        salida ["gerundio"] = verb["Gerundio"] ["Gerundio Gerondio"][""]
        salida ["gerundio-compuesto"] ="habiendo "+verb["Participo"] ["Participo Participo"]
    else:
        salida ["infinitivo-compuesto"] = "haberse "+ verb["Participo"] ["Participo Participo"];
        salida ["gerundio-compuesto"] ="habiéndose "+verb["Participo"] ["Participo Participo"]
        
        # Verificar si es "ar" o es "er " o "ir"
        
        if infinitivo[:-2][-2:] =="ar": 
            salida ["gerundio"] = infinitivo [:-4] +"ándose"
        else:
            salida ["gerundio"] = infinitivo [:-4] +"iéndose"
        
        #"iéndose"
        
    """
    salida = {
        "infinitivo": infinitivo,
        "infinitivo-compuesto": "haber "+ verb["Participo"] ["Participo Participo"],
        "gerundio": verb["Gerundio"] ["Gerundio Gerondio"][""], 
        "gerundio-compuesto": "habiendo "+verb["Participo"] ["Participo Participo"], 
        "participio": verb["Participo"] ["Participo Participo"]
    }
    """
    return salida;
    
# Indicativo
# Presente 

def json_verbo_conjugado (infinitivo):

    conjugacion = {
                "no-personales": formas_no_personales_vebo (infinitivo),
                "indicativo":{
                    "presente": conjugar_verbo_todas_personas (infinitivo, "Indicativo", "Indicativo presente"),
                    "pretérito perfecto simple": conjugar_verbo_todas_personas (infinitivo, "Indicativo", "Indicativo pretérito perfecto simple"),
                    "pretérito perfecto compuesto": conjugar_verbo_todas_personas (infinitivo, "Indicativo", "Indicativo pretérito perfecto compuesto"),
                    "pretérito imperfecto": conjugar_verbo_todas_personas (infinitivo, "Indicativo", "Indicativo pretérito imperfecto"),
                    "pretérito pluscuamperfecto": conjugar_verbo_todas_personas (infinitivo, "Indicativo", "Indicativo pretérito pluscuamperfecto"),
                    "pretérito perfecto simple": conjugar_verbo_todas_personas (infinitivo, "Indicativo", "Indicativo pretérito perfecto simple"),
                    "pretérito anterior": conjugar_verbo_todas_personas (infinitivo, "Indicativo", "Indicativo pretérito anterior"),
                    "futuro simple": conjugar_verbo_todas_personas (infinitivo, "Indicativo", "Indicativo futuro"),
                    "futuro compuesto": conjugar_verbo_todas_personas (infinitivo, "Indicativo", "Indicativo futuro perfecto"),
                    "condicional simple": conjugar_verbo_todas_personas (infinitivo, "Condicional", "Condicional Condicional"),
                    "condicional compuesto": conjugar_verbo_todas_personas (infinitivo, "Condicional", "Condicional perfecto")
                },
                "subjuntivo":{
                    "presente": conjugar_verbo_todas_personas (infinitivo, "Subjuntivo", "Subjuntivo presente"),
                    "pretérito perfecto compuesto": conjugar_verbo_todas_personas (infinitivo, "Subjuntivo", "Subjuntivo pretérito perfecto"),
                    "pretérito imperfecto": conjugar_verbo_todas_personas (infinitivo, "Subjuntivo", "Subjuntivo pretérito imperfecto 1"),
                    "pretérito pluscuamperfecto": conjugar_verbo_todas_personas (infinitivo, "Subjuntivo", "Subjuntivo pretérito pluscuamperfecto 1"),
                    "futuro simple": conjugar_verbo_todas_personas (infinitivo, "Subjuntivo", "Subjuntivo futuro"),
                    "futuro compuesto": conjugar_verbo_todas_personas (infinitivo, "Subjuntivo", "Subjuntivo futuro perfecto"),
                },
                "imperativo":conjugar_verbo_todas_personas (infinitivo, "Imperativo", "Imperativo Afirmativo"),
    }
    
    return conjugacion; 

def arrayFormasVerbales (objeto_verbo):
    salida = []; 
    for modo in objeto_verbo:
        if modo =="no-personales" or modo =="imperativo":
            for tiempo in objeto_verbo[modo]:

                if "modo" != "infinitivo": 
                    forma = objeto_verbo[modo][tiempo]
                    if " " in forma:
                        forma = forma.split(" ")[1];
                        salida.append(forma)
                    elif "/" in forma:
                        forma = forma.split("/");
                        salida.append(forma[0])
                        salida.append(forma[1])
                    else: 
                        salida.append(forma)
           
        else: 
            for tiempo in objeto_verbo[modo]:
                for persona in objeto_verbo[modo][tiempo]:
             
                    forma = objeto_verbo[modo][tiempo][persona];
                    if " " in forma:
                        forma = forma.split(" ");
                        if len(forma) == 2:
                            salida.append(forma[1]);
                        elif len(forma) == 3:
                            salida.append(forma[0])
                            salida.append(forma[2])
                        elif len(forma) == 4:
                            salida.append(forma[3])
                    else: 
                        salida.append(forma)
                   
    return list(set(salida))

for letra in diccionario_json:
    for palabra in diccionario_json[letra]:
        es_verbo=False;
        try: 
            definicion = diccionario_json[letra][palabra][0]["definicion"]
            if isinstance (definicion, list):
                for acepcion in definicion: 
                    if "intr." in acepcion \
                    or "tr." in acepcion \
                    or "prnl." in acepcion \
                    or "copulat." in acepcion:
                        es_verbo = True; 
            else:
                if "intr." in definicion \
                    or "tr." in definicion \
                    or "prnl." in definicion \
                    or "copulat." in definicion:
                        es_verbo = True; 
        except:
            pass;
        
        if es_verbo:
            try:
                formas_verbales = json_verbo_conjugado(palabra);
                output_diccionario_json[letra][palabra][0]["formas_verbales"] =formas_verbales;
                for forma_verbal in arrayFormasVerbales(formas_verbales):
                    try:    
                        if forma_verbal!=palabra: output_diccionario_json[forma_verbal[0]][forma_verbal].append({"redir": palabra})
                    except:
                        if forma_verbal!=palabra: output_diccionario_json[forma_verbal[0]][forma_verbal] = [{"redir": palabra}]
            except:
                print ("Error al conjugar el verbo",palabra)


"""
guardado_diccionario_json=open ("diccionario_sin_etiquetas_con_conjugaciones.json", "w", encoding="utf-8")   
 
json.dump(diccionario_json, guardado_diccionario_json, ensure_ascii=False, indent=4)
guardado_diccionario_json.close()

"""

guardado_diccionario_json=open ("diccionario_sin_etiquetas_con_conjugaciones.json", "w", encoding="utf-8")    
json.dump(output_diccionario_json, guardado_diccionario_json, ensure_ascii=False, indent=4)
guardado_diccionario_json.close()
print ("Guardado completo")
