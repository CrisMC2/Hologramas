
-----

## 🚀 Configuración y Dependencias del Proyecto

Esta sección detalla los pasos exactos para configurar el entorno de desarrollo y las dependencias para ejecutar este proyecto de **Inteligencia Artificial/Machine Learning**.

### 1\. Requisitos de Python

Asegúrate de que tienes instalada la versión de Python requerida. Se recomienda usar **Python 3.11** junto con **PIP**.

| Requisito | Versión Específica |
| :--- | :--- |
| **Python** | **3.11.x** |
| **PIP** | Instalado por defecto con Python |

Verifica la versión de Python en tu terminal:

```bash
python3.11 --version  # O simplemente 'python --version'
# Debería mostrar: Python 3.11.x
```

### 2\. Creación y Activación del Entorno Virtual (`venv`)

Es **obligatorio** aislar las dependencias del proyecto. Usaremos `venv` para crear un entorno limpio y asegurarnos de que la instalación de librerías sea reproducible.

**Paso 2.1: Crear el Entorno Virtual**

Crea el entorno virtual llamado `venv` dentro de la carpeta del proyecto:

```bash
python -m venv venv
```

**Paso 2.2: Activar el Entorno Virtual**

**¡Importante\!** Debes activar el entorno antes de instalar cualquier dependencia. Verás el prefijo `(venv)` aparecer en tu terminal cuando esté activo.

| Sistema Operativo | Comando de Activación (Copiar y Pegar) |
| :--- | :--- |
| **Linux/macOS** | `source venv/bin/activate` |
| **Windows (CMD o Git Bash)** | `venv\Scripts\activate` |
| **Windows (PowerShell)** | `.\venv\Scripts\Activate.ps1` |

Una vez ejecutado, tu terminal cambiará a algo como: `(venv) C:\ruta\a\tu\proyecto>`.

### 3\. Instalación de Dependencias

Con el entorno `(venv)` **activo y visible** en tu terminal, puedes proceder a instalar todas las librerías necesarias utilizando el archivo **`requirements.txt`**.

**Instala las dependencias:**

```bash
pip install -r requirements.txt
```

**Verificación:** La instalación procederá **solo bajo el prefijo `(venv)`**. Esto garantiza que todas las librerías se instalen en el entorno aislado `venv`.

-----

4. Ejecución del Proyecto
Una vez que todas las dependencias estén instaladas, el proyecto se ejecuta llamando al script principal, main.py, desde el entorno virtual activo.

Ejecuta el script principal:

Bash

```bash
(venv) python main.py
```
El script comenzará la ejecución del modelo de IA/ML.
