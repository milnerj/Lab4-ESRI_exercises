# Created by: Jacob Milner
# Assignment: TGIS 501A - Lab 4 - Exercise 05 - Challenge 3
# Date: 10/22/2014
# Purpose: Write a script that runs the Dissolve tool

import arcpy
from arcpy import env
env.workspace = "C:/Users/Jacob/Desktop/EsriPress/Python/Data/Exercise05"
in_features = "parks.shp"
out_features = "parks_dissolved.shp"
# Syntax: Dissolve_management(in_features, out_feature_class, {dissolve_field;dissolve_field...}, {statistics_fields;statistics_fields...}, {multi_part}, {unsplit_lines})
arcpy.Dissolve_management(in_features, out_features, "PARK_TYPE", "", "FALSE")