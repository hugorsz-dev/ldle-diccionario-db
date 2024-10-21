# Abrir archivos
from io import open; 
from copy import deepcopy

# Multigénero
from generar_diccionario_inicial import multiGenero

print (multiGenero("amigo, ga"))

# Importar - exportar JSON
import json; 


# Importación de archivos
diccionario_archivo=open ("diccionario_sin_etiquetas_con_conjugaciones_sinonimos.json", "rb")
diccionario_json = json.load (diccionario_archivo)
diccionario_archivo.close()

output_diccionario_json = deepcopy(diccionario_json)
aux_redir ="";
for letra in diccionario_json:
    for palabra in diccionario_json[letra]:
        try:
            origen = diccionario_json[letra][palabra][0]["origen"]
            for apartado in origen:
                if "Tb." in apartado[:5] and "en acep" not in apartado:
                    apartado = apartado.replace("*", "").replace("{", "")
                    if "♦" in apartado: apartado = apartado.split("♦")[0]
                    apartado = apartado.split (".")[1]
                    if ";" in apartado:
                        if not "im-" in apartado: 
                            apartado = (apartado.replace (", p", "").replace(", Arg", "").replace (";",","));
                            for infra_apartado in apartado.split(","):
                                try:
                                    output_diccionario_json[infra_apartado.strip()[0]][infra_apartado.strip()] = {"redir":palabra}    
                                except:
                                    output_diccionario_json[infra_apartado.strip()[0]][infra_apartado.strip()].append( {"redir":palabra})    
                                    
                            #Cargar para mas adelante
                            aux_redir = infra_apartado.strip();
                    # Correcto
                    elif "- " in apartado:
                        # print (apartado.split("-")[0]+"-")
                        try:
                            output_diccionario_json[apartado.split("-")[0].strip()[0]][(apartado.split("-")[0]+"-").strip()].append({"redir":palabra})
                        except:
                            output_diccionario_json[apartado.split("-")[0].strip()[0]][(apartado.split("-")[0]+"-").strip()] = {"redir":palabra}

                        aux_redir = (apartado.split("-")[0]+"-").strip()
                    # Correcto
                    elif not "," in apartado:
                        # print (apartado) 
                        try:
                            output_diccionario_json[apartado.strip()[0]][apartado.strip()].append({"redir":palabra})
                        except:
                            output_diccionario_json[apartado.strip()[0]][apartado.strip()] = {"redir":palabra}

                        aux_redir = apartado.strip();
                    else:
                        if ", p" in apartado \
                        or ", Am" in apartado \
                        or ", Bol" in apartado \
                        or ", Méx" in apartado \
                        or ", desus" in apartado \
                        or "Cuba" in apartado \
                        or ", Ec" in apartado \
                        or ", Nic" in apartado \
                        or ", Col" in apartado \
                        or ", Ur" in apartado \
                        or ", Am" in apartado \
                        or ", Ven" in apartado \
                        or ", Ant" in apartado \
                        or ", Chile" in apartado \
                        or ", Guat" in apartado \
                        or ", Arg" in apartado \
                        or ", C" in apartado \
                        or ", Hond" in apartado:
                            try:
                                output_diccionario_json[apartado.split(",")[0].strip()[0]][apartado.split(",")[0].strip()].append({"redir":palabra}) 
                            except:
                                output_diccionario_json[apartado.split(",")[0].strip()[0]][apartado.split(",")[0].strip()] = {"redir":palabra}
                            aux_redir= apartado.split(",")[0].strip()
                            #print (apartado.split(",")[0].strip());
                        else:
                            for infra_apartado in apartado.split(","):
                                try:
                                    output_diccionario_json[infra_apartado.strip()[0]][infra_apartado.strip()].append({"redir":palabra})
                                except: 
                                    output_diccionario_json[infra_apartado.strip()[0]][infra_apartado.strip()] = {"redir":palabra}

                                aux_redir = infra_apartado.strip()
                                #print (infra_apartado.strip())
                    
                    # Añadir las redirecciones para palabras que contengan femenino. 
                    
                    if "," in diccionario_json[letra][palabra][0]["palabra"] and "-" not in diccionario_json[letra][palabra][0]:
                        aux_redir = aux_redir+", "+diccionario_json[letra][palabra][0]["palabra"].split(",")[1].strip()
                        try:
                            output_diccionario_json[multiGenero (aux_redir)["f"][0]][multiGenero (aux_redir)["f"]].append({"redir":palabra}) 
                        except:
                            output_diccionario_json[multiGenero (aux_redir)["f"][0]][multiGenero (aux_redir)["f"]] = {"redir":palabra}
        
        
        except:
            pass



output_diccionario_json["h"]["harmónica"] = [{"redir":"armónico"}]
output_diccionario_json["c"]["cualquier"] = [{"redir":"cualquiera"}]
output_diccionario_json["d"]["dómino"] = [{"redir":"dominó"}]
output_diccionario_json["s"]["sicológica"] = [{"redir":"psicológico"}]
output_diccionario_json["m"]["moka"] = [{"redir":"moca"}]
output_diccionario_json["Ó"]["Óscar"] = [{"redir":"óscar"}]
output_diccionario_json["p"]["pinnado"] = [{"redir":"pinado"}]
output_diccionario_json["p"]["polka"] = [{"redir":"polca"}]
output_diccionario_json["q"]["quiqui"] = [{"redir":"kiki"}]
output_diccionario_json["u"]["ultramaro"] = [{"redir":"ultramarino"}]
output_diccionario_json["-"]["-'aca"] = [{"redir":"-aco"}]

print (output_diccionario_json["a"]["afila"])
guardado_diccionario_json=open ("diccionario_sin_etiquetas_con_conjugaciones_sinonimos_y_redirecciones.json", "w", encoding="utf-8")   
 
json.dump(output_diccionario_json, guardado_diccionario_json, ensure_ascii=False, indent=4)
guardado_diccionario_json.close()
