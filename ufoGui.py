#Junhui Park
#December 4, 2024
#AP CSP 5th
#Close Encounters of a Kind - GUI

#import libraries
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

#import class UfoGraph from ufoData file
from ufoData import UfoGraph

#gui class
class UfoGui:
    def __init__(self):
        #setting window
        self.mainWindow = tk.Tk()

        #default setting of window
        self.mainWindow.title("UFO Sightings Data Visualization")
        self.mainWindow.geometry("400x400")

        #set fram for background image
        frame = tk.Frame(self.mainWindow)
        frame.place(x= -5, y = -2)

        #call background image
        img = ImageTk.PhotoImage(Image.open("background.jpeg"))
        imglabel = tk.Label(frame, image = img)
        imglabel.pack()

        #assign name for class UfoGraph
        #easily access class in another file    
        self.graph = UfoGraph()

        #title label
        self.titleLabel = tk.Label(self.mainWindow, text = "UFO Sightings Data Visualization")
        self.titleLabel.place(x = 100, y= 40)

        #button to open pie chart of shapes
        self.graph1Button = tk.Button(self.mainWindow, text = "Pie Chart", command = self.graph.graph1PieChart) 
        self.graph1Button.place(x = 50, y = 100)

        #button to open line plot of sightings by decades
        self.graph2Button = tk.Button(self.mainWindow, text = "Line Plot", command = self.graph.graph2LinePlot) 
        self.graph2Button.place(x = 50, y = 170)

        #button to open bar graph of top 20 cities
        self.graph3Button = tk.Button(self.mainWindow, text = "Bar Graph", command = self.graph.graph3BarGraph)
        self.graph3Button.place(x = 50, y= 240)

        #loop
        self.mainWindow.mainloop()