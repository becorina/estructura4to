#herencia
class Estudiantes:#CLASE PADRE
    def __init__(self,nom,edad,dni):
        self.nom=nom
        self.edad=edad
        self.precio=dni
    def descripcion(self):
        print(f"Nombre: {self.nom} edad: {self.edad} dni: {self.dni}")  
class profesor(Estudiantes):
        def __init__(self, nom, edad, dni, escuela):
            super().__init__(nom, edad, dni)
            self.escuela=escuela
        def descripcion(self):
            super().descripcion()
            print(f"escuela {self.escuela}")  
class estudiantes(Estudiantes):
    def __init__(self, nom, edad, dni, escuela):
            super().__init__(nom, edad, dni)
            self.escuela=escuela
    def descripcion(self):
            super().descripcion()
            print(f"escuela {self.escuela}")
            
p1=estudiantes("Bauti",2021,"16años", 48 548 583 "ProA")
p1.descripcion()
p2=estudiantes("Antonio",2022,"13años",57 456 654 "Monjas")
p2.descripcion()
p3=estudiantes("Juan",2021,"15años",47 537 572 "juan pablo")              
p3.descripcion() 
   
    
    