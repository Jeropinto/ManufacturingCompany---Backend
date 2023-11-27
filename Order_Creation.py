import pymysql


def actualizar():
    cambio = input("Ingrese el nuevo status de la orden")
    Order.set_status({cambio})
    pass


def buscar_id(cursor):
    input_id = input("Ingrese el ID a buscar en la base de datos: ")
    sql = "SELECT * FROM Orders WHERE id = %s"
    cursor.execute(sql, (input_id,))
    result = cursor.fetchone()

    if result:
        print(f"El ID {input_id} se encontró en la base de datos: {result}")
    else:
        print(f"No se encontró ningún registro con el ID {input_id} en la base de datos.")


def crear_order(cursor, id, bottle_type, quantity, status="produccion"):
    nuevo = Order(id=id, bottle_type=bottle_type, quantity=quantity, status=status)
    pass


class Order:
    def __init__(self, id, bottle_type, quantity, status):
        self.id = id
        self.bottle_type = bottle_type
        self.quantity = quantity
        self.status = status

    # Getter 'id'
    def get_id(self):
        return self.id

    # Setter 'id'
    def set_id(self, new_id):
        self.id = new_id

    # Getter 'bottle_type'
    def get_bottle_type(self):
        return self.bottle_type

    # Setter 'bottle_type'
    def set_bottle_type(self, new_bottle_type):
        self.bottle_type = new_bottle_type

    # Getter 'quantity'
    def get_quantity(self):
        return self.quantity

    # Setter 'quantity'
    def set_quantity(self, new_quantity):
        self.quantity = new_quantity

    # Getter 'status'
    def get_status(self):
        return self.status

    # Setter 'status'
    def set_status(self, new_status):
        self.status = new_status

conn = pymysql.connect(user='sql10665373', password='91ZzgEZBkc', host='sql10.freesqldatabase.com', port=3306, db='sql10665373')
with conn.cursor() as cursor:
    while True:
        print("\nOpciones disponibles:")
        print("1. Búsqueda de ID")
        print("2. Creación de Orden")
        print("3. Actualización de Datos")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            buscar_id(cursor)
        elif opcion == '2':
            crear_order(cursor)
        elif opcion == '3':
            actualizar(cursor)
        elif opcion == '4':
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
conn.close()


