# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 12:52:17 2022

@author: tuanv
"""

import arcpy
from arcpy import env
import sys
env.workspace = r"C:\Users\tuanv\Desktop\GIS_Programing\Lab3\data"
sys.path[0]
env.overwriteOutput = 1


aoi = 'interestAreas.shp'
meshPoints = 'meshPoints.shp'

xMin = []
yMin = []
height = []
width = []

with arcpy.da.SearchCursor(aoi,['SHAPE@']) as cursor:
    for row in cursor:
        xMin.append(row[0].extent.XMin)
        yMin.append (row[0].extent.YMin)
        height.append(row[0].extent.height)
        width.append(row[0].extent.width)




CoordXY = []

listCoordX1= []
listCoordY1= []
for item in range(0,int(width[0]),2000):
    x = xMin[0] + item
    listCoordX1.append(x) 
for i in range(0,int(height[0]),2000):
    y = yMin[0] + i
    listCoordY1.append(y)
for x in listCoordX1:
    for y in listCoordY1:
        CoordXY.append((x,y))

listCoordX2= []
listCoordY2= []
for item in range(0,int(width[1]),2000):
    x = xMin[1] + item
    listCoordX2.append(x) 
for i in range(0,int(height[1]),2000):
    y = yMin[1] + i
    listCoordY2.append(y)
for x in listCoordX2:
    for y in listCoordY2:
        CoordXY.append((x,y))

listCoordX3= []
listCoordY3= []
for item in range(0,int(width[2]),2000):
    x = xMin[2] + item
    listCoordX3.append(x) 
for i in range(0,int(height[2]),2000):
    y = yMin[2] + i
    listCoordY3.append(y)
for x in listCoordX3:
    for y in listCoordY3:
        CoordXY.append((x,y))


if arcpy.Exists(meshPoints):
    arcpy.management.Delete(meshPoints)
    
arcpy.CreateFeatureclass_management(env.workspace,meshPoints,'MULTIPOINT')

point = arcpy.Point()
array = arcpy.Array()

for i in CoordXY:
    point.X = i[0]
    point.Y = i[1]
    array.append(point)

mesh = arcpy.Multipoint(array)
with arcpy.da.InsertCursor(meshPoints,['SHAPE@']) as cursor:
    cursor.insertRow([mesh])

meshPoints_clipped = 'meshPoints_clipped.shp'
arcpy.Clip_analysis(meshPoints,aoi,meshPoints_clipped)

meshPoints_clipped_buff = 'meshPoints_clipped_buff.shp'
arcpy.analysis.Buffer(meshPoints_clipped,meshPoints_clipped_buff,500)    
    
    


    