# Ditt namn
# Din klass
# Datum
# Skapa ett spel i 3d

# https://www.ursinaengine.org/documentation.html
# Om du inte kan köra ursina måste du öppna en terminal och skriva in "pip install ursina", klicka sedan på enter.
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


# Create our Ursina-app. Choose size.
app = Ursina(size=(1600, 900))

# This makes the app-window hide the FPS and hide the exit button
window.fps_counter.enabled = False
window.exit_button.enabled = True


# This function is not needed but it makes it more clear
# Put all entities here that is supposed to be in the app when it starts
def createworld():
    for x in range(20):
        for z in range(20):
            Entity(model="cube", texture="brick", position=(x, 0, z), collider="box")


# The update function is what updates the game while its running. For example an object could move 5 positions each time the update runs.
def update():
    pass


# Bakgrundsfärg
window.color = rgb(119, 141, 226)

# Call the createworld function
createworld()

player = FirstPersonController(collider="cube", position=(10, 30, 10))


app.run()
