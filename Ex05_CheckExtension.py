# Created by: Jacob Milner
# Assignment: TGIS 501A - Lab 4 - Exercise 05 - Challenge 4
# Date: 10/22/2014
# Purpose: Write a script determines whether the following extensions are available: ArcGIS 3D Analyst, ArcGIS Network Analyst, ArcGIS Spatial Analyst

import arcpy
if arcpy.CheckExtension("3D") == "Available":
	ext_3D = "3D Analyst "
else:
	ext_3D = ""
if arcpy.CheckExtension("Network") == "Available":
	ext_network = "Network Analyst "
else:
	ext_network = ""
if arcpy.CheckExtension("Spatial") == "Available":
	ext_spatial = "Spatial Analyst "
else:
	ext_spatial = ""
print "The following extensions are available: " + ext_3D + ext_spatial + ext_network