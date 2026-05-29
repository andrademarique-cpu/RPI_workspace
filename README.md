# RPI_workspace 🤖

Librería DIY modular para el control de motores, servos y sensores en la Raspberry Pi 5.

Este proyecto está diseñado para sortear las limitaciones de hardware PWM y las restricciones de entorno de Python 3.13 en la nueva arquitectura del chip RP1 de la Raspberry Pi 5, utilizando `gpiozero` y los drivers nativos del sistema.

## 🚀 Instalación y Configuración

Sigue estos pasos para clonar el repositorio y configurar el entorno virtual de forma segura, permitiendo el acceso a los pines GPIO de la Raspberry Pi.

1. **Clona el repositorio** en tu Raspberry Pi y entra a la carpeta:
```bash
git clone [https://github.com/andrademarique-cpu/RPI_workspace.git](https://github.com/andrademarique-cpu/RPI_workspace.git)
cd RPI_workspace
python3 -m venv --system-site-packages .workspace
```

y ahora en el bash para activar el entorno
```bash
source .workspace/bin/activate
pip install -e .
```