"""por que esta lista queda de la forma 0, 1, 2, string"""
print "ingrese  el numero de palabras que usara"
tam= input 
for i in range(tam):
	list=range(tam)
	print "agregue la palabra numero %d" %i
	list[i]= raw_input()
print list


