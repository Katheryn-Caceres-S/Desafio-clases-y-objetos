

class Te:
    
    #atributo de clase. 365 dias
    duracion =  365

    sabores = {
        1: {"nombre": "te negro", "tiempo": 3, "recomendacion": "desayuno"},
        2: {"nombre": "te verde", "tiempo": 5, "recomendacion": "almuerzo"},
        3: {"nombre": "agua de hierbas", "tiempo": 6, "recomendacion": "once"},
    }

    precios = {
        300 : 3000,
        500 : 5000
    }

    @staticmethod
    def receta (sabor:int):
        """retorna el tiempo de preparacionen minutos y  recomendacion segun sabro inresado"""

        pedido = Te.sabores[sabor]

        return pedido["nombre"], pedido["tiempo"], pedido["recomendacion"]


    @staticmethod
    def obtener_precio(formato:int):   
        """retorna precio para el formato indicado""" 

        return Te.precios[formato]