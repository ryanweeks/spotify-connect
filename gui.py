'''	 
Project: Spotify Connect
Filename: gui.py

Description:
Creates and runs GUI. The main program that is run.
'''

	
# Importing library
import imp
appJar = imp.load_source("appJar", "Dependencies/appJar/appjar.py")
from appJar import gui
import os.path


# Creating gui
app=gui("Spotify-Connect", "600x500")


def runGui() :
	'''
	Pre: app gui exists
	Post: app gui has been opened
	Purpose: Create the app gui, set with graphics and content
	'''
	# Styling gui
	#app.setIcon("Images/Weather-app.ico")
	app.setResizable(canResize=False)
	app.setBg("dark blue")
	app.setFont(12, "Verdana")

	# .addLabel(name, text, row, col, colspan, rowspan) 
	app.addLabel("Title", "Spotify-Connect", 0, 0, 4)

	# Add a separator between the options and input box
	# for improved readability
	app.addHorizontalSeparator(2, 1, 1, colour="orange")

	# Starts gui
	app.go()

def press(btn):
	'''
	Pre: A gui button that has been pressed
	Post: Action taken depending on button
	Purpose: Handle button clicks to Submit, Reset, or Quit
	'''
	continue
runGui()