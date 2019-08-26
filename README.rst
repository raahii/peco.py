peco.py
--

A prompt tool that enables users to select a choice(line) by filtering interactively like [peco](https://github.com/peco/peco). 
This package is not a CLI tool. You can easily use this by passing list of choices in your python code.

```python
from peco import Peco


def alphabets():
    return [chr(ord("A") + i) for i in range(24)]


dummy_choices = alphabets()
selected_choice = Peco(dummy_choices).run()

print("selected:", selected_choice)
# (ex) >> selected: D
```
