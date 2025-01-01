## About
Visualizing UFO Data in the ufo.csv file using Python and tkinter

## Files
### ufo.csv
* CSV file with the UFO data
* Date, time, duration, shape, description, publication date, city, state, longitude, latitude etc.

### ufoData.py
* Python data visualization
* Libraries: matplotlib.pyplot, pandas, numpy
* Pie chart, line graph, bar graph
  * Sorted data into groups if needed


### ufoGui.py & background.jpeg
* GUI using tkinter and PIL
* imports class 'UfoGraph' from ufoData.py
* background.jpeg as background of GUI
* GUI includes three buttons that calls each graph

### main.py
* imports class 'UfoGui' from ufoGui.py
* this file is run
