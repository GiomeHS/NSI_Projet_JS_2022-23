import ursina
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from direct.stdpy import thread
from ursina.prefabs.health_bar import HealthBar

# constantes
FPS_MAX = 75
earth_distance = 15
earth_speed = 1/365.25

if __name__== '__main__':
  app = ursina.Ursina(borderless = True)
  ursina.window.title = 'prototype'
  screen = None

  # déplacement
  player = FirstPersonController(gravity = 0)
  # élement
  sun = ursina.Entity(model = 'sphere', position = ursina.Vec3(0, 0, 1), texture = "8k_sun", scale = (5,5,5), shader=lit_with_shadows_shader)
  earth = ursina.Entity(model = 'sphere', position = ursina.Vec3(15, 0, 1), texture = "2k_earth", shader=lit_with_shadows_shader)
  floor = [[ ursina.Entity(visible = False, model = 'cube', position = ursina.Vec3(i, -1, j), texture = 'white_cube') for j in range(10)] for i in range(10)]
  sky_texture = ursina.load_texture("2k_stars")
  ursina.Sky(texture = sky_texture, shader = None)
  # shader
  light = ursina.PointLight(parent=sun, shadows=False)

  # update (boucle itérative built-in de Ursina)
  def update():
    # invoke(print_time, delay = 0)
    angle = ursina.time.time() * earth_speed
    x = earth_distance * ursina.math.cos(angle)
    y = earth_distance * ursina.math.sin(angle)
    z = 0
    direction = (sun.position - earth.position).normalized()
    earth.position = sun.position + direction * z + earth.right * x + earth.forward * y
    earth.rotation_y -= 1

  # pour fermer la fenêtre (touche echap)
  def input(key):
    if key == "escape":
      quit()
     
  app.run()
