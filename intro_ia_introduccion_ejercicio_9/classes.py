from abc import abstractmethod


class Categoria ():

    def __init__(self):
        self.contabilidad = []

    '''Metodo que habilita hacer un depósito'''

    def deposito(self, descripcion, monto):
        var = list(filter(lambda item: item['descripcion'] == descripcion, self.contabilidad))
        if not var:
            self.contabilidad.append({'cantidad': monto, 'descripcion': descripcion})
        else:
            #cantidad = var[0].get('cantidad')
            var[0]['cantidad'] = var[0]['cantidad'] + monto

    '''Metodo para obtener balance de la contabilidad central'''''
    def obtener_balance(self):
        total = 0
        for element in self.contabilidad:
            total = total + element.get('cantidad')

        return total



    '''Metodo para verificar fondos'''
    def verificar_fondos(self, monto):
        if (monto <= self.obtener_balance()):
            return True
        else:
            return False
        # #funcionamiento anterior
        # var = list(filter(lambda item: item['descripcion'] == descripcion, self.contabilidad))
        # valor_inicial = var[0]['cantidad']
        # if (monto > valor_inicial):
        #     return False
        # else:
        #     return True

    '''Metodo de extraccion de fondos, utiliza el metodo de verificar_fondos para verificar que los fondos sean correctos'''
    def extraccion(self, monto, descripcion):
        #if (self.verificar_fondos(monto = monto, descripcion= descripcion) == True):
        if (self.verificar_fondos(monto=monto) == True):
            monto_extraccion = monto * (-1)
            self.contabilidad.append({'cantidad': monto_extraccion, 'descripcion': descripcion})
            return True
        else:
            return False


    '''Metodo para realizar transferencia:
    con una extracción y un depósito en las catergorías que corresponda, con la descripción:
    "Transf. a Categoría destinp" y "Trans. de Categoría destino" '''

    def transferencia(self, monto, categoria_dest, categoria_origen):
        #if (self.verificar_fondos(monto = monto, descripcion= descripcion) == True):
        if (self.verificar_fondos(monto=monto) == True):
            # Subclase de las categorias
            origen = (categoria_origen.__class__.__name__)
            destino = (categoria_dest.__class__.__name__)
            # Detalle de operatoria
            descripcion_deposito = "Transferencia de origen " + origen
            descripcion_destino = "Transferencia a " + destino

            assert ((self.extraccion(monto,descripcion_destino)) == True)


            categoria_dest.deposito( descripcion_deposito, monto)

        else:
            return False




    ''' Método abstracto para cada uno de las categorias
    Lo extendi en otras subclases '''

    @abstractmethod
    def presupuesto(self):
        pass

    '''Método para graficar tablas'''


    def crear_tabla_gastos(self, categoria_2, categoria_3):
        #por el momento solo son 3 categorias (subclases)
        porcent = "o"

        cat_1 = self.__class__.__name__
        balance_cat1 = self.obtener_balance()

        balance_cat2 = categoria_2.obtener_balance()
        cat_2 = categoria_2.__class__.__name__

        balance_cat3 = categoria_3.obtener_balance()
        cat_3 = categoria_3.__class__.__name__

        total_cat = balance_cat1 + balance_cat2 + balance_cat3
        cat_1_porcen = round((balance_cat1 * 100 / total_cat), -1 )
        cat_2_porcen = round((balance_cat2 * 100 / total_cat), -1 )
        cat_3_porcen = round((balance_cat3 * 100 / total_cat), -1 )


        barras_cat1 = int(cat_1_porcen / 10)
        total_cat1 = (10 - barras_cat1) * " " + ((1 + barras_cat1) * "o")

        barras_cat2 = int(cat_2_porcen / 10)
        total_cat2 = (10 - barras_cat2) * " " + ((1 + barras_cat2) * "o")

        barras_cat3 = int(cat_3_porcen / 10)
        total_cat3 = (10 - barras_cat3) * " " + ((1 + barras_cat3) * "o")



        for c in range(0, 11):
            print((100 - (10 * c)), " | ", total_cat1[c], total_cat2[c], total_cat3[c])
        print("----------")

        #TODO! Ajustar el rango para palabra completa
        for c in range(0, 8):
            print ("   ", cat_1[c], cat_2[c],cat_3[c])






# Herencia de para las categorias Alimento, vestimenta, entretenimiento
class Alimento(Categoria):

    def __init__(self):
        '''Inicializa los atributos de la clase Padre'''
        super().__init__()

    def presupuesto(self):
        title = "*************"
        subclase_name = (self.__class__.__name__)
        print (title + subclase_name + title)
        for element in self.contabilidad:
            print(element.get("descripcion"), "   ", element.get("cantidad"))
        print("Total: ", self.obtener_balance())



class Vestimenta(Categoria):

    def __init__(self):
        '''Inicializa los atributos de la clase Padre'''
        super().__init__()

    def presupuesto(self):
        title = "*************"
        subclase_name = (self.__class__.__name__)
        print (title + subclase_name + title)
        for element in self.contabilidad:
            print(element.get("descripcion"), "   ", element.get("cantidad"))
        print("Total: ", self.obtener_balance())




class Entretenimiento(Categoria):
    def __init__(self):
        '''Inicializa los atributos de la clase Padre'''
        super().__init__()

    def presupuesto(self):
        title = "*************"
        subclase_name = (self.__class__.__name__)
        print (title + subclase_name + title)
        for element in self.contabilidad:
            print(element.get("descripcion"), "   ", element.get("cantidad"))
        print("Total: ", self.obtener_balance())



