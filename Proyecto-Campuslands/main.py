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
notas_camper=notasJS["notas"]

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
    hacer_cordi=int(input("Selecciona un número: \n 1. Editar/ver notas\n 2. Estado \n 3. Crear rutas\n 4. Asignar\n 5. Listar\n"))
    
    if hacer_cordi==1: ##EDITAR/VER
        menu_notas=input("Deseas:\n 1. Ver notas salon.\n 2. Ver notas estudiante.\n 3. Poner nota.\n 4. Quitar nota.\n")
        
        if menu_notas==1: 
            group=str(input("\nA que grupo pertenece? \n"))##SELECCIÓN DE GRUPO A REVISAR
            current_grade_path = f"DATA/notas/notas_{group}.json"
            notas_grupo=current_grade_path
            with open(current_grade_path, 'r', encoding='utf-8') as json_file:
                current_grade = json.load(json_file)
            
            print(f"\n ---GRUPO {group}---\n") ##IMPRIMIR GRUPO
            for i in range(len(current_grade)):
                current = current_grade[i]
                print(current,"\n")

        elif menu_notas==2: ##BUSCAR CAMPER JIJI
            group=str(input("\nA que grupo pertenece? \n"))##SELECCIÓN DE GRUPO A REVISAR
            current_grade_path = f"DATA/notas/notas_{group}.json"
            notas_grupo=current_grade_path
            with open(current_grade_path, 'r', encoding='utf-8') as json_file:
                current_grade = json.load(json_file)
            
            print(f"\n ---GRUPO {group}---\n") ##IMPRIMIR GRUPO
            for i in range(len(current_grade)):
                current = current_grade[i]
                print(current,"\n")
            
            identific=int(input("\nCual es su identificacion? \n")) ##BUSCAR E IMPRIMIR CAMPER
            for camper in current_grade:
                if camper["id"]==identific:
                    print(camper)
                    
        elif menu_notas==3: ##EDICION NOTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAS :DDDDDDDDDD
            group=str(input("\nQue grupo desea editar? \n")) ##SELECCIÓN DE GRUPO A REVISAR
            current_grade_path = f"DATA/notas/notas_{group}.json"
            notas_grupo=current_grade_path
            with open(current_grade_path, 'r', encoding='utf-8') as json_file:
                current_grade = json.load(json_file)
            
            print(f"\n ---GRUPO {group}---\n") ##IMPRIMIR GRUPO
            for i in range(len(current_grade)):
                current = current_grade[i]
                print(current,"\n")

            identific=int(input("\nCual es su identificacion? \n")) ##BUSCAR E IMPRIMIR CAMPER
            for i in range(len(current_grade)):
                grades=current_grade[i]
                if grades["id"]==identific:
                    print(current_grade[i])
                else:
                    i=i+1

            rta=int(input("\nQue nota va a editar?\n 1. Teorica\n 2. Practica\n 3. Trabajos\n 4. Todas\n"))

            if rta==1:
                change=int(input("\nA que nota se va a cambiar nota teorica? \n"))##EN PROCESO
                current_grade_path = f"DATA/notas/notas_{group}.json"

                with open(current_grade_path, 'r', encoding='utf-8') as json_file:
                    current_grade = json.load(json_file)
                current = current_grade[i]
                current["teorica"] = change

                with open(current_grade_path, 'w', encoding='utf-8') as json_file:
                    json.dump(current_grade, json_file)
                print(current_grade)

            elif rta==2:
                change=int(input("\nA que nota se va a cambiar nota practica? \n"))##EN PROCESO
                current_grade_path = f"DATA/notas/notas_{group}.json"

                with open(current_grade_path, 'r', encoding='utf-8') as json_file:
                    current_grade = json.load(json_file)
                current = current_grade[i]
                current["practica"] = change

                with open(current_grade_path, 'w', encoding='utf-8') as json_file:
                    json.dump(current_grade, json_file)
                print(current_grade)
            
            elif rta==3:
                change=int(input("\nA que nota se va a cambiar nota trabajos? \n"))##EN PROCESO
                current_grade_path = f"DATA/notas/notas_{group}.json"

                with open(current_grade_path, 'r', encoding='utf-8') as json_file:
                    current_grade = json.load(json_file)
                current = current_grade[i]
                current["trabajos"] = change

                with open(current_grade_path, 'w', encoding='utf-8') as json_file:
                    json.dump(current_grade, json_file)
                print(current_grade)
            
            elif rta==4: ##EDITAR TODAS LAS NOTAS DEL CAMPPPPPPPPPPPPPPPPPEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRR
                change=int(input("\nA que nota se va a cambiar nota teorica? \n"))##EN PROCESO
                current_grade_path = f"DATA/notas/notas_{group}.json"
                with open(current_grade_path, 'r', encoding='utf-8') as json_file:
                    current_grade = json.load(json_file)
                current = current_grade[i]
                current["teorica"] = change
                with open(current_grade_path, 'w', encoding='utf-8') as json_file:
                    json.dump(current_grade, json_file)

                change=int(input("\nA que nota se va a cambiar nota practica? \n"))##EN PROCESO
                current_grade_path = f"DATA/notas/notas_{group}.json"
                with open(current_grade_path, 'r', encoding='utf-8') as json_file:
                    current_grade = json.load(json_file)
                current = current_grade[i]
                current["practica"] = change
                with open(current_grade_path, 'w', encoding='utf-8') as json_file:
                    json.dump(current_grade, json_file)

                change=int(input("\nA que nota se va a cambiar nota trabajos? \n"))##EN PROCESO
                current_grade_path = f"DATA/notas/notas_{group}.json"
                with open(current_grade_path, 'r', encoding='utf-8') as json_file:
                    current_grade = json.load(json_file)
                current = current_grade[i]
                current["trabajos"] = change
                with open(current_grade_path, 'w', encoding='utf-8') as json_file:
                    json.dump(current_grade, json_file)
                print(current_grade)

            else:
                print("Esta opcion no esta disponible.")
        
        elif menu_notas==4: ##EN PROCESO ESPERANDO AL PROFE (ELIMINAR NOTAS)
            
            group=str(input("\nQue grupo desea visualizar para borrar? \n"))
            notas_grupo=notas_camper[group]
            
            for i in range(len(notas_grupo)):
                print(notas_grupo[i])
            identific=int(input("\nA que estudiante le va a eliminar la nota? \n"))
            camper_analisis=[]
            for i in range(len(notas_grupo)):
                grades=notas_grupo[i]
                if grades["id"]==identific:
                    print(notas_grupo[i])
                else:
                    i=i+1

            rta=int(input("\nQue nota va a eliminar?\n 1. Teorica\n 2. Practica\n 3. Trabajos\n 4. Todas\n"))
        
            if rta==1:
                notas_grupo[i]
                print(f"\n{notas_grupo[i]}\n")

                current_grade=open("DATA/notas.json","w")
                current=json.loads(current_grade) ##Converted
                current["notas"][group][i]["teorica"]=0
                
                grade_delete=json.dumps(current)
                current_grade.write(grade_delete)
                
                print(notas_grupo[i])

            elif rta==2:
                notas_grupo[i]
                print(f"\n{notas_grupo[i]}\n")

                current_grade=open("DATA/notas.json","w")
                current=json.loads(current_grade) ##Converted
                current["notas"][group][i]["practica"]=0
                
                grade_delete=json.dumps(current)
                current_grade.write(grade_delete)
                
                print(notas_grupo[i])


            elif rta==3:
                notas_grupo[i]
                print(f"\n{notas_grupo[i]}\n")

                current_grade=open("DATA/notas.json","w")
                current=json.loads(current_grade) ##Converted
                current["notas"][group][i]["trabajos"]=0
                
                grade_delete=json.dumps(current)
                current_grade.write(grade_delete)
                
                print(notas_grupo[i])
            
            elif rta==4:

                print(f"\n{notas_grupo[i]}\n")

                current_grade=open("DATA/notas.json","w")
                current=json.loads(current_grade) ##Converted
                current["notas"][group][i]["teorica"]=0
                current["notas"][group][i]["practica"]=0
                current["notas"][group][i]["trabajos"]=0
                
                grade_delete=json.dumps(current)
                current_grade.write(grade_delete)
                
                print(notas_grupo[i])
                                                        ##HASTA ACA LLEGA EN PROCESO
            else:
                print("Esta opcion no esta disponible.")

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
                opcion2=int(input("Pon la identificación del estudiante a buscar:\n"))
                datico2=input("Pon el salon al que pertenece(si pertenece a uno)\n")
                if datico2 in campersJS["grados"]:
                    especifico = [estate["estado"] for estate in campersJS["grados"][datico2] if estate["id"] == opcion2]
                    if especifico:
                        for tarta in especifico:
                            print(tarta)
                elif  genteJS["gente"]:
                    especifico = [estate["estado"] for estate in genteJS["gente"] if estate["id"] == opcion2]
                    if especifico:
                        for tarta in especifico:
                            print(tarta)
                else:
                    print("No se encontro")
                    
            #Editar un estado:
            elif menu_estado==3:
                opcion3 = int(input("Pon la identificación del estudiante a buscar:\n"))
                datico3=input("Pon el salon al que pertenece(si pertenece a uno)\n")
                nuevo_estado=input("Pon el nuevo estado que tendra\n").lower()
                if datico3 in campersJS["grados"]:
                    especifico = [estate["estado"] for estate in campersJS["grados"][datico3] if estate["id"] == opcion3]
                    if especifico:
                        us_camper['estado'] = nuevo_estado

                        if nuevo_estado=="cursando":
                            with open('campers.json', 'w') as json_file:
                                json.dump(campersJS, json_file)
                                print(us_camper)
                        elif nuevo_estado!="cursando":
                            with open('gente.json', 'w') as json_file:
                                json.dump(genteJS, json_file)
                                print(genteJS)

                elif  genteJS["gente"]:
                    especifico = [estate["estado"] for estate in genteJS["gente"] if estate["id"] == opcion3]
                    if especifico:
                        genteJS['estado'] = nuevo_estado
                        
                        if nuevo_estado=="cursando":
                            with open('campers.json', 'w') as json_file:
                                json.dump(campersJS, json_file)
                                print(us_camper)
                        elif nuevo_estado!="cursando":
                            with open('gente.json', 'w') as json_file:
                                json.dump(genteJS, json_file)
                                print(genteJS)

                else:
                    print("No se encontro")
                                
    elif hacer_cordi==3: #Crear ruta
            nueva_ruta=[]
            j=input("Pon el grupo y ruta a crear.(Ejemplo: grupo: P2, Ruta: Note)\n ")
            nueva_ruta.append(j)
            us_ruta.append(nueva_ruta)
            print(us_ruta)

    elif hacer_cordi==4:#Asignar(parte de la hora)
        id=int(input("Pon la identificacion del profesor que deseas asignar:\n"))
        salo_trainers

    elif hacer_cordi==5:#Listar
        who=int(input(" 1. Listar trainers\n 2. Listar camper y trainer por ruta\n"))

        if who==1:
            lis_trainers=[]
            for queso in us_trainer:
                lis_trainers.append(queso["nombres"])
            print(lis_trainers)

        elif who==2:
            for q in us_ruta:
                print(q)


else:
    print("Se ingreso mal la información o no existe.")
