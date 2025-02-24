# Plotting trajectories over time on Google Earth

## Description

This python script transform one or several temporal trajectories composed of a 
set of nodes and links into a KML file plotting these trajectories over time 
on Google Earth. 

## Inputs

The script  **kmlMovie.py** takes as input two *csv* files with column names, 
**the value separator is a semicolon ";"**. 

* ***Nodes.csv*** is composed of 3 columns providing geographical information 
about the nodes:
  1. Node ID
  2. Longitude of the node
  3. Latitude of the node

* ***Links.csv*** is composed of 5 columns providing information about the 
"temporal" link between nodes defined in ***Nodes.csv***. The links should be
sorted by starting time.
  1. Link ID (numeric)
  2. Node of origin
  3. Node of destination 
  4. Departure time of the link from the node of origin (date format *'2014-01-01T08:00:00Z'*)
  5. Arrival time of the link to the node of destination

## Parameters

The script has also 7 parameters to set the kml movie's time windows, the nodes' 
and links' visibility (remaining time on screen), the nodes' and links' styles 
and the name of the output file. Their values can be set directly into the 
script.

  1. ***begin:*** Starting time of the movie (date format *'2014-01-01T08:00:00Z'*)
  2. ***end:*** Ending time of the movie (date format *'2014-01-01T08:00:00Z'*)
  3. ***delay_node:*** Number of seconds the nodes remain visible after their creation
  4. ***delay_link:*** Number of seconds the links remain visible after their creation
  5. ***hrefnodestyle:*** Hyperlink leading to the node style file
  6. ***rgbcolorlink:*** Define the links color with an rgb code
  7. ***output_file:*** Name of the output file
  
## Execution

You can run the script using the command below to plot three temporal 
trajectories in Madrid.

**python kmlMovies.py**

If you need help, find a bug, want to give me advice or feedback, please contact me!

## Repository mirrors

This repository is mirrored on both GitLab and GitHub. You can access it via the following links:

- **GitLab**: [https://gitlab.com/maximelenormand/KML-movie-Python](https://gitlab.com/maximelenormand/KML-movie-Python)  
- **GitHub**: [https://github.com/maximelenormand/KML-movie-Python](https://github.com/maximelenormand/KML-movie-Python)  

The repository is archived in Software Heritage:

[![SWH](https://archive.softwareheritage.org/badge/origin/https://github.com/maximelenormand/KML-movie-Python/)](https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/maximelenormand/KML-movie-Python)

