# Abrir archivos
from io import open; 
# Importar - exportar JSON
import json; 

# Importación de archivos

# Búsqueda de verbos en femenino

"""
PENDIENTE DE AGREGAR

[**presupuestario, ria**] adj. Perteneciente o relativo al
presupuesto, especialmente al de un Estado. m.
[1.]{.sans-b} Motivo, causa o pretexto con que se ejecuta algo.
[ǁ]{.extrafont3} [2.]{.sans-b} Supuesto o suposición. [ǁ]{.extrafont3}
[3.]{.sans-b} Cómputo anticipado del coste de una obra o de los gastos y
rentas de una corporación. [ǁ]{.extrafont3} [4.]{.sans-b} Cantidad de
dinero calculado para hacer frente a los gastos generales de la vida
cotidiana, de un viaje, etc. [ǁ]{.extrafont3} [5.]{.sans-b} desus.
Propósito formado por el entendimiento y aceptado por la voluntad.
[■]{.extrafont3} \~ [**que**]{.sans}. loc. conjunt. [**supuesto
que**]{.sans}. [➤]{.extrafont3} [**crédito \~ , déficit \~. presupuesto**]{.sans}.

(incrustar_redir.py - faltan 1900 términos por agregar !! )
"""



print("""
////////////////////////////////////
// _         ____   _      _____  //
//| |     _ |  _ \ | |    | ____| //
//| |    (_)| | | || |    |  _|   //
//| |___    | |_| || |___ | |___  //
//|_____|   |____/ |_____||_____| //
////////////////////////////////////
""")
print ("Li·DRAE - Consulta a la base de datos")

print ("Cargando ficheros JSON . . .")

diccionario_archivo=open ("diccionario_sin_etiquetas_con_conjugaciones_sinonimos_redirecciones_sin_redundancias.json", "rb")
diccionario_json = json.load (diccionario_archivo)
diccionario_archivo.close()

print (". . . Ficheros JSON cargados correctamente.")

while True:
    try:
        palabra = input("<ldle> ")
        if palabra =="exit()":
            break;
        print (json.dumps(diccionario_json[palabra[0]][palabra], indent=4,  ensure_ascii=False))
    except:
        print ("<error> No encontrado:", palabra+".")