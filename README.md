## **Práctico n°2:** FastAPI.

El trabajo práctico n°3 profundiza en el desarrollo backend utilizando Python, explorando la creación de una API RESTful modular y robusta mediante el framework **FastAPI**. Este proyecto es una modificación del [repositorio original](https://github.com/profcarlosamartinez/fastapi_backend), donde se le ha implementado la gestión de clientes.

---

### 🛠️ **Tecnologías y conceptos cubiertos.**

* **Arquitectura Modular:** Separación de responsabilidades dividiendo el sistema en módulos independientes. Uso de `routers` (controladores de endpoints), `services` (lógica de negocio y persistencia) y `schemas` (definición de estructuras de datos).

* **Validación de datos y Modelos:** Uso de la librería `Pydantic` para definir estrictamente los datos de entrada y salida (*Response Models*). Implementación de validaciones automáticas avanzadas utilizando `EmailStr`, límites numéricos y expresiones regulares (`pattern`).

* **Manejo de Parámetros:** Uso de parámetros de ruta (`Path`) para identificar recursos únicos (como búsquedas por ID) y parámetros de consulta (`Query`) para añadir paginación y filtros avanzados (ej. filtrar clientes según su estado activo/inactivo).

* **Gestión de Errores y Códigos HTTP:** Implementación de `HTTPException` para devolver respuestas controladas al cliente con sus respectivos status codes (201 para creaciones exitosas, 400 frente a reglas de negocio no cumplidas como emails duplicados, 404 para elementos inexistentes y 422 para errores de formato).

* **Operaciones CRUD y Reglas de Negocio:** Desarrollo de endpoints para dar de alta, listar, actualizar totalmente (PUT) y aplicar borrado lógico (desactivación) de registros. Incorporación de lógica de negocio, como la verificación de alertas de stock mínimo.

---

### 🚀 **¿Cómo ejecutarlo y ponerlo a prueba?**

Para poner a prueba la API en tu entorno local, sigue estos pasos:
1. **Activar el entorno virtual:** Desde tu terminal y activa el entorno.
   * En Windows: `.venv\Scripts\activate`
   * En Linux/Mac: `source .venv/bin/activate`

2. **Instalar las dependencias:** `pip install -r requirements.txt`

3. **Ejecutar el servidor local**: `uvicorn app.main:app --reload`

4. **Probar los Endpoints**:
    * Swagger UI: http://127.0.0.1:8000/docs
    * REST Client: Mediante el archivo: `tests/test_api.http`
