"""
Plotting trajectories over time on Google Earth with Python

This python script transforms one or several temporal trajectories composed of a set of nodes and links 
into a KML file plotting these trajectories over time on Google Earth.

More specifically, the script takes as input two .csv files: Nodes.csv and Links.csv with column names and 
a semicolon ";" as value separator.

Nodes.csv is composed of 3 columns providing geographical information about the nodes, each row represents 
a node:

   1. Node ID
   2. Longitude of the node
   3. Latitude of the node

Links.csv is composed of 5 columns providing information about the "temporal" links between two nodes defined
in Nodes.csv. The links should be sorted by starting time. Each row represents a link:

   1. Link ID (numeric)
   2. Node of origin
   3. Node of destination
   4. Departure time of the link from the node of origin (date format '2014-01-01T08:00:00Z')
   5. Arrival time of the link to the node of destination (date format '2014-01-01T08:00:00Z')

The script has also 7 parameters to set the kml movie's time windows, the nodes' and links' visibility 
(remaining time on screen), the nodes' and links' styles and the name of the output file. Their values can be set 
directly into the Python script kmlMovie.py.

   1. begin: Starting time of the movie (date format '2014-01-01T08:00:00Z')
   2. end: Ending time of the movie (date format '2014-01-01T08:00:00Z')
   3. delay_node: Number of seconds the nodes remain visible after their creation
   4. delay_link: Number of seconds the links remain visible after their creation
   5. hrefnodestyle: Hyperlink leading to the node style file
   6. rgbcolorlink: Define the links color with an rgb code
   7. output_file: Name of the output file

Copyright 2015 Maxime Lenormand. All rights reserved. Code under License GPLv3.
"""

# ******************************************** IMPORTS *******************************************************
# ************************************************************************************************************

import math
import numpy as np
import simplekml
from datetime import datetime 


# ********************************************* LOAD DATA ****************************************************
# ************************************************************************************************************

#Parameters
begin = '2014-01-01T07:59:00Z'                                      #Start time of the movie 
end = '2014-01-01T08:06:00Z'                                        #End time of the movie 
delay_node = 100                                                    #Nodes' remaining time on screen
delay_link = 100                                                    #Links' remaining time on screen
hrefnodestyle = 'http://bit.ly/1Q57CMA'                             #Hyperlink node style
rgbcolorlink = [70,147,226]                                         #RGB color link
output_file = 'Movie.kml'                                           #Name of the output file
 
#Import nodes
nodes_file = open('Nodes.csv')                               
col = nodes_file.readline().rstrip('\n\r').split(';')  #Colnames 
nodes = {}
for line in nodes_file:
        attr = line.rstrip('\n\r').split(';')
        nodes[str(attr[0])] = [float(attr[1]),float(attr[2])]

#Import links
links_file = open('Links.csv')                               
col = links_file.readline().rstrip('\n\r').split(';')  #Colnames 
links = {}
for line in links_file:
        attr = line.rstrip('\n\r').split(';')
        links[attr[0]] = [str(attr[1]),str(attr[2]),str(attr[3]),str(attr[4])]
        
# ********************************************* LOAD FUNCTIONS ***********************************************
# ************************************************************************************************************

#From date format to UNIX format
def TZtoUNIX(date):
  sec = datetime.strptime(date,'%Y-%m-%dT%H:%M:%SZ')
  sec=(sec-datetime(1970,1,1)).total_seconds()      
  return sec

#From UNIX format to date format
def UNIXtoTZ(sec):
  date = datetime.utcfromtimestamp(sec).strftime('%Y-%m-%dT%H:%M:%SZ')    
  return date

