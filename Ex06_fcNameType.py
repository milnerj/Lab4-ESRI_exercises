# Created by: Jacob Milner
# Assignment: TGIS 501A - Lab 4 - Exercise 06 - Challenge 1
# Date: 10/22/2014
# Purpose: Write a script that reads all feature classes in a workspace and prints the name of each feature class and the geometry type of that feature class in the following format: "streams is a point feature class"

import arcpy
from arcpy import env
env.workspace = "C:/Users/Jacob/Desktop/EsriPress/Python/Data/Exercise06"
fc_list = arcpy.ListFeatureClasses()
for fc in fc_list:
	describe = arcpy.Describe(fc)
print "{0} is a {1} feature class".format(describe.basename, describe.shapeType)
