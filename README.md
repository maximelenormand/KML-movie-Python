Plotting trajectories over time on Google Earth with Python
===================================================================================

This python script transform one or several temporal trajectories composed of a set of nodes and links into a KML file plotting 
these trajectories over time on Google Earth. More specifically, the script takes as input two *csv* files with column names, **the value separator 
is a semicolon ";"**. 

* ***Nodes.csv*** is composed of 3 columns providing geographical information abbout the nodes:
  1. Node ID
  2. Longitude of the node
  3. Latitude of the node

* ***Links.csv*** is composed of 5 columns providing information about the "temporal" link between nodes defined in ***Nodes.csv***. The links should be sorted by starting time.
  1. Link ID (numeric)
  2. Node of origin
  3. Node of destination 
  4. Departure time of the link from the node of origin (date format *'2014-01-01T08:00:00Z'*)
  5. Arrival time of the link to the node of destination

*  The script has also 7 parameters to set the kml movie's time windows, the nodes' and links' visibility 
(remaining time on screen), the nodes' and links' styles and the name of the output file. Their values can be set 
directly into the Python script kmlMovie.py.
  1. ***begin:*** Starting time of the movie (date format *'2014-01-01T08:00:00Z'*)
  2. ***end:*** Ending time of the movie (date format *'2014-01-01T08:00:00Z'*)
  3. ***delay_node:*** Number of seconds the nodes remain visible after their creation
  4. ***delay_link:*** Number of seconds the links remain visible after their creation
  5. ***hrefnodestyle:*** Hyperlink leading to the node style file
  6. ***rgbcolorlink:*** Define the links color with an rgb code
  7. ***output_file:*** Name of the output file

The code is not very complicated and you can test it directly to plot three temporal trajectories in Madrid. If you want more details about this script feel free to visit [this post](https://maximelenormand.github.io/Blog/kml-movie-python). 

Enjoy!

If you need help, find a bug, want to give me advice or feedback, please contact me!
You can reach me at maxime.lenormand[at]irstea.fr


  


