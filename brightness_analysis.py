import json
import collections
import dateutil
import datetime
import numpy as np
import re
import math
import webcolors

def get_time_id(ts):
    index = 0
    for t in timeslots:
        if ts <= t:
            return index
        index += 1
    return -1

def getrgb(originalRgb):
    rgb = re.split('\(|\,|\)', originalRgb)
    return int(rgb[1]), int(rgb[2]), int(rgb[3])

def getLuminance(originalRgb):
    r, g, b = getrgb(originalRgb)
    return math.sqrt( 0.299*pow(r, 2) + 0.587*pow(g, 2) + 0.114*pow(b, 2) )

def closest_colour(requested_colour):
    color = ""
    closest = -1
    for key in colormap.keys():
        r_c, g_c, b_c = getrgb(colormap[key])
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        dist = math.sqrt(rd+gd+bd)
        if closest == -1 or dist < closest:
            closest = dist
            color = key
    return color

def process_color(data):
    data = data["colors"]

    timeslots = [datetime.datetime(2015,11,19,17,0,0), datetime.datetime(2015,11,19,19,0,0), datetime.datetime(2015,11,19,21,0,0), datetime.datetime(2015,11,19,23,0,0), datetime.datetime(2015,11,20,11,0,0),datetime.datetime(2015,11,20,15,0,0), datetime.datetime(2015,11,20,17,0,0), datetime.datetime(2015,11,20,19,0,0)]

    colormap = {}
    colormap["black"] = "rgb(0,0,0)"
    colormap["white"] = "rgb(255,255,255)"
    colormap["red"] = "rgb(255,0,0)"
    colormap["lime"] = "rgb(0,255,0)"
    colormap["blue"] = "rgb(0,0,255)"
    colormap["yellow"] = "rgb(255,255,0)"
    colormap["cyan"] = "rgb(0,255,255)"
    colormap["magenta"] = "rgb(255,0,255)"
    colormap["silver"] = "rgb(192,192,192)"
    colormap["gray"] = "rgb(128,128,128)"
    colormap["maroon"] = "rgb(128,0,0)"
    colormap["olive"] = "rgb(128,128,0)"
    colormap["green"] = "rgb(0,128,0)"
    colormap["purple"] = "rgb(128,0,128)"
    colormap["teal"] = "rgb(0,128,128)"
    colormap["navy"] = "rgb(0,0,128)"

    colors = collections.OrderedDict()
    valence = collections.OrderedDict()
    luminance = collections.OrderedDict()
    colorNames = collections.OrderedDict()
    for record in data:
    	uid = record["uid"]
    	ts = dateutil.parser.parse(record["time"])
    	t = get_time_id(ts)
    	if uid not in colors.keys():
    		colors[uid] = collections.OrderedDict()
		if uid not in valence.keys():
			valence[uid] = collections.OrderedDict()
		if uid not in luminance.keys():
			luminance[uid] = collections.OrderedDict()
		if uid not in colorNames.keys():
			colorNames[uid] = collections.OrderedDict()
		r, g, b = getrgb(record["color"])
		colorNames[uid][t] = closest_colour((r, g, b))
		luminance[uid][t] = getLuminance(record["color"])
		colors[uid][t] = record["color"]
		valence[uid][t] = record["valence"]

	return colorNames

