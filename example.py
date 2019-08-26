from peco import Peco


def alphabets():
    return [chr(ord("A") + i) for i in range(24)]


dummy_choices = alphabets()
selected_choice = Peco(dummy_choices).run()

print("selected:", selected_choice)
