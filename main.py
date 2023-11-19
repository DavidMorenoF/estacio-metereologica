
def on_button_pressed_a():
    led.plot_bar_graph(input.temperature(), 50)
input.on_button_pressed(Button.A, on_button_pressed_a)