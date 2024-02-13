#Catalina Mulford Monroy y Daniela Forero Ballen
#Primer archivo de prueba
import json
import module as mod

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
us_ruta=rolesJS["Campuslands"]["Grupos"]
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
    hacer_cordi=int(input("Selecciona un número: \n 1. Editar/ver notas\n 2. Estado \n 3. Crear rutas\n 4. Asignar\n"))
    
    if hacer_cordi==1: ##EDITAR/VER
        menu_notas=input("Deseas:\n 1. Ver notas salon.\n 2. Ver notas estudiante.\n 3. Poner nota.\n 4. Quitar nota.\n")
        
        if menu_notas==1: 
            group=str(input("\nQue grupo desea revisar? \n"))##SELECCIÓN DE GRUPO A REVISAR
            notas_grupo=notas_camper[group]
            for i in range(len(notas_grupo)):
                print(notas_grupo[i])

        elif menu_notas==2:
            group=str(input("\nA que grupo pertenece? \n"))##SELECCIÓN DE GRUPO A REVISAR
            notas_grupo=notas_camper[group]
            identific=int(input("\nCual es su identificacion? \n"))
            for i in range(len(notas_grupo)):
                grades=notas_grupo[i]
                if grades["id"]==identific:
                    print(notas_grupo[i])
                else:
                    i=i+1
        elif menu_notas==3:
            print("En proceso :D")
        
        

    if hacer_cordi==2:#Estado
            menu_estado=int(input("Deseas:\n 1. Buscar personas por estado.\n 2. Ver estado de un estudiante.\n 3. Editar estado.\n"))
            
            #Todos los de un mismo estado
            if menu_estado==1:
                opcion1=str(input("Que estado deseas buscar?(Ingreso, Inscrito, Aprobado,Cursando, Graduado, Expulsado, Retirado)\n").lower())
                otro_cursando=[]
                cursando = []

                if opcion1=="cursando":
                    for grado, estudiantes in campersJS["grados"].items():
                        for estudiante in estudiantes:
                            if estudiante["estado"].lower() == opcion1:
                                cursando.append(estudiante)
                    if cursando:
                        print(f"Estudiantes en estado '{opcion1}':")
                        for estudiante in cursando:
                            print(f"Nombre: {estudiante['nombres']} {estudiante['apellidos']}, estado: {estudiante['estado']}")
                    else:
                        print(f"No se encontraron estudiantes en estado '{opcion1}'.")
                
                elif opcion1!="cursando":
                    for estudiante in genteJS["gente"]:
                        if estudiante["estado"].lower() == opcion1:
                            otro_cursando.append(estudiante)
                    if otro_cursando:
                        print(f"Estudiantes en estado '{opcion1}':")
                        for estudiante in otro_cursando:
                            print(f"Nombre: {estudiante['nombres']} {estudiante['apellidos']}, estado: {estudiante['estado']}")
                    else:
                        print(f"No se encontraron estudiantes en estado '{opcion1}'.")
            
            #Ver estado de un estudiante en especifico
            elif menu_estado==2:
                print("Ya no másssssss")


            #Editar un estado:
            elif menu_estado==3:
                print("Que problematico es esto de existir.")
                                
    elif hacer_cordi==3: #Crear ruta
            nueva_ruta=[]
            j=input("Pon el grupo y ruta a crear.(Ejemplo: grupo: P2, Ruta: Note)\n ")
            nueva_ruta.append(j)
            us_ruta.append(nueva_ruta)
            print(us_ruta)

    elif hacer_cordi==5:#Proceso, no funciona :)
        who=input(" 1. Listar trainers\n 2. Listar camper y trainer por ruta\n")

        if who==1:
            lis_trainers=[]
            for queso in us_trainer:
                lis_trainers.append("nombres")
            print(lis_trainers)
        elif who==2:
            delirio=rolesJS["Grupos"]
            print(delirio)
