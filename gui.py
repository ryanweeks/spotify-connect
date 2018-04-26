'''	 
Project: Spotify Connect
Filename: gui.py

Description:
Creates and runs GUI. The main program that is run.
'''


# Importing library
import imp
import wConditions
import optHandler
import extensions
appJar = imp.load_source("appJar", "Dependencies/appJar/appjar.py")
from appJar import gui
import os.path


# Creating gui
app=gui("Weather", "600x500")


def runGui() :
    '''
    Pre: app gui exists
    Post: app gui has been opened
    Purpose: Create the app gui, set with graphics and content
    '''
    # Styling gui
    app.setIcon("Images/Weather-app.ico")
    app.setResizable(canResize=False)
    app.setBg("light blue")
    app.setFont(12, "Verdana")

    # .addLabel(name, text, row, col, colspan, rowspan) 
    app.addLabel("Title", "Weather App", 0, 0, 4)

    # Adding input box
    app.addLabel("Location", "Location:", 1, 0)
    app.addEntry("Location", 1, 1)

    # Add a separator between the options and input box
    # for improved readability
    app.addHorizontalSeparator(2, 1, 1, colour="orange")

    # Adding options
    app.startToggleFrame("Options", 3, 1, 1)
    app.setToggleFrameBg("Options", "light blue")
    app.addProperties("Options", optHandler.defaultOpts)
    app.stopToggleFrame()

    # Add all buttons
    app.addButton("Submit", press, 9, 0, 0)
    app.addButton("Reset", press, 9, 1, 0)
    app.addButton("Quit", press, 9, 2, 0)
    app.setButtonFont(10, "Verdana")

    # Update submit button
    app.setButtonBg("Submit", "yellow")

    # Update reset button
    app.setButtonBg("Reset", "yellow")

    # Update quit button
    app.setButtonBg("Quit", "yellow")
    
    # Bind enter key to press
    app.enableEnter(press)
    
    # Starts gui
    app.go()
   

def showResult(data, resultGui):
    '''
    Pre: json data on weather conditions and initialized gui
    Post: result gui is opened
    Purpose: Display results gui and update content with
    requested forecast data
    '''
    # Display content
    zipcode = "Your Weather for: " + app.getEntry("Location")
    resultGui.setLabel("zipcode", zipcode)
    
    curConditions = ""

    # Iterate through all options and call requested functions
    for option, setting in optHandler.defaultOpts.iteritems():
        # TODO: report if property does not exist
        if app.getProperty("Options", option):
            curConditions = curConditions + str(optHandler.optMappings[option][0](data)) + str(optHandler.optMappings[option][1])
            # Will set background image to current condition
            if option == "Conditions":
                weather = wConditions.getIconName(data)
                filepath = "Images/status-" + weather + ".ico"
                if os.path.exists(filepath):
                    resultGui.setIcon(filepath)
                else:
                    resultGui.setIcon("Images/Weather-app.ico")
    resultGui.setMessage("Current Conditions", curConditions)
    
    resultGui.go()


def press(btn):
    '''
    Pre: A gui button that has been pressed
    Post: Action taken depending on button
    Purpose: Handle button clicks to Submit, Reset, or Quit
    '''
    if btn=="Submit" or btn=='<Return>':
        # Make results gui
        results = makeResultsGui()
        valid = False
        
        loc = app.getEntry("Location")
        if loc.isdigit():
                valid = extensions.valZip(loc, app)
        else:
                valid = extensions.valLoc(loc, app)

        if valid:
            jsonData = wConditions.getJson(loc)
            valid = extensions.valJson(jsonData, app)
            
        # Will only get forecast if the zipcode or location is valid
        if valid:
            showResult(jsonData, results)
    elif btn=="Reset":
		# Clear the entry of any input before entering a new location 
		app.setProperties("Options", optHandler.defaultOpts)
		app.clearEntry("Location")
		app.setFocus("Location")
    elif btn=="Quit":
		# Exit the program 
        app.infoBox("Goodbye", "Thanks for stopping by ;)")
        app.stop()


def makeResultsGui():
    '''
    Pre: none
    Post: Returns a results gui that has been initialized and content loaded
    Purpose: Create the results gui, styled and with content
    '''
    # Create results gui
    results=gui("Your Weather", "400x600")
    
    # Style gui
    results.setResizable(canResize=False)
    results.setBg("light blue")

    # Display content
    zipcode = "Your Weather for: " + app.getEntry("Location")
    results.addLabel("zipcode", zipcode, 0, 0)
    results.addMessage("Current Conditions", "")
    
    return results


runGui()