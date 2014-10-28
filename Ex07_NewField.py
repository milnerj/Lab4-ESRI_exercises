# Created by: Jacob Milner
# Assignment: TGIS 501A - Lab 4 - Exercise 07 - Challenge 2
# Date: 10/22/2014
# Purpose: Write a script that adds a text field to roads.shp called "FERRY" and populates this field with "YES" or "NO" values depending on the value of the "FEATURE" field

import arcpy
from arcpy import env
env.workspace = "C:/Users/Jacob/Desktop/EsriPress/Python/Data/Exercise07"
fc = "roads.shp"
arcpy.AddField_management(fc, "FERRY", "TEXT", "", "", 3)
cursor = arcpy.da.UpdateCursor(fc, ["FEATURE", "FERRY"])
for row in cursor:
	if row[0] == "Ferry Crossing":
		row[1] = "YES"
	else:
		row[1] = "NO"
	cursor.updateRow(row)