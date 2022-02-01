# IMPORTANT: IF YOU WANT TO RUN THIS SCRIPT YOU NEED TO BE IN THE PROJECT DIR
from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

sizes = [
    "xs",
    "sm",
    "lg",
    "1x",
    "2x",
    "3x",
    "4x",
    "5x",
    "6x",
    "7x",
    "8x",
    "9x",
    "10x",
]

file_yaml = "node_modules/@fortawesome/fontawesome-free/metadata/icons.yml"

with open("wagtailiconify/choices/fontawesome.py", "w+") as choices_py:

    choices_py.write("SIZES = [\n")

    for size in sizes:
        choices_py.write(f"    ('fa-{size}', '{size}'),\n")

    choices_py.write("]\n\n")

    choices_py.write("ICONS = [\n")
    with open(file_yaml, "r+") as stream:

        icons = load(stream, Loader=Loader)

        for icon in icons:
            for font_type in icons[icon]["styles"]:
                if font_type == "regular":
                    coded = "far"
                elif font_type == "solid":
                    coded = "fas"
                elif font_type == "brands":
                    coded = "fab"
                choices_py.write(
                    f"    ('{coded} fa-{icon}', '{icon} ({font_type})'),\n"
                )

    choices_py.write("]\n")
