# Created by: Jacob Milner
# Assignment: TGIS 501A - Lab 4 - Exercise 05 - Challenge 2
# Date: 10/22/2014
# Purpose: Write a script that runs the Add XY Features tool

import arcpy
from arcpy import env
env.workspace = "C:/Users/Jacob/Desktop/EsriPress/Python/Data/Exercise05"
in_features = "hospitals.shp"
arcpy.AddXY_management(in_features)