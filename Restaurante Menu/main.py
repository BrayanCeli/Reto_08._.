#codigo de prueba aqui#

from restaurante3 import ManejoPedidos, Pago, Pedido, PedidoObjetosIterables

"""
aca va la prueba de lo que esta en el archivo restaurante3.py y se 
comprueba con modificaciones con respecto al archivo original
"""

def demo_pedido_completo():
    manager = ManejoPedidos()

def mostrar_menu(manager):
    """Muestra el menú actual"""
    print("\n--- MENÚ DISPONIBLE ---")
    for nombre, item in manager.menu.menu_items.items():
        print(f"{nombre}: ${item.price:.2f} ({item.type}/{item.subtype})")

items_iniciales = [
        ("Refresco", 2.5, "bebida", "mediano"),
        ("Ensalada Felipe", 6.50, "plato", "entrada"),
        ("Pizza Hawaiana", 12.5, "plato", "principal"),
        ("Banana split", 5.0, "postre", "postre")
    ]
for nombre, precio, tipo, subtipo in items_iniciales:
        if not manager.menu.get_item(nombre):
            manager.menu.add_item(nombre, precio, tipo, subtipo)
    
mostrar_menu(manager)
    
pedido = manager.create_order()
print("\n--- AÑADIENDO ÍTEMS AL PEDIDO ---")
    
manager.add_to_order(pedido, "Pizza Hawaiana", 2)
manager.add_to_order(pedido, "Banana split", 1)
    
pedido.mostrar_factura()
    
print("\n--- PROCESANDO PAGO ---")
pago = Pago(pedido, "tarjeta")
if pago.procesar_pago():
    print("Pago completado con éxito :)")
else:
    print("Fallo en el pago >:(")

pago.generar_recibo()

if __name__ == "__main__":
    try:
        demo_pedido_completo()
        
        print("\n✨ Prueba completada con éxito ✨")
        
        pedido = Pedido()
        pedido.agregar_item(refresco, 2)
        pedido.agregar_item(cerveza)
        pedido.agregar_item(ensalada)
        pedido.agregar_item(pizza, 2)
        
        print("\nItems en el pedido:")
        for item in pedido.get_items_iterable():
            print(f"{item['nombre']} x{item['cantidad']} ({item['tipo']}/{item['subtipo']})")
            print(f"  Precio unitario: ${item['precio_unitario']:.2f}")
            print(f"  Precio total: ${item['precio_total']:.2f}\n")
        
    
    except ValueError as e:
        print(f"\nError durante la prueba: {str(e)}")
    
    print("DEMO SISTEMA DE RESTAURANTE 3.0 ")
    
    
 

