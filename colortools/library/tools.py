#!/usr/bin/env python3
'''
    These are various tools used by mediacurator
'''

import sys
import webcolors
import csv

def load_arguments():
    '''Get/load command parameters 

    Args:

    Returns:
        arguments: A dictionary of lists of the options passed by the user
    '''
    arguments = {
        "directories":list(),
        "files":list(),
        "inputs":list(),
        "filters":list(),
        "outputs":list(),
        "printop":list(),
    }

    for arg in sys.argv:
        # Confirm with the user that he selected to delete found files
        if "-del" in arg:
            exit()
        elif "-in:" in arg:
            arguments["inputs"] += arg[4:].split(",")
        elif "-filters:" in arg:
            arguments["filters"] += arg[9:].split(",")
        elif "-out:" in arg:
            arguments["outputs"] += arg[5:].split(",")
        elif "-print:" in arg:
            arguments["printop"] += arg[7:].split(",")
        elif "-files:" in arg:
            arguments["files"] += arg[7:].split(",,")
        elif "-dirs:" in arg:
            arguments["directories"] += arg[6:].split(",,")

    return arguments

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

def generate_all_colors():
    '''

    Args:

    Returns:
        arguments: A dictionary of lists of the options passed by the user
    '''
    results = {}
    tmp = template = {
        "hex": None,
        "red": None,
        "green": None,
        "blue": None,
        "name_english": None,
    }
    for red in range(256):
        tmp["red"] = red
        for green in range(256):
            tmp["green"] = green
            for blue in range(256):
                tmp["blue"] = blue

                redhex = str(format(red, 'x')).upper()
                if len(redhex) < 2:
                    redhex = f"0{redhex}"

                greenhex = str(format(green, 'x')).upper()
                if len(greenhex) < 2:
                    greenhex = f"0{greenhex}"

                bluehex = str(format(blue, 'x')).upper()
                if len(bluehex) < 2:
                    bluehex = f"0{bluehex}"

                tmp["hex"] = f"#{redhex}{greenhex}{bluehex}"
                closest_name = actual_name = get_colour_name((red, green, blue))
                if actual_name:
                    tmp["name_english"] = actual_name
                    results[tmp["hex"]] = tmp
                tmp = template
    return results
                
def get_css_colors_webcolors():
    results = {}
    tmp = template = {
        "hex": None,
        "red": None,
        "green": None,
        "blue": None,
        "name_english": None,
    }
    colors = webcolors.CSS3_HEX_TO_NAMES.items()
    for code, name in colors:
        # print(f"{name}:{code} > red:{code[1:3]}:{int(code[1:3], 16)} - green:{code[3:5]}:{int(code[3:5], 16)} - blue:{code[5:7]}:{int(code[5:7], 16)}")
        tmp["hex"]          = code.upper()
        tmp["red"]          = int(code[1:3], 16)
        tmp["green"]        = int(code[3:5], 16)
        tmp["blue"]         = int(code[5:7], 16)
        tmp["name_english"] = name
        # tmp["name_english"] = webcolors.rgb_to_name((tmp["red"], tmp["green"], tmp["blue"]))
        results[name] = tmp
        print(tmp)
        tmp = template
    print(len(colors))
    return colors

def get_css_colors():
    results = {}
    with open('./misc/colors.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            redhex = str(format(int(row[3]), 'x')).upper()
            if len(redhex) < 2:
                redhex = f"0{redhex}"

            greenhex = str(format(int(row[4]), 'x')).upper()
            if len(greenhex) < 2:
                greenhex = f"0{greenhex}"

            bluehex = str(format(int(row[5]), 'x')).upper()
            if len(bluehex) < 2:
                bluehex = f"0{bluehex}"

            results[row[0]] = {
                "hex": f"#{redhex}{greenhex}{bluehex}",
                "red": int(row[3]),
                "green": int(row[4]),
                "blue": int(row[5]),
                "name_english": row[1],
                "keyword": row[0],
            }
    return results




def generate_css():
    colors = get_css_colors()
#     f = open("./misc/fontcolors.css", "w")
#     for key in colors:
#         print(key)
#         f.write(f"""
# .{colors[key]['keyword']} {{
#     /* {colors[key]['name_english']} */
#     /* color: {colors[key]['hex']} */
#     color: rgba({colors[key]['red']}, {colors[key]['green']}, {colors[key]['blue']}, 1);
# }}

# """)
#     f.close()
    # print(colors)
    with open("./misc/fontcolors.css", 'w') as cssfile:
        for key in colors:
            cssfile.write(f"""
.text_{colors[key]['keyword']} {{
    /* {colors[key]['name_english']} */
    /* color: {colors[key]['hex']} */
    color: rgba({colors[key]['red']}, {colors[key]['green']}, {colors[key]['blue']}, 1);
}}

""")

    with open("./misc/bgcolors.css", 'w') as cssfile:
        for key in colors:
            cssfile.write(f"""
.bg_{colors[key]['keyword']} {{
    /* {colors[key]['name_english']} */
    /* background-color: {colors[key]['hex']} */
    background-color: rgba({colors[key]['red']}, {colors[key]['green']}, {colors[key]['blue']}, 1);
}}

""")