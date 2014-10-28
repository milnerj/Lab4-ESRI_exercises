# Created by: Jacob Milner
# Assignment: TGIS 501A - Lab 4 - Exercise 07 - Challenge 1
# Date: 10/22/2014
# Purpose: Write a script that creates a 15000-meter buffer around features classified as an "airport" and a 7500-meter buffer around features classified as a "seaplane base"; output is two separate feature classes, one for each type

import arcpy
from arcpy import env
env.workspace = "C:/Users/Jacob/Desktop/EsriPress/Python/Data/Exercise07"
airport = " \"FEATURE\" = 'Airport'"
seaplane = " \"FEATURE\" = 'Seaplane Base'"
arcpy.Select_analysis("airports.shp", "Results/airports_select.shp", airport)
arcpy.Select_analysis("airports.shp", "Results/seaports_select.shp", seaplane)
arcpy.Buffer_analysis("Results/airports_select.shp", "Results/airports_buffer.shp", "15000 METERS")
arcpy.Buffer_analysis("Results/seaports_select.shp", "Results/seaports_buffer.shp", "7500 METERS")