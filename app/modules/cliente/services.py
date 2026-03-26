from typing import List, Optional
from .schemas import ClienteCreate, ClienteRead

db_clientes: List[ClienteRead] = [
    ClienteRead(id=1, nombre="Empresa A", email="contacto@empresaa.com", cuil=123456789, activo=True)
]
id_counter = 2

# Función para crear un cliente nuevo
def crear(data: ClienteCreate) -> Optional[ClienteRead]:
    global id_counter
    
    email_existe = any(c.email == data.email for c in db_clientes)
    if email_existe:
        return None
        
    nuevo = ClienteRead(id=id_counter, **data.model_dump())
    db_clientes.append(nuevo)
    id_counter += 1
    return nuevo

# Función para enlistar todos los clientes
def obtener_todos(skip: int = 0, limit: int = 10, activo: Optional[bool] = None) -> List[ClienteRead]:
    resultados = db_clientes
    
    if activo is not None:
        resultados = [c for c in resultados if c.activo == activo]
        
    return resultados[skip : skip + limit]

# Función para obtener los clientes por ID
def obtener_por_id(id: int) -> Optional[ClienteRead]:
    for c in db_clientes:
        if c.id == id:
            return c
    return None

# Función para actualizar los datos de un cliente
def actualizar_cliente(id: int, data:ClienteCreate) -> Optional[ClienteRead]:
    for index, c in enumerate(db_clientes):
        if c.id == id:
            cliente_actualizado = ClienteRead(id=id, **data.model_dump())
            db_clientes[index] = cliente_actualizado
            return cliente_actualizado
    return None

# Función para eliminar un cliente
def desactivar_cliente(id: int) -> Optional[ClienteRead]:
    for index, c in enumerate(db_clientes):
        if c.id == id:
            c_dict = c.model_dump()
            c_dict["activo"] = False
            cliente_actualizado = ClienteRead(**c_dict)
            db_clientes[index] = cliente_actualizado
            return cliente_actualizado
    return None
