import PySimpleGUI as sg
from random import randint

dice = lambda: randint(1, 6)
graph = sg.Graph(
    canvas_size=(512, 512),
    graph_bottom_left=(0, 0),
    graph_top_right=(512, 512),
    drag_submits=True,
    enable_events=True,
    key="dice",
)
layout = [[graph], [sg.Button("roll")]]
window = sg.Window("Dice", layout, finalize=True)
picture = graph.draw_image(filename=f"inverted-dice-{dice()}.png", location=(0, 512))
while True:
    event, values = window.read()
    print(event)
    if event == "roll":
        window["dice"].delete_figure(picture)
        picture = graph.draw_image(
            filename=f"inverted-dice-{dice()}.png", location=(0, 512)
        )
    if event in (None, "Exit"):
        break
window.close()
