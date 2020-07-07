import ui

import anchor.observer as nsobserver

v = ui.View()

class Observer:
    
    def __init__(self, view):
        self.view = view
        
    def on_change(self):
        self.view.mirror.center = self.view.center + (0, 200)

class Mover(ui.View):
    
    def __init__(self, mirror, **kwargs):
        super().__init__(**kwargs)
        self.mirror = mirror
        self.add_subview(
            ui.Label(
                text='Move me',
                text_color='white',
                alignment=ui.ALIGN_CENTER,
                center=self.bounds.center(),
                flex='RTBL',
            )
        )
        self.observer = Observer(self)
    
    def touch_moved(self, t):
        self.center += t.location - t.prev_location

mirror = ui.View(
    background_color='lightgrey'
)

mover = Mover(mirror,
    background_color='darkred',
    flex='RLTB',
)

observer = nsobserver.NSKeyValueObserving()
observer.observe(mover)

v.add_subview(mover)
v.add_subview(mirror)

mover.center = v.bounds.center()
    
v.present('fullscreen', animated=False)
