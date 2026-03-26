from fastapi import APIRouter, HTTPException, Query, status, Path
from typing import List, Optional
from . import schemas, services

router = APIRouter(prefix="/clientes", tags=["Clientes"])

# ---------------------------------------------------------
# ALTA DE CLIENTE
# Método: POST | Endpoint: /clientes | Estado: 201 Created
# ---------------------------------------------------------
@router.post("/", response_model=schemas.ClienteRead, status_code=status.HTTP_201_CREATED)
def alta_cliente(cliente: schemas.ClienteCreate):
    nuevo_cliente = services.crear(cliente)
    
    if not nuevo_cliente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="El email ya se encuentra registrado en el sistema"
        )
    return nuevo_cliente

@router.get("/", response_model=List[schemas.ClienteRead], status_code=status.HTTP_200_OK)
def listar_clientes(
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, le=50),
    activo: Optional[bool] = Query(None, description="Filtrar clientes por estado activo/inactivo")
):
    return services.obtener_todos(skip, limit, activo)

# ---------------------------------------------------------
# DETALLE DE CLIENTE (Obtener por ID)
# Método: GET | Endpoint: /clientes/{id} | Estado: 200 OK
# ---------------------------------------------------------
@router.get(
    "/{id}", response_model=schemas.ClienteRead, status_code=status.HTTP_200_OK
)
def detalle_cliente(id: int = Path(..., gt=0)):
    cliente = services.obtener_por_id(id)
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado"
        )
    return cliente


# ---------------------------------------------------------
# ACTUALIZAR CLIENTE (Reemplazo Total)
# Método: PUT | Endpoint: /clientes/{id} | Estado: 200 OK
# ---------------------------------------------------------
@router.put(
    "/{id}", response_model=schemas.ClienteRead, status_code=status.HTTP_200_OK
)
def actualizar_cliente(cliente: schemas.ClienteCreate, id: int = Path(..., gt=0)):
    # Usamos ClienteCreate porque en tu servicio la función espera un data:ClienteCreate (reemplazo total)
    actualizado = services.actualizar_cliente(id, cliente)
    if not actualizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado"
        )
    return actualizado


# ---------------------------------------------------------
# BORRADO LÓGICO (Desactivar)
# Método: PUT | Endpoint: /clientes/{id}/desactivar | Estado: 200 OK
# ---------------------------------------------------------
@router.put(
    "/{id}/desactivar",
    response_model=schemas.ClienteRead,
    status_code=status.HTTP_200_OK,
)
def borrado_logico(id: int = Path(..., gt=0)):
    desactivado = services.desactivar_cliente(id)
    if not desactivado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado"
        )
    return desactivado