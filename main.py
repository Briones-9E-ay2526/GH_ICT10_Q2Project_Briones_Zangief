# Set Operators
from pyscript import display, document

def makeahugeset(e):
    first = document.getElementById('firstname').value
    last = document.getElementById('lastname').value
    newmember = {f"{first} {last}"} # for displaying the first and last name to the output

    grade_7 = {'George Washington', 'Benjamin Franklin'}
    grade_8 = {'Abraham Lincoln', 'John Adams'}
    grade_9 = {'John Kennedy', 'John Kennedy Jr'}
    grade_10 = {'Theodore Roosevelt', 'Franklin Roosevelt'}

    full_club = grade_7 | grade_8 | grade_9 | grade_10 | newmember # connects everything to output
    fullc_joined = ", ".join(full_club) # to remove the {'',} things and join them

    display(f'All Members: {fullc_joined} Total Members: {len(full_club)}', target='output')