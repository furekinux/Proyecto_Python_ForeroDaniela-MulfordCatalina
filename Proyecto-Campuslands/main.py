##Primer archivo de prueba
import json
con = open("DATA/campers.json")
campersJS = json.load(con)

conec = open("DATA/gente.json")
genteJS = json.load(conec)

conecta = open("DATA/notas.json")
notasJS = json.load(conecta)

conlos = open("DATA/roles.json")
rolesJS = json.load(conlos)

conjsons = open("DATA/salas.json")
salasJS = json.load(conjsons)

us_trainer=rolesJS["Campuslands"]["Trainer"]
salo_trainers=salasJS["salas"]
estado_cursando=campersJS["grados"]
us_camper=campersJS["grados"]
us_coordinacion=rolesJS["Campuslands"]["Coordinacion"]

#Ingresar usuario:
quien=str(input("Quien desea ingresar?(Trainer,Coordinación)(No uses tildes o puntos)\n"))

#         Trainer:

if quien == "Trainer" or quien == "trainer":
    identificacion=int(input("Pon tu identificación: \n"))

    if any(int(usuario["id"]) == identificacion for usuario in us_trainer):
        if True:
            hacer_trainer=int(input("Selecciona un número:\n 1. Ver grupo(s)\n 2. Ver salas y horarios\n"))
            
            if hacer_trainer == 1:
                grupos = [grupo["Grupos"] for grupo in us_trainer if grupo["id"] == identificacion]
                if grupos:
                    print("Tus grupos son:")
                    for gru in grupos:
                        print({gru})
                else:
                    print("No hay grupos asignados.")

            elif hacer_trainer==2:
                trainer_salones = []
                for salon_nombre, clases in salo_trainers.items():
                    for clase in clases:
                        for nombre_clase, info in clase.items():
                            if info.get("id") == identificacion:
                                trainer_salones.append({salon_nombre: info})
                
                if trainer_salones:
                    print("Tu horario es:")
                    for sala in trainer_salones:
                        print(sala)
                else:
                    print("No tienes salas asignadas.")

                
    else:
        print("Identificación incorrecta para un Trainer.")

    
    ##-----------------------Inicio de coordinación--------------------------##
elif quien=="Coordinacion" or quien=="coordinacion":
    hacer_cordi=int(input("Selecciona un número: \n 1. Editar/ver notas\n 2. Estado \n 3. Crear rutas\n 4. Asignar\n"))##Aún no termine de escribir el menú, me distraje con la corrección del trainer jsjaja
    if hacer_cordi==1:
        menu_notas=input("Deseas:\n 1. Ver notas salon.\n 2. Ver notas estudiante.\n 3. Poner nota.\n 4. Quitar nota.\n")
        print("notasJS")##Lo de dani y su función :)

    elif hacer_cordi==2:#Estado
        menu_estado=int(input("Deseas:\n 1. Buscar personas por estado.\n 2. Ver estado de un estudiante.\n 3. Editar estado.\n"))
        #Todos los de un mismo estado
        
        if menu_estado==1:
            opcion1=str(input("Que estado deseas buscar?(Ingreso, Inscrito, Aprobado,Cursando, Graduado, Expulsado, Retirado)\n").lower)
            
            if any(estado["estado"] == "cursando" for estado in estado_cursando):
                if True:
                    cursando = []
                    for grupo_estado, grupito in cursando.items():
                        for clase in grupito:
                            for buscando, info in clase.items():
                                if info.get("estado") == opcion1:
                                    cursando.append({grupo_estado: info})
                        if cursando:
                            print("Tu horario es:")
                            for estudiando in cursando:
                                print(estudiando)
                        else:
                            print("No tienes salas asignadas.")
