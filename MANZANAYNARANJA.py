def manzanas_naranjas():
    print("Elige el radio de la casa (dos números separados por un espacio, primero el menor valor)")
    s,t = map(int, input().strip().split(' '))
    print("Introduce la posición del manzano y del naranjo separadas por un espacio.")
    a,b = map(int, input().strip().split(' '))
    print("Introduce a la distancia a la que caen las manzanas del manzano y las naranjas del naranjo separadas por un espacio.")
    m,n = map(int, input().strip().split(' '))
    print("Introduce las distancias que hay entre cada par de manzanas separadas por un espacio.")
    apple = list(map(int, input().strip().split(' ')))
    print("Introduce las distancias que hay entre cada par de naranjas separadas por un espacio.")
    orange = list(map(int, input().strip().split(' ')))

    manzanas_caidas = sum([1 for f in apple if (f+a) >= s and (f+a) <= t])
    naranjas_caidas = sum([1 for f in orange if (f+b) >= s and (f+b) <= t])

    if manzanas_caidas != 1:
        print ("Han caído {} manzanas en la casa".format(manzanas_caidas))
    else:
        print ("Ha caído {} manzana en la casa".format(manzanas_caidas))
    if naranjas_caidas != 1:   
        print ("Ha caído {} naranja en la casa".format(naranjas_caidas))
    else:
        print ("Ha caído {} naranja en la casa".format(naranjas_caidas))

manzanas_naranjas()


