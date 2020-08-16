import ui

from anchors.observer import on_change


class Mover(ui.View):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_subview(
            ui.Label(
                text='Move me',
                text_color='white',
                alignment=ui.ALIGN_CENTER,
                center=self.bounds.center(),
                flex='RTBL',
            )
        )
    
    def touch_moved(self, t):
        self.center += t.location - t.prev_location


v = ui.View()

mover = Mover(
    background_color='darkred',
    center=v.bounds.center(), flex='RLTB',
)

mirror = ui.View(
    background_color='lightgrey'
)

v.add_subview(mover)
v.add_subview(mirror)

def move_mirror(sender):
    mirror.center = sender.center + (0, 200)

on_change(mover, move_mirror)
    
v.present('fullscreen', animated=False)

