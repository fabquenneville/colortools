#!/usr/bin/env python3

# Normal import
try:
    from colortools.library.tools import load_arguments, get_css_colors, get_css_colors_webcolors, generate_css_fonts, generate_css_backgrounds, generate_csv
# Allow local import for development purposes
except ModuleNotFoundError:
    from library.tools import load_arguments, get_css_colors, get_css_colors_webcolors, generate_css_fonts, generate_css_backgrounds, generate_csv

def main():
    arguments = load_arguments()
    colors = get_css_colors()
    if len(colors) < 1:
        colors = get_css_colors_webcolors()
    if "cssfonts" in arguments["tasks"]:
        generate_css_fonts(colors)
    if "cssbgs" in arguments["tasks"]:
        generate_css_backgrounds(colors)
    if "csv" in arguments["tasks"]:
        generate_csv(colors)

if __name__ == '__main__':
    main()
