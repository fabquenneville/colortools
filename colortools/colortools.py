#!/usr/bin/env python3

# Normal import
try:
    from colortools.library.tools import load_arguments, generate_css
# Allow local import for development purposes
except ModuleNotFoundError:
    from library.tools import load_arguments, generate_css

def main():
    # colors = generate_all_colors()
    # colors = get_css_colors()
    generate_css()
    # print(colors)

if __name__ == '__main__':
    main()
