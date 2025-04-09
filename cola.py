class Queue:
    """
    Implementación de una cola (FIFO: First In, First Out).
    Permite agregar elementos al final de la cola (enqueue), 
    eliminar y obtener el primer elemento de la cola (dequeue), 
    y revisar el primer elemento sin eliminarlo (first).
    """
    
    def __init__(self, limit=None):
        """
        Constructor de la clase Queue.
        """
        self.items = []  # Lista interna para almacenar los elementos de la cola
        self.limit = limit  # Límite opcional para el número de elementos

    def enqueue(self, item):
        """
        Añade un nuevo elemento al final de la cola.
        """
        if self.limit is None or len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise Exception("La cola ha alcanzado su límite")

    def dequeue(self):
        """
        Elimina y retorna el primer elemento de la cola.
        """
        if not self.is_empty():
            return self.items.pop(0)
        raise Exception("La cola está vacía")

    def first(self):
        """
        Retorna el primer elemento de la cola sin eliminarlo.
        """
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        """
        Verifica si la cola está vacía.
        """
        return len(self.items) == 0

    def size(self):
        """
        Obtiene el tamaño de la cola (número de elementos).
        """
        return len(self.items)
