# Created by: Jacob Milner
# Assignment: TGIS 501A - Lab 4 - Exercise 06 - Challenge 2
# Date: 10/22/2014
# Purpose: Write a script that reads all files in a personal/file gdb and copies only the polygon feature classes to a new file gdb

import arcpy
from arcpy import env
env.workspace = "C:/Users/Jacob/Desktop/EsriPress/Python/Data/Exercise06/Results/NM.gdb"
fc_list = arcpy.ListFeatureClasses()
arcpy.CreateFileGDB_management("C:/Users/Jacob/Desktop/EsriPress/Python/Data/Exercise06/Results", "NM_new.gdb")
for fc in fc_list:
	describe = arcpy.Describe(fc)
	if describe.shapeType == "Polygon":
		arcpy.Copy_management(fc, "C:/Users/Jacob/Desktop/EsriPress/Python/Data/Exercise06/Results/NM_new.gdb/" + fc)