#Compute the coordinates of an intermediate point on a great circle path between two points origin->dest.
#The location of the intermediate point on the arc can be tuned with the parameter fraction to obtain
#a point located at a distance fraction*(great circle distance between origin and dest) from the origin.       
def IntermediatePoint(origin, dest, fraction):
  
  #Earth spherical radius in meters
  r = 6371*1000
  
  #Calculate great circle distance between origin and dest in radians
  lon1 = (math.pi/180.)*origin[0]
  lat1 = (math.pi/180.)*origin[1] 
  lon2 = (math.pi/180.)*dest[0] 
  lat2 = (math.pi/180.)*dest[1]

  dlon = lon2-lon1
  dlat = lat2-lat1

  d = math.pow(math.sin(dlat/2.),2)+math.cos(lat1)*math.cos(lat2)*math.pow(math.sin(dlon/2.),2)    
  d = 2*math.asin(min(1,math.sqrt(d)))
  
  #Calculate longitude and latitude of the intermediate point
  A = math.sin((1-fraction)*d)/math.sin(d)
  B  =math.sin(fraction*d)/math.sin(d)
  
  x = A*math.cos(lat1)*math.cos(lon1) + B*math.cos(lat2)*math.cos(lon2)
  y = A*math.cos(lat1)*math.sin(lon1) + B*math.cos(lat2)*math.sin(lon2)
  z = A*math.sin(lat1)                + B*math.sin(lat2)
  
  lon = (180./math.pi)*math.atan2(y,x)
  lat = (180./math.pi)*math.atan2(z,math.sqrt(math.pow(x,2)+math.pow(y,2)))
  
  #Calculate altitude in meters in a sinusoidal trajectory
  h = d*r*0.3
  h = h*math.sin(math.pi*fraction)
  
  return [lon, lat, h]

 
# ********************************************* MAIN *********************************************************
# ************************************************************************************************************

#Create kml file
kml = simplekml.Kml()

#Node style
nodestyle = simplekml.Style()
nodestyle.iconstyle.icon.href = hrefnodestyle
nodestyle.iconstyle.scale = 0.5

#Dummy node to define the time window
dummynodestyle = simplekml.Style()
dummynodestyle.iconstyle.icon.href = ''
dummynode = [nodes[nodes.keys()[0]][0],nodes[nodes.keys()[0]][1]]
dummynode = kml.newpoint(name='', coords=[tuple(dummynode)])
dummynode.timespan.begin = begin
dummynode.timespan.end = end
dummynode.style = dummynodestyle

#Loop over the links
for key in sorted(links):
  
    #Link  
    link = links[key] 
    time_departure = link[2]    
    time_arrival = link[3]
    duration = TZtoUNIX(link[3]) - TZtoUNIX(link[2])
    
    #Nodes origin & destination
    node1 =[nodes[link[0]][0],nodes[link[0]][1]]
    node2 =[nodes[link[1]][0],nodes[link[1]][1]]
      
    origin = kml.newpoint(name='', coords=[tuple(node1)])
    origin.timespan.begin = time_departure
    origin.timespan.end = UNIXtoTZ(TZtoUNIX(time_departure) + delay_node)
    origin.style = nodestyle
    
    dest = kml.newpoint(name='', coords=[tuple(node2)])
    dest.timespan.begin = time_arrival
    dest.timespan.end = UNIXtoTZ(TZtoUNIX(time_arrival) + delay_node)
    dest.style = nodestyle  
    
    #Trajectory
    p0 = (node1[0], node1[1], 0)    #First point 
    for f in np.arange(0,1.05,0.05):
        p = IntermediatePoint(node1, node2, f)
        pi = (p[0],p[1],p[2])      
        line = kml.newlinestring(coords=[p0,pi], tessellate=1, altitudemode='relativeToGround')
        line.style.linestyle.width = 5
        line.style.linestyle.color = simplekml.Color.rgb(rgbcolorlink[0],rgbcolorlink[1],rgbcolorlink[2], a=255) 
        line.timespan.begin = UNIXtoTZ(TZtoUNIX(time_departure) + int(f*duration))
        line.timespan.end = UNIXtoTZ(TZtoUNIX(time_departure) + int(f*duration) + delay_link)     
        p0=pi 

#Save kml file 
kml.save(output_file)
