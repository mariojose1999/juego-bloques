from ursina import *
from ursina.prefabs.firstp_person_controller import FirstPersonController
from random import uniform

app = Ursina()

window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = True

# Sonidos
sonido1 = Audio('colocar.mp3', autoplay=False)
sonido2 = Audio('eliminar.mp3', autoplay=False)
sonidos_reproducidos = False

# Suelo
ground = Entity(Model= 'phone', scale=100, Texture'white_cube', texture_scale=(100,100), collider='box', color=color.gray)

# Jugador
player = FirstPersonController()
player.gravity = 0  # Para que pueda volar
player.cursor.visible = True
player.speed = 5
player.jump_height = 0  # Desactivamos el salto para evitar errores con gravedad
player.y = 2

# Enemigos (cubos rojos)
enemigos = []
for i in range(10):
    enemigo = Entity(model='cube', color=color.red, scale=1.5, position=(uniform(-20,20), 0.75, uniform(-20,20)), collider='box')
    enemigos.append(enemigo)

# Reproducir sonidos automáticamente al iniciar
def input(key):
    global sonidos_reproducidos
    if key == 'escape':
        application.quit()

# Volar con espacio y shift
def update():
    global sonidos_reproducidos

    if not sonidos_reproducidos:
        sonido1.play()
        invoke(sonido2.play, delay=2.5)  # Reproduce el segundo sonido 2.5s después del primero
        sonidos_reproducidos = True

    if held_keys['space']:
        player.y += time.dt * 5  # Subir
    if held_keys['left shift']:
        player.y -= time.dt * 5  # Bajar

app.run()
