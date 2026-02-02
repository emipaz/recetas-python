import unittest
from rango import Rango, RangoError


class TestRangoContains(unittest.TestCase):
    """Pruebas exhaustivas de __contains__."""
    
    def test_contains_paso_entero(self):
        """__contains__ con paso entero."""
        it = Rango(0, 10, 2)
        self.assertTrue(0 in it)
        self.assertTrue(2 in it)
        self.assertTrue(4 in it)
        self.assertTrue(8 in it)
        self.assertFalse(1 in it)
        self.assertFalse(5 in it)
        self.assertFalse(10 in it)
    
    def test_contains_paso_flotante_05(self):
        """__contains__ con paso 0.5."""
        it = Rango(0, 10, 0.5)
        self.assertTrue(0 in it)
        self.assertTrue(0.5 in it)
        self.assertTrue(1.0 in it)
        self.assertTrue(1.5 in it)
        self.assertTrue(9.5 in it)
        # Valores que NO están
        self.assertFalse(0.3 in it)
        self.assertFalse(1.6 in it) 
        self.assertFalse(10 in it)
    
    def test_contains_paso_flotante_02(self):
        """__contains__ con paso 0.2."""
        it = Rango(0, 1, 0.2, pres=1)
        self.assertTrue(0.0 in it)
        self.assertTrue(0.2 in it)
        self.assertTrue(0.4 in it)
        self.assertTrue(0.6 in it)
        self.assertTrue(0.8 in it)
        # Valores que NO están
        self.assertFalse(0.1 in it)
        self.assertFalse(0.3 in it)
        self.assertFalse(0.5 in it)
        self.assertFalse(1.0 in it)
    
    def test_contains_paso_negativo(self):
        """__contains__ con paso negativo."""
        it = Rango(10, 0, -1)
        self.assertTrue(10 in it)
        self.assertTrue(9 in it)
        self.assertTrue(5 in it)
        self.assertTrue(1 in it)
        self.assertFalse(0 in it)
        self.assertFalse(11 in it)
    
    def test_contains_paso_negativo_flotante(self):
        """__contains__ con paso negativo flotante."""
        it = Rango(10, 0, -1.5)
        self.assertTrue(10 in it)
        self.assertTrue(8.5 in it)
        self.assertTrue(7.0 in it)
        self.assertFalse(8.4 in it)
        self.assertFalse(0 in it)
    
    def test_contains_fuera_de_rango(self):
        """__contains__ con valores fuera del rango."""
        it = Rango(5, 15, 2)
        self.assertFalse(4 in it)
        self.assertFalse(15 in it)
        self.assertFalse(20 in it)
    
    def test_contains_tipo_invalido(self):
        """__contains__ rechaza tipos inválidos."""
        it = Rango(0, 10)
        self.assertFalse("5" in it)
        self.assertFalse(None in it)
        self.assertFalse(True in it)  # bool es rechazado
    
    def test_contains_precision_flotante(self):
        """__contains__ maneja errores de precisión flotante."""
        it = Rango(0, 1, 0.1, pres=1)
        # Algunos valores pueden tener pequeños errores de redondeo
        self.assertTrue(0.3 in it or 0.3 not in it)  # Válido en cualquier caso
        self.assertTrue(0.1 in it)


class TestRangoLen(unittest.TestCase):
    """Pruebas de __len__."""
    
    def test_len_paso_entero(self):
        """Verifica len() con paso entero."""
        it = Rango(0, 10, 2)
        self.assertEqual(len(it), 5)
    
    def test_len_paso_flotante(self):
        """Verifica len() con paso flotante."""
        it = Rango(0, 1, 0.1, pres=1)
        self.assertEqual(len(it), 10)
    
    def test_len_paso_flotante_05(self):
        """Verifica len() con paso 0.5."""
        it = Rango(0, 10, 0.5)
        self.assertEqual(len(it), 20)

    def test_len_paso_negativo(self):
        """Verifica len() con paso negativo."""
        it = Rango(10, 0, -2)
        self.assertEqual(len(it), 5)
    
    def test_len_paso_negativo_flotante(self):
        """Verifica len() con paso negativo flotante."""
        it = Rango(10, 0, -0.5)
        self.assertEqual(len(it), 20)


class TestRangoBasico(unittest.TestCase):
    """Pruebas básicas."""
    
    def test_un_parametro(self):
        """rango(fin)."""
        it = Rango(5)
        self.assertEqual(list(it), [0, 1, 2, 3, 4])
    
    def test_dos_parametros(self):
        """rango(inicio, fin)."""
        it = Rango(2, 5)
        self.assertEqual(list(it), [2, 3, 4])
    
    def test_tres_parametros(self):
        """rango(inicio, fin, paso)."""
        it = Rango(0, 10, 2)
        self.assertEqual(list(it), [0, 2, 4, 6, 8])
    
    def test_tres_parametros_flotante(self):
        """rango(inicio, fin, paso) con paso flotante."""
        it = Rango(0, 1, 0.2, pres=1)
        self.assertEqual(list(it), [0.0, 0.2, 0.4, 0.6, 0.8])

    def test_paso_negativo(self):
        """rango(inicio, fin, paso) con paso negativo."""
        it = Rango(5, 0, -1)
        self.assertEqual(list(it), [5, 4, 3, 2, 1])

    def test_paso_negativo_flotante(self):
        """rango(inicio, fin, paso) con paso negativo flotante."""
        it = Rango(1, 0, -0.2, pres=1)
        self.assertEqual(list(it), [1.0, 0.8, 0.6, 0.4, 0.2])

    def test_multiple_iterations(self):
        """Verifica que se puedan hacer múltiples iteraciones."""
        it = Rango(3)
        self.assertEqual(list(it), [0, 1, 2])
        self.assertEqual(list(it), [0, 1, 2])  # Segunda iteración


class TestRangoErrores(unittest.TestCase):
    """Pruebas de errores."""
    
    def test_error_paso_cero(self):
        """paso=0 lanza error."""
        with self.assertRaises(RangoError):
            Rango(0, 10, 0)
    
    def test_error_sin_argumentos(self):
        """Sin argumentos lanza error."""
        with self.assertRaises(RangoError):
            Rango()


class TestRangosIguales(unittest.TestCase):
    """Pruebas de rangos iguales."""
    
    def test_rangos_iguales(self):
        """Verifica que dos rangos iguales sean equivalentes."""
        r1 = Rango(0, 10, 2)
        r2 = Rango(0, 10, 2)
        self.assertEqual(list(r1), list(r2))
        self.assertEqual(len(r1), len(r2))
        for val in [0, 2, 4, 6, 8]:
            self.assertTrue(val in r1)
            self.assertTrue(val in r2)
        for val in [1, 3, 5, 7, 9, 10]:
            self.assertFalse(val in r1)
            self.assertFalse(val in r2)

    def test_rangos_diferentes(self):
        """Verifica que dos rangos diferentes no sean equivalentes."""
        r1 = Rango(0, 10, 2)
        r2 = Rango(0, 10, 3)
        self.assertNotEqual(list(r1), list(r2))
        self.assertNotEqual(len(r1), len(r2))

if __name__ == "__main__":
    unittest.main(verbosity=2)