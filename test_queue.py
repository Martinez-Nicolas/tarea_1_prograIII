from queue import Queue

queue = Queue()

print("🧪 Probando cola sin límite:")
queue.enqueue("Misión 1")
queue.enqueue("Misión 2")
print(f"Tamaño: {queue.size()}")
print(f"Primero en la cola: {queue.first()}")
queue.dequeue()
print(f"Tamaño después del dequeue: {queue.size()}")

# Pruebas con cola con límite
print("\n🧪 Probando cola con límite:")
limited_queue = Queue(limit=2)
limited_queue.enqueue("Misión A")
limited_queue.enqueue("Misión B")
try:
    limited_queue.enqueue("Misión C")
except Exception as e:
    print(f"⚠️ Error esperado: {e}")

print(f"Tamaño actual: {limited_queue.size()}")
