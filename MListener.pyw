from pynput import mouse


def on_move(x, y):
    pass


def on_click(x, y, button, pressed):
    pass


def on_scroll(x, y, dx, dy):
    pass

# with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    mouse.Listener.join()
