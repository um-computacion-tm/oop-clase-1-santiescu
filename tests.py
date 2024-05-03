import unittest
from clases import Alumno, Materia, Profesor

class TestMateria (unittest.TestCase):
    
    def test_constructor(self):
        nombre='Calculo'
        profesores=['Dario','Patricia']
        calculo=Materia(nombre,profesores)
        self.assertEqual(calculo.__nombre__,'Calculo')
        self.assertEqual(calculo.__profesores__,['Dario','Patricia'])
    
    def test_obtener_profesores(self):
        nombre='Calculo'
        profesores=['Dario','Patricia']
        calculo=Materia(nombre,profesores)
        self.assertEqual(calculo.obtener_profesores(),['Dario','Patricia'])
    
    def test_cambiar_nombre(self):
        nombre='Calculo'
        profesores=['Dario','Patricia']
        calculo=Materia(nombre,profesores)
        calculo.cambiar_nombre('Calculo2')
        self.assertEqual(calculo.__nombre__,'Calculo2')

class TestProfesor (unittest.TestCase):
     
     def test_profesor(self):
        profesores = Profesor("dario", "titular", "6000")
        self.assertEqual(profesores.__nombre__, "dario")
        self.assertEqual(profesores.__cargo__, "titular")
        self.assertEqual(profesores.__legajo__, "6000")

     def test_obtener_nomnbre(self):
        profesores = Profesor("dario", "titular", "6000")
        self.assertEqual(profesores.obtener_nombre(), "dario")

     def test_obtener_cargo(self):
        profesores = Profesor("dario", "titular", "6000")
        self.assertEqual(profesores.obtener_cargo(), "titular")

     def test_obtener_legajo(self):
        profesores = Profesor("dario", "titular", "6000")
        self.assertEqual(profesores.obtener_legajo(), "6000")

class TestAlumno (unittest.TestCase):
  
    def test_alumno(self):
        alumno = Alumno("Santiago", "62068", "20", ".sb.escudero")
        self.assertEqual(alumno.__nombre__, "Santiago")
        self.assertEqual(alumno.__legajo__, "62068")
        self.assertEqual(alumno.__edad__, "20")
        self.assertEqual(alumno.__mail__, ".sb.escudero") 

    def test_obtener_nombre(self):
        alumno = Alumno("Santiago", "62068", "20", ".sb.escudero")
        self.assertEqual(alumno.obtener_nombre(), "Santiago")

    def test_cambiar_mail(self):
        mail = ".sb.escudero"
        alumno = Alumno("Santiago", "62068", "20", mail)
        alumno.cambiar_mail("i.milutin")
        self.assertEqual(alumno.__mail__, "i.milutin")






unittest.main()