#!/bin/bash
# Dependencias de mlconjug3, un conjugador de verbos. 
pip install scikit-learn==1.3.0;
pip install pyyaml;
pip install joblib;
pip install defusedxml;
pip install scikit-learn;

# Separa soloDefinicionesSinLema.md -> definiciones (archivo binario separado por líneas)
python exportarDiccionario.py;
# Realiza una clasificación general de las palabras en bruto, asigna redirecciones al genero femenino. 
python generar_diccionario_inicial.py; 
# Elimina las etiquetas de formato EBUP
python eliminar_etiquetas.py; 
# Conjuga los verbos usando mlconjug3
python incrustar_verbos.py;
# Incrusta los sinónimos de sinonimos.json
python incrustar_sinonimos.py; 
# Las palabras explícitamente indicadas como redirecciones obtienen registros de redirección. 
python incrustar_redir.py; 
# Elimina registros redundantes, ya repetidos porque hay dos palabras iguales. 
python eliminar_registros_redundantes.py;
