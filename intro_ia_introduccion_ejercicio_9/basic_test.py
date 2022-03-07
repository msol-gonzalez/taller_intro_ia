import classes

if __name__ == '__main__':

    #subclase entretenimiento
    entretenimiento  = classes.Entretenimiento()
    entretenimiento.deposito("cine", 1000)
    entretenimiento.deposito("educacion", 1000)

    #sin fondos suficientes
    #assert (entretenimiento.extraccion(50000, "alimentos"))
    assert (entretenimiento.extraccion(50, "alimentos"))

    print ("el balance es de la categoria entretenimiento: ", entretenimiento.obtener_balance())



    #subclase alimento
    restaurant = classes.Alimento()
    restaurant.deposito("restaurant", 200)

    entretenimiento.transferencia(200,restaurant,entretenimiento)

    entretenimiento.presupuesto()

    restaurant.presupuesto()

    vesti = classes.Vestimenta()
    vesti.deposito("jean", 200)
    vesti.presupuesto()

    restaurant.crear_tabla_gastos(vesti, entretenimiento)


