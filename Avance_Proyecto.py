class Cliente:
    def __init__(self, usuario, nombre, edad, genero, peso, estatura, cadera, objetivo, alergias):
        
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.estatura = estatura
        self.cadera = cadera
        self.objetivo = objetivo
        self.alergias = alergias
        self.usuario = usuario
        self.genero = genero
        self.entrenadores = None
        self.entrenamiento = None
        
        

        indice_grasa = cadera / (estatura * sqrt(estatura)) - 18
        imc = peso/(estatura**2)

        self.indice_masa_corporal = imc
        self.indice_grasa = indice_grasa
    def registrar(self):
        try:
            base_cliente = open("base_cliente.txt", 'r')
        except FileNotFoundError:
            open("base_cliente.txt", 'w')
        with open("base_cliente.txt", 'a') as base_cliente:
            base_cliente.write(f"{self.usuario} {self.nombre} {self.edad} {self.peso} {self.estatura} {self.cadera} {self.objetivo} {self.alergias}")
