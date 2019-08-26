from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings, merge_key_bindings
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.styles import Style, merge_styles

from .peco_ui import PecoContainer


class Peco(object):
    def __init__(self, choices):
        self.choices = choices
        self.container = PecoContainer(choices)

    @property
    def key_bindings(self):
        kb = KeyBindings()

        @kb.add("c-c")
        @kb.add("c-q")
        def terminate(event):
            event.app.exit(None)

        return merge_key_bindings([self.container.key_bindings, kb])

    @property
    def styles(self):
        app_styles = Style.from_dict({})
        return merge_styles([self.container.styles, app_styles])

    def run(self):
        app = Application(
            layout=Layout(self.container, focused_element=self.container.input_area),
            key_bindings=self.key_bindings,
            style=self.styles,
            mouse_support=False,
            full_screen=True,
        )
        return app.run()
