# Student checker
from pyscript import display, document

def club_check(e):
    document.getElementById('result').innerHTML = ' '

    persons_input = str(document.getElementById('firstname').value)
    persons_input2 = str(document.getElementById('lastname').value)

    input = str(persons_input) + " " + str(persons_input2)
    inputlast = input.title()

    allowed_people = ['George Washington', 'Abraham Lincoln', 'John Kennedy', 'Teddy Roosevelt']
    persons_checker = inputlast in allowed_people
    display_message = (f'Sorry {inputlast}, you are not included in the club', f'Congratulations {inputlast}, you are part of the club!')

    display(display_message[persons_checker], target='result')