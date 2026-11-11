from pyscript import display, document

non_metals = {
    "H":  ("Hydrogen",    1,  1.008),
    "He": ("Helium",      2,  4.0026),
    "C":  ("Carbon",      6,  12.011),
    "N":  ("Nitrogen",    7,  14.007),
    "O":  ("Oxygen",      8,  15.999),
    "F":  ("Fluorine",    9,  18.998),
    "Ne": ("Neon",       10,  20.180),
    "P":  ("Phosphorus", 15,  30.974),
    "S":  ("Sulfur",     16,  32.06),
    "Cl": ("Chlorine",   17,  35.45),
    "Ar": ("Argon",      18,  39.948),
    "Se": ("Selenium",   34,  78.971),
    "Br": ("Bromine",    35,  79.904),
    "Kr": ("Krypton",    36,  83.798),
    "I":  ("Iodine",     53,  126.90),
    "Xe": ("Xenon",      54,  131.29),
    "Rn": ("Radon",      86,  222.00)
} # these are ALL the nonmetal values

def find_the_element(e):
    document.getElementById('output').innerHTML = ''
    elements = document.getElementById('symbol').value # this is where we get the INPUT of the user

    result = non_metals.get(elements, ('Not a nonmetal', '?', '?')) # I saw that .get is in the seatwork, so I'm assuming sir that .get tries to get if X is in Y similiar to "in" but this time it's not boolean values. I guess it works

    #for the ('X', 'Y', 'Z') part, that's where the RESULT will be shown, that's why there's a 0, 1, 2 down here

    document.getElementById('output').innerHTML = f"""
    <p>Symbol: {elements}</p>
    <p>Element: {result[0]}</p>
    <p>Atomic Number: {result[1]}</p>
    <p>Atomic Mass: {result[2]}</p>
    """

    # symbol get shown first, which is why there's a comma to separate itself from the results
    # then the rest will output on the 0, 1, 2. 'Not a nonmetal' is 0, and the rest are 1 and 2
    # <p> is to make it vertical i think, cuz it's a bit wonky with the design if it's not <p>