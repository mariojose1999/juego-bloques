# Juego 3D con Ursina

Este es un juego 3D básico hecho con la librería **Ursina** en Python. El objetivo es construir y destruir bloques en un mundo 3D, similar a un juego tipo *Minecraft*. Además, tiene características como un ciclo de día/noche, un HUD de vida e inventario, y modos de juego como supervivencia y creativo.

## Características

- **Movimiento y control de personaje**: El personaje puede moverse por el mundo y tiene gravedad y salto controlado.
- **Construcción y destrucción**: Puedes colocar y destruir bloques usando el clic izquierdo y derecho del ratón.
- **Modo creativo y supervivencia**: Puedes alternar entre un modo creativo (sin gravedad y con mayor velocidad) y un modo supervivencia (con gravedad y velocidad estándar).
- **Ciclo de día y noche**: El ciclo del día y la noche se simula cambiando la intensidad de la luz ambiental.
- **Sonidos**: Sonidos cuando colocas y eliminas bloques.
- **Mundo persistente**: Los cambios en el mundo se guardan en un archivo JSON para cargarlo en futuras sesiones.

## Requisitos

- Python 3.7+
- Ursina

## Instalación

1. Clona este repositorio o descarga los archivos.

2. Instala las dependencias:

   ```bash
   pip install ursina
