try:	
	print "escriba la cantidad de empleados:"
	cantidad= input()	
	for i in range(cantidad):
			print "escribe el nombre de tu empleado"
			diccionario= {}
			diccionario["nombre"]=raw_input()
			print "escriba la edad del empleado"
			diccionario["edad"]=input()
			print "escriba el puesto del empleado"
			diccionario["puesto"]= raw_input()
			def crear_archivo():
				archi=open('datos','w')
				archi.close
				
		
		
except:
	print "algo salio mal:("
