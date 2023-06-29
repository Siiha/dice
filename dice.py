import PySimpleGUI as sg
from random import randint
dice = lambda: randint(1,6)
graph = sg.Graph(
    canvas_size=(512,512),
    graph_bottom_left=(0,0),
    graph_top_right=(512, 512),
   drag_submits=True,
    key='dice')
layout = [
   [graph],
   [sg.Button("roll")]]
window = sg.Window('Dice', layout, finalize=True)
pic = lambda: graph.draw_image(filename=f"inverted-dice-{dice()}.png",location=(0, 512))
picture = pic()
while True:
   event, values = window.read()
   if event == 'roll':
	   graph.delete_figure(picture)
	   picture = pic()
   if event in (None, 'Exit'):
      break
window.close()
