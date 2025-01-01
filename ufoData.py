#Junhui Park
#December 4, 2024
#AP CSP 5th
#Close Encounters of a Kind - Data Visualization 

# #import library
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  

#class for all graphs
class UfoGraph:
    #opening csv file 
    #renamed the csv file to ufo.csv
    def __init__(self):
        self.df = pd.read_csv('ufo.csv', on_bad_lines='skip')

    #first graph - pie chart
    def graph1PieChart(self):
        #remove whitespaces
        self.df.columns = self.df.columns.str.strip()

        #keep track of counts for each shape
        shapeCounts = self.df['Shape'].value_counts()

        #handling any small shapes with under 300 datas
        otherShapes = shapeCounts[shapeCounts < 300]
        #when shape under 300 datas exist
        if not otherShapes.empty:
            #small data will go in the 'other' space
            shapeCounts['other'] += otherShapes.sum()
            #keep shapes with more than 300 occurences
            shapeCounts = shapeCounts[shapeCounts >= 300]  

        #name of shape
        shapeLabel = shapeCounts.index
        #frequency of shape
        sizes = shapeCounts.values

        #plot pie charts
        plt.pie(sizes, labels = shapeLabel)
        plt.title('UFO Shapes')
        plt.show()

    #second graph - line graph
    def graph2LinePlot(self):
        #remove whitespaces
        self.df.columns = self.df.columns.str.strip()
        
        #extract discovery date of ufo to datetime object in pandas library
        #replace invalid data
        self.df['Discovery Date'] = pd.to_datetime(self.df['Discovery Date'], errors='coerce')

        self.df['Year'] = self.df['Discovery Date'].dt.year

        #group the data by year and count the number of sightings
        decadeFrequecy = self.df['Year'].value_counts().sort_index()

        #plot line graph for the number of ufo sightings over every decade
        plt.figure(figsize=(10, 6))
        #x value & y value
        x = decadeFrequecy.index
        y = decadeFrequecy.values
        #graph x, y value and set line as green
        plt.plot(x, y, color='#4CAF50', linewidth=3)

        #title and label x and y axis
        plt.title('Number of UFO Sightings Every Decade')
        plt.xlabel('Year')
        plt.ylabel('Number of Sightings')
        #show grid
        plt.grid(True)

        #show graph
        plt.show()

    #third graph - bar graph
    def graph3BarGraph(self):
        #remove whitespaces
        self.df.columns = self.df.columns.str.strip()

        #extract top 20 data in state category
        stateCount = self.df['State'].value_counts().head(20)

        #state name
        stateLabel = stateCount.index
        #occurence of ufo in states
        sizes = stateCount.values
 
        #plot title and axis labels
        plt.title("Top 20 UFO Sighted States")
        plt.bar(stateLabel, sizes)
        plt.xlabel("States")
        plt.ylabel("Frequency")

        #show line plot
        plt.show()