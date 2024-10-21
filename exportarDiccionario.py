import pickle;
import re
from io import open; 

def encontrar_rango(texto, patron_inicio, patron_fin):
    # Crear patrón de búsqueda
    patron = re.compile(r'%s(.*?)%s' % (re.escape(patron_inicio), re.escape(patron_fin)), re.DOTALL)
    # Encontrar todas las coincidencias
    coincidencias = patron.findall(texto)
    return coincidencias

definiciones = open ("soloDefinicionesSinLema.md", "r");

arrayDefinicionesDesordenadas = definiciones.readlines(); 

"""
- Juntar cada bloque de definición en un unico array, teniendo en cuenta que están separados y que su separación debe ir seguida de un (" ") 
- Eliminar los espacios.

El archivo limpio de definiciones se cargará en el array de definicionesOrdenadas
"""

definicionesOrdenadas = []
contador =0;
definicion ="";

for segmentoSeparado in arrayDefinicionesDesordenadas:
    definicion = definicion + segmentoSeparado+" ";
    if segmentoSeparado=="\n":
        definicionesOrdenadas.append(definicion.replace("\n", ""))
        definicion =""

# Puesto que la ultima definicion no tiene salto de línea, debe integrarse fuera del bucle.
definicionesOrdenadas.append (arrayDefinicionesDesordenadas[len (arrayDefinicionesDesordenadas)-1])

# Limpiar registros erróneos
indices_a_eliminar = []

# Registros basura 

for indice, bloque in enumerate(definicionesOrdenadas):
    try:
        palabra = encontrar_rango(bloque, "[**", "**]")[0]     
    except: 
        try:
            contador = contador+1;     
            if bloque[0]!="[" and bloque[1]!="*" or "#" in bloque:    
                indices_a_eliminar.append(indice)
                print ("Eliminar índice", indice)
        except: 
            indices_a_eliminar.append(indice)
             
for indice in sorted(indices_a_eliminar, reverse=True):
    definicionesOrdenadas.pop(indice)
    print("Eliminado índice", indice)      

print ("-----------------------")

# Formas redundantes
indices_a_eliminar = []
contador=0; 

for indice, bloque in enumerate(definicionesOrdenadas):
    if "..." in bloque and "\\" in bloque and "V." in bloque:
        indices_a_eliminar.append(indice)
        print (bloque)
        print ("Eliminar índice", indice)
        
for indice in sorted(indices_a_eliminar, reverse=True):
    definicionesOrdenadas.pop(indice)
    print("Eliminado índice", indice)  
    


# Guardado del archivo para conservarlo 

guardadoDiccionario=open ("definiciones", "wb")      
pickle.dump(definicionesOrdenadas,guardadoDiccionario)
guardadoDiccionario.close();
