#!/bin/bash

# 1. Asegurarnos de estar en la carpeta de trabajo correcta
cd /home/p4/RPI_workspace

# 2. Activar el entorno virtual correctamente con "source"
source .workspace/bin/activate

# 3. Ejecutar el script principal de robótica
python main.py

# 4. (Opcional) Desactivar el entorno cuando el script de Python termine
deactivate