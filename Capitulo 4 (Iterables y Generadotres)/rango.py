class RangoError(Exception):
    """Excepción personalizada para errores de Rango."""
    pass


class Rango:
    """Iterador reutilizable que genera valores en un rango."""
    
    def __init__(self, *args, pres=1):
        """Inicializa el rango con validación.
        
        Args:
            *args: 1-3 argumentos numéricos (inicio, final, paso)
            pres (int): Precisión decimal. Default: 1
        
        Raises:
            RangoError: Si los argumentos son inválidos
        """
        self.pres = pres
        self._validar_y_asignar_parametros(*args)
    
    def _validar_y_asignar_parametros(self, *args):
        """Valida y asigna parámetros internos."""
        
        if not args:
            raise RangoError(
                "❌ rango() requiere al menos 1 argumento\n"
                "   Uso: Rango(fin) | Rango(inicio, fin) | Rango(inicio, fin, paso)"
            )
        
        if len(args) > 3:
            raise RangoError(
                f"❌ rango() recibió {len(args)} argumentos, máximo 3\n"
                f"   Argumentos recibidos: {args}"
            )
        
        if len(args) == 1:
            self.inicio, self.final, self.paso = 0, args[0], 1
        elif len(args) == 2:
            self.inicio, self.final, self.paso = args[0], args[1], 1
        else:
            self.inicio, self.final, self.paso = args[0], args[1], args[2]
        
        for valor, nombre in [(self.inicio, "inicio"), 
                              (self.final, "final"), 
                              (self.paso, "paso")]:
            if isinstance(valor, bool):
                raise RangoError(
                    f"❌ '{nombre}' no puede ser booleano\n"
                    f"   Valor: {valor}"
                )
            
            if not isinstance(valor, (int, float)):
                raise RangoError(
                    f"❌ '{nombre}' debe ser número\n"
                    f"   Tipo recibido: {type(valor).__name__}\n"
                    f"   Valor: {repr(valor)}"
                )
        
        if self.paso == 0:
            raise RangoError(
                "❌ 'paso' no puede ser cero\n"
                "   Intenta con paso=1 o paso=-1"
            )
        
        if self.pres < 0:
            raise RangoError(
                f"❌ 'pres' no puede ser negativa\n"
                f"   pres = {self.pres}"
            )
    
    def __iter__(self):
        """Retorna un generador cada vez que se itera.
        
        Yields:
            float: Valores en el rango
        """
        actual = self.inicio
        
        while (self.paso > 0 and round(actual, self.pres) < round(self.final, self.pres)) or \
              (self.paso < 0 and round(actual, self.pres) > round(self.final, self.pres)):
            yield round(actual, self.pres)
            actual += self.paso
    
    def __repr__(self):
        return f"Rango({self.inicio}, {self.final}, {self.paso})"
    
    def __len__(self):
        """Calcula la cantidad de elementos sin iterar.
        
        Funciona con pasos enteros y flotantes.
        
        Returns:
            int: Número de elementos en el rango
        """
        if self.paso > 0:
            if self.final <= self.inicio:
                return 0
            diferencia = self.final - self.inicio
            cantidad = diferencia / self.paso
            return int(cantidad)
        else:
            if self.final >= self.inicio:
                return 0
            diferencia = self.inicio - self.final
            cantidad = diferencia / abs(self.paso)
            return int(cantidad)
    
    def __contains__(self, valor):
        """Verifica si un valor está EN LA SECUENCIA sin iterar todo.
        
        Calcula matemáticamente si el valor pertenece a la secuencia:
        Para paso positivo: valor = inicio + n*paso donde n es entero ≥ 0
        Para paso negativo: valor = inicio + n*paso donde n es entero ≥ 0
        
        Args:
            valor: Valor a verificar
        
        Returns:
            bool: True si el valor está exactamente en la secuencia
        
        Examples:
            >>> it = Rango(0, 10, 2)
            >>> 4 in it      # True (0 + 2*2)
            >>> 5 in it      # False
            >>> it = Rango(0, 10, 0.5)
            >>> 1.5 in it    # True (0 + 3*0.5)
            >>> 1.6 in it    # False
        """
        # Validar tipo
        if isinstance(valor, bool):
            return False
        
        if not isinstance(valor, (int, float)):
            return False
        
        # Verificar si está en el rango correcto
        if self.paso > 0:
            if not (self.inicio <= valor < self.final):
                return False
        else:
            if not (self.final < valor <= self.inicio):
                return False
        
        # Calcular n: cuántos pasos desde inicio hasta valor
        # valor = inicio + n * paso  =>  n = (valor - inicio) / paso
        n = (valor - self.inicio) / self.paso
        
        # n debe ser un número entero (o muy cercano por errores flotantes)
        # Usamos una tolerancia pequeña para comparaciones flotantes
        tolerancia = 10 ** (-self.pres - 2)
        
        n_redondeado = round(n)
        diferencia = abs(n - n_redondeado)
        
        # Verificar si n es prácticamente entero
        if diferencia > tolerancia:
            return False
        
        # Verificar que n sea no-negativo
        if n_redondeado < 0:
            return False
        
        return True
    
    def __eq__(self, otro):
        """Compara dos objetos Rango."""
        if not isinstance(otro, Rango):
            return False
        return (self.inicio == otro.inicio and 
                self.final == otro.final and 
                self.paso == otro.paso and 
                self.pres == otro.pres)
    
    def __str__(self):
        """Representación en string del rango."""
        return f"Rango({self.inicio}, {self.final}, {self.paso}) pres={self.pres}"


