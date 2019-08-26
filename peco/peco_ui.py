import os

from prompt_toolkit.buffer import Buffer
from prompt_toolkit.key_binding import KeyBindings, merge_key_bindings
from prompt_toolkit.keys import Keys
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import TextArea

from .logger import Logger

v = os.getenv("PECO_PY_LOGGER")
logger = Logger("./log.txt", v == "on")


class ChoicesArea(object):
    container_style = "class:choice-area"
    default_style = "class:choice-item"
    selected_style = "class:choice-item.selected"

    def __init__(self, choices, get_text_func):
        assert len(choices) > 0

        self.choices = choices
        self.filtered_choices = choices
        self.current_value = choices[0]
        self._selected_index = 0
        self.get_filter_text = get_text_func

        # Control and window.
        self.control = FormattedTextControl(
            self._get_choice_fragments, focusable=False, show_cursor=False
        )

        self.window = Window(content=self.control, style=self.container_style)

    @property
    def styles(self):
        return Style.from_dict({"choice-item.selected": "underline bg:#ff80ab #ffffff"})

    @property
    def key_bindings(self):
        # Key bindings.
        kb = KeyBindings()

        @kb.add("up")
        @kb.add("c-p")
        def up(event):
            self._selected_index = max(0, self._selected_index - 1)

        @kb.add("down")
        @kb.add("c-n")
        def down(event):
            self._selected_index = min(
                len(self.filtered_choices) - 1, self._selected_index + 1
            )

        @kb.add("pageup")
        @kb.add("c-u")
        def _(event):
            w = event.app.layout.current_window
            self._selected_index = max(
                0, self._selected_index - len(w.render_info.displayed_lines)
            )

        @kb.add("pagedown")
        @kb.add("c-d")
        def pagedown(event):
            w = event.app.layout.current_window
            self._selected_index = min(
                len(self.filtered_choices) - 1,
                self._selected_index + len(w.render_info.displayed_lines),
            )

        @kb.add("enter")
        def enter(event):
            self._handle_enter()
            event.app.exit(self.current_value)

        return kb

    def _handle_enter(self):
        if len(self.filtered_choices) == 0:
            self.current_value = None
            return
        self.current_value = self.filtered_choices[self._selected_index]

    def _get_choice_fragments(self):
        text = self.get_filter_text()
        self.filtered_choices = [c for c in self.choices if c.find(text) >= 0]
        self._selected_index = max(
            0, min(self._selected_index, len(self.filtered_choices) - 1)
        )

        def one_item(i, item):
            if i == self._selected_index:
                style = self.selected_style
            else:
                style = self.default_style

            return style, item + "\n"

        result = []
        for i, item in enumerate(self.filtered_choices):
            result.append(one_item(i, item))
            # result.append(("class:newline", "\n"))

        return result

    def __pt_container__(self):
        return self.window


class PecoContainer(object):
    def __init__(self, choices):
        self.choices = choices
        input_area = TextArea(
            height=1,
            prompt="QUERY> ",
            style="class:input-area",
            multiline=False,
            wrap_lines=False,
        )

        choices_area = ChoicesArea(choices, (lambda: input_area.text))

        self.window = HSplit([input_area, choices_area])

        self.input_area = input_area
        self.choices_area = choices_area

    @property
    def key_bindings(self):
        return self.choices_area.key_bindings

    @property
    def styles(self):
        return self.choices_area.styles

    def __pt_container__(self):
        return self.window
