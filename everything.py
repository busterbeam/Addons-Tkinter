# Every-tkinter code

__version__ = "0.1"


class help:
    help = "Just call \"characters\", \"colors\" or \"fonts\"."
    update = """The "Everything" module currently have characters, colors and fonts.
Next update will have languages (partially)."""

from string import ascii_lowercase, ascii_uppercase, digits

class characters:
    digits = digits
    lowercase = ascii_lowercase
    uppercase = ascii_uppercase
    symbols = r',.!#$%*'
    all_symbols = punctuation


class colors:
    BLUE = "blue"
    GREEN = "green"
    BLACK = "black"
    WHITE = "white"
    RED = "red"
    YELLOW = "yellow"
    BROWN = "brown"
    GRAY = "gray"
    CYAN = "cyan"
    DARK_RED = "darkred"
    PINK = "pink"
    DARK_BLUE = "darkblue"
    DARK_GREEN = "darkgreen"
    LIGHT_BLUE = "lightblue"
    LIGHT_GREEN = "lightgreen"
    MAGENTA = "magenta"
    PURPLE = "purple"
    LIGHT_RED = "lightred"
    DARK_PURPLE = "darkpurple"
    LIGHT_PURPLE = "lightpurple"
    AQUA = "aqua"
    ORANGE = "orange"
    LIME = "lime"
    NAVY = "navy"
    def __str__(self):
        return "Available colors:\n" + '\n'.join(
            v for v in dir(self) if not v.startswith("_")
        ) + "More colors will be added soon."


class fonts:
    ARIAL = "arial"
    HELVETICA = "helvetica"
    COURIER = "courier"
    AHARONI = "aharoni"
    BROADWAY = "broadway"
    CAMBRIA = "cambria"
    COMIC_SANS = "comic sans MS"
    FIXEDSYS = "Fixedsys"
    CALIBRI = "Calibri"
    UBUNTU = "Ubuntu"
    SANS_SERIF = "microsoft sans serif"
    TIMES_NEW_ROMAN = "Times New Roman"
    ROMAN = "Roman"

    class bold:
        ARIAL = "arial", "bold"
        HELVETICA = "helvetica", "bold"
        COURIER = "courier", "bold"
        AHARONI = "aharoni", "bold"
        BROADWAY = "broadway", "bold"
        CAMBRIA = "cambria", "bold"
        COMIC_SANS = "comic sans MS", "bold"
        FIXEDSYS = "Fixedsys", "bold"
        CALIBRI = "Calibri", "bold"
        UBUNTU = "Ubuntu", "bold"
        SANS_SERIF = "microsoft sans serif", "bold"
        TIMES_NEW_ROMAN = "Times New Roman", "bold"
        ROMAN = "Roman", "bold"

    class italic:
        ARIAL = "arial", "italic"
        HELVETICA = "helvetica", "italic"
        COURIER = "courier", "italic"
        AHARONI = "aharoni", "italic"
        BROADWAY = "broadway", "italic"
        CAMBRIA = "cambria", "italic"
        COMIC_SANS = "comic sans MS", "italic"
        FIXEDSYS = "Fixedsys", "italic"
        CALIBRI = "Calibri", "italic"
        UBUNTU = "Ubuntu", "italic"
        SANS_SERIF = "microsoft sans serif", "italic"
        TIMES_NEW_ROMAN = "Times New Roman", "italic"
        ROMAN = "Roman", "italic"
