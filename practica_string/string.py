print "esto es una prueva de string"
print "hola escribir tu nombre:"
h= raw_input()
t= len(h)
for i in range(t):
	print "la  letra numero %d de tu nombre es" %i
	prim1= raw_input()
	if prim1== h[i]:
		print "bien hecho"
	else:
		print "fallaste"

print "felisidades" +" "+"has terminado con exito"
