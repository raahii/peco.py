peco.py (WIP)
--

![demo.gif](https://user-images.githubusercontent.com/13511520/63680188-0b96e500-c82e-11e9-85aa-87687a3cb5c6.gif)

This is a python prompt tool that enables users to select a choice(line) by filtering interactively like [peco](https://github.com/peco/peco). This package is not a CLI tool. 


You can easily use this by passing list of choices in your python code like following:

```python
from peco import Peco

def alphabets():
    return [chr(ord("A") + i) for i in range(26)]

dummy_choices = alphabets()
selected_choice = Peco(dummy_choices).run()

print("selected:", selected_choice)
# >> selected: D
```

### TODO: 

- [ ] highlight line correctly
- [ ] paging
- [ ] separate label and value from choices argument