def rango(*args, pres=1):
    """Función auxiliar que retorna un objeto Rango.
    
    Args:
        *args: 1-3 argumentos numéricos
        pres (int): Precisión decimal
    
    Returns:
        Rango: Objeto iterador reutilizable
    """
    return Rango(*args, pres=pres)


# === EJEMPLOS DE USO ===
if __name__ == "__main__":
    print("=" * 70)
    print("✅ PRUEBA 1 - __contains__ con paso ENTERO")
    print("=" * 70)
    it = Rango(0, 10, 2)
    print(f"Rango: {it}")
    print(f"Elementos: {list(it)}")
    print(f"¿4 en rango? (esperado: True): {4 in it}")
    print(f"¿5 en rango? (esperado: False): {5 in it}")
    print(f"¿0 en rango? (esperado: True): {0 in it}")
    print(f"¿10 en rango? (esperado: False): {10 in it}")
    
    print("\n" + "=" * 70)
    print("✅ PRUEBA 2 - __contains__ con paso FLOTANTE 0.5")
    print("=" * 70)
    it = Rango(0, 10, 0.5)
    print(f"Rango: {it}")
    print(f"Primeros 11 elementos: {list(Rango(0, 6, 0.5))}")
    print(f"¿1.5 en rango? (esperado: True): {1.5 in it}")
    print(f"¿1.6 en rango? (esperado: False): {1.6 in it}")  # ✅ Ahora False
    print(f"¿3.0 en rango? (esperado: True): {3.0 in it}")
    print(f"¿3.25 en rango? (esperado: False): {3.25 in it}")
    
    print("\n" + "=" * 70)
    print("✅ PRUEBA 3 - __contains__ con paso FLOTANTE 0.2")
    print("=" * 70)
    it = Rango(0, 1, 0.2, pres=1)
    print(f"Rango: {it}")
    print(f"Elementos: {list(it)}")
    print(f"¿0.0 en rango? (esperado: True): {0.0 in it}")
    print(f"¿0.2 en rango? (esperado: True): {0.2 in it}")
    print(f"¿0.4 en rango? (esperado: True): {0.4 in it}")
    print(f"¿0.3 en rango? (esperado: False): {0.3 in it}")  # ✅ Ahora False
    print(f"¿1.0 en rango? (esperado: False): {1.0 in it}")
    
    print("\n" + "=" * 70)
    print("✅ PRUEBA 4 - __contains__ con paso NEGATIVO")
    print("=" * 70)
    it = Rango(10, 0, -1.5)
    print(f"Rango: {it}")
    print(f"Elementos: {list(it)}")
    print(f"¿10 en rango? (esperado: True): {10 in it}")
    print(f"¿8.5 en rango? (esperado: True): {8.5 in it}")
    print(f"¿8.4 en rango? (esperado: False): {8.4 in it}")
    print(f"¿0 en rango? (esperado: False): {0 in it}")
    
    print("\n" + "=" * 70)
    print("✅ PRUEBA 5 - Comparación de métodos")
    print("=" * 70)
    it = Rango(0, 5, 0.5)
    valor_busqueda = 2.5
    print(f"Rango: {it}")
    print(f"¿{valor_busqueda} en rango (con __contains__)?: {valor_busqueda in it}")
    print(f"¿Verificación manual: {list(Rango(0, 5, 0.5))}")