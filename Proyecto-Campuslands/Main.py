##Primer archivo de prueba
import json
con = open("DATA/campers.json")
campersJS = json.load(con)

conec = open("DATA/gente.json")
genteJS = json.load(conec)

conecta = open("DATA/notas.json")
notasJS = json.load(conecta)

conlos = open("DATA/Roles.json")
rolesJS = json.load(conlos)

conjsons = open("DATA/salas.json")
salasJS = json.load(conjsons)

us_trainer=rolesJS["Campuslands"]["Trainer"]
salo_trainers=salasJS["salas"]
us_camper=campersJS["grados"]
us_coordinacion=rolesJS["Campuslands"]["Coordinacion"]

#Ingresar usuario:
quien=str(input("Quien desea ingresar?(No uses tildes o puntos)\n"))

#         Trainer:

if quien == "Trainer" or quien == "trainer":
    identificacion=input("Pon tu nombre: \n")

    if any(usuario["nombres"] == identificacion for usuario in us_trainer):
        if True:
            hacer_trainer=int(input("Selecciona un número:\n 1. Ver grupo(s)\n 2. Ver salas y horarios\n"))
            
            if hacer_trainer == 1:
                grupos = [grupo["Grupos"] for grupo in us_trainer if grupo["nombres"] == identificacion]
                if grupos:
                    print("Tus grupos son:")
                    for gru in grupos:
                        print({gru})
                else:
                    print("No hay grupos asignados.")

            elif hacer_trainer==2:##No se pq pero no me esta funcionando y me detuvo el codigo, lo arreglo "mañana"
                trainer_salones=[]
                for salon, clase in salo_trainers.items():
                    for clases in clase:
                        for nom_salon, info in clases.items():
                            if info.get("trainer")==identificacion:
                                trainer_salones.append((salon,info["hora"]))
                if trainer_salones:
                    for sala,hora in trainer_salones:
                        print(f"Salon:{sala}, Hora:{hora}")
                else:
                    print("No hay hora o salon asignado.")
                
    else:
        print("Identificación incorrecta para un Trainer.")

##-------------Pon aqui lo de campers------------------------------------##

if quien == "Camper" or quien == "camper":
    print("Pon tu grupo: \nGrupos disponibles: ")
    for i in range(len(us_camper)):
        print(us_camper[i])
        i=i+1
    grupo=str(input(""))
    if any(usuario["nombres"] == grupo for usuario in us_camper):
        identificacion=input("Pon tu ID de camper: \n")
        if any(usuario["id"] == identificacion for usuario in us_camper[grupo]):
            if True:
                hacer_camp=int(input("Selecciona un número: \n 1. Ver notas\n 2. Ver estado \n 3. Retirarse"))
                if hacer_camp==1:
                    for i in range(len(us_camper)):
                        notas = [notasJS for notas in us_camper[i] if notasJS == identificacion]
    else:
        print("Grupo no disponible")

##-----------------------Inicio de coordinación--------------------------##
if quien=="Coordinacion" or quien=="coordinacion":
    hacer_cordi=int(input("Selecciona un número: \n 1. Editar/ver notas\n 2. Cambiar Estado \n 3. Crear rutas\n 4. Asignar"))##Aún no termine de escribir el menú, me distraje con la corrección del trainer jsjaja
