import tkinter as tk
import pyautogui as pg
import time

root = tk.Tk()
root.title("CAM Tool Program")
root.attributes("-topmost", True)

# Setting the window size
root.geometry("550x250")

# Load the logo image (replace 'path_to_logo.png' with the actual file path)
logo = tk.PhotoImage(file="images.png")
root.iconphoto(False, logo)  # Set the logo as the window icon

# Declare string variables for different tool types
drill_var = tk.StringVar()
endmill_var = tk.StringVar()
bullnose_var = tk.StringVar()
ballcutter_var = tk.StringVar()
boring_var = tk.StringVar()

# Function to process the input based on the filled box
def submit(event=None):
    # Get the values from the input fields
    drill_input = drill_var.get().strip()
    endmill_input = endmill_var.get().strip()
    bullnose_input = bullnose_var.get().strip()
    ballcutter_input = ballcutter_var.get().strip()
    boring_input = boring_var.get().strip()
    
    if drill_input:
        # Process Drill input
        entry_array = drill_input.split()
        process_drill(entry_array)
    elif endmill_input:
        # Process Endmill input
        entry_array = endmill_input.split()
        process_endmill(entry_array)
    elif bullnose_input:
        # Process Bull Nose input
        entry_array = bullnose_input.split()
        process_bullnose(entry_array)
    elif ballcutter_input:
        # Process Ball Cutter input
        entry_array = ballcutter_input.split()
        process_ballcutter(entry_array)
    elif boring_input:
        # Process Ball Cutter input
        entry_array = boring_input.split()
        process_boring(entry_array)
    else:
        print("No input provided")

    # Clear the fields
    drill_var.set("")
    endmill_var.set("")
    bullnose_var.set("")
    ballcutter_var.set("")
    boring_var.set("")

def process_drill(entry_array):
    # Example: 5 D P -> Drill with 5 mm in P20 metal
    print(f"Drill Input: {entry_array}")
    #Click on operation
    pg.moveTo(130, 480)
    pg.click()
    pg.press("d")
    #pg.click(button='right')
    time.sleep(0.5)
    #Tools
    pg.moveTo(118, 267)
    pg.click()
    time.sleep(0.5)
    #Select
    pg.moveTo(378, 604)
    pg.click()
    time.sleep(0.5)
    #10.5
    pg.moveTo(566, 567)
    pg.click(clicks=2)#Double Click
    time.sleep(0.5)
    #Diameter
    pg.moveTo(1353, 527)
    pg.click(clicks=2)
    time.sleep(0.5)
    pg.write(entry_array[0])
    time.sleep(0.5)
    #Cutting Condition
    pg.moveTo(1784, 458)
    pg.click()
    time.sleep(0.5)
    if entry_array[1] in ["M" ,"m" ,"MS", "ms"]:
        #Feed Z
        pg.moveTo(1320, 775)
        pg.click(clicks=2)
        if entry_array[0] == "5":
            pg.write("50")
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("1000")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(1)
        if entry_array[0] in ["1", "2"]:
            pg.write("40") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("2000")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(1)
        if entry_array[0] in ["3", "4"]:
            pg.write("50") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.press("1500")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["8", "8.5", "9"]:
            pg.write("60") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("600")      
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["6", "7"]:
            pg.write("60") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("600")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["10", "11", "12", "10.5"]:
            pg.write("50") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("500")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["13", "14", "15", "16", "17", "18", "19", "20"]:
            pg.write("40") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("400")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(0.5)
        else:
            print("No data available")
        #Technology
        pg.moveTo(138,311)
        pg.click()
        time.sleep(.1)
        #Shortest Distance
        pg.moveTo(297,330)
        pg.click()
        time.sleep(.1)
        #Drill cycle type
        pg.moveTo(620,294)
        pg.click()
        time.sleep(.1)
        #Peck
        pg.moveTo(445,341)
        pg.click()
        time.sleep(0.5)
        #Data
        pg.moveTo(627,437)
        pg.click()
        time.sleep(0.5)
        #Step Down
        pg.moveTo(1027,435)
        pg.click()
        time.sleep(0.5)
        if entry_array[0] =="5":
            #Enter value
            pg.write(".3")
            time.sleep(0.5)
        if entry_array[0] in ["1", "2"]:
            #Enter value
            pg.write(".05")
            time.sleep(0.5)
        if entry_array[0] in ["8", "8.5", "9"]:
            #Enter value
            pg.write(".65")
            
            time.sleep(0.5)
        if entry_array[0] in ["10", "11", "12", "10.5"]:
            #Enter value
            pg.write(".75")
        
            time.sleep(0.5)
        if entry_array[0] in ["13", "14", "15", "16", "17", "18", "19", "20"]:
            #Enter value
            pg.write(".7")
            time.sleep(0.5)
        if entry_array[0] in ["3", "4"]:
            #Enter value
            pg.write(".2")
            time.sleep(0.5)
        if entry_array[0] in ["6", "7"]:
            #Enter value
            pg.write(".4")
            time.sleep(0.5)
        else:
            print("")
        
        #delay
        pg.moveTo(1018,487)
        pg.click()
        pg.write(".001")
        time.sleep(0.5)
        #Ok
        pg.moveTo(875,606)
        pg.click()
    if entry_array[1] in ["P", "p","P20", "p20"]:
        #Feed Z
        pg.moveTo(1320, 775)
        pg.click(clicks=2)
        if entry_array[0] == "5":
            pg.write("50")
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("1000")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(1)
        if entry_array[0] in ["1", "2"]:
            pg.write("40") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("2000")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(1)
        if entry_array[0] in ["3", "4"]:
            pg.write("50") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.press("1500")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["8", "8.5", "9"]:
            pg.write("60") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("600")      
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["6", "7"]:
            pg.write("60") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("600")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["10", "11", "12", "10.5"]:
            pg.write("50") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("500")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["13", "14", "15", "16", "17", "18", "19", "20"]:
            pg.write("40") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("400")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(0.5)
        else:
            print("No data available")
        #Technology
        pg.moveTo(138,311)
        pg.click()
        time.sleep(.1)
        #Shortest Distance
        pg.moveTo(297,330)
        pg.click()
        time.sleep(.1)
        #Drill cycle type
        pg.moveTo(620,294)
        pg.click()
        time.sleep(.1)
        #Peck
        pg.moveTo(445,341)
        pg.click()
        time.sleep(0.5)
        #Data
        pg.moveTo(627,437)
        pg.click()
        time.sleep(0.5)
        #Step Down
        pg.moveTo(1027,435)
        pg.click()
        time.sleep(0.5)
        if entry_array[0] =="5":
            #Enter value
            pg.write(".3")
            time.sleep(0.5)
        if entry_array[0] in ["1", "2"]:
            #Enter value
            pg.write(".05")
            time.sleep(0.5)
        if entry_array[0] in ["8", "8.5", "9"]:
            #Enter value
            pg.write(".65")
            
            time.sleep(0.5)
        if entry_array[0] in ["10", "11", "12", "10.5"]:
            #Enter value
            pg.write(".75")
        
            time.sleep(0.5)
        if entry_array[0] in ["13", "14", "15", "16", "17", "18", "19", "20"]:
            #Enter value
            pg.write(".7")
            time.sleep(0.5)
        if entry_array[0] in ["3", "4"]:
            #Enter value
            pg.write(".2")
            time.sleep(0.5)
        if entry_array[0] in ["6", "7"]:
            #Enter value
            pg.write(".4")
            time.sleep(0.5)
        else:
            print("")
        
        #delay
        pg.moveTo(1018,487)
        pg.click()
        pg.write(".001")
        time.sleep(0.5)
        #Ok
        pg.moveTo(875,606)
        pg.click()
 

def process_endmill(entry_array):
    # Example: 12 E M R -> Endmill with 12 mm in MS metal, Rough cutting
    print(f"Endmill Input: {entry_array}")
    #Click on operation
    pg.moveTo(130, 480)
    pg.click()
    pg.press("d")
    #pg.click(button='right')
    time.sleep(0.5)
    #Tools
    pg.moveTo(118, 267)
    pg.click()
    time.sleep(0.5)
    #Select
    pg.moveTo(378, 604)
    pg.click()
    time.sleep(0.5)
    #10.5
    pg.moveTo(566, 567)
    pg.click(clicks=2)#Double Click
    time.sleep(0.5)
    #Diameter
    pg.moveTo(1353, 527)
    pg.click(clicks=2)
    time.sleep(0.5)
    pg.write(entry_array[0])
    time.sleep(0.5)
    #Cutting Condition
    pg.moveTo(1784, 458)
    pg.click()
    time.sleep(0.5)
    if entry_array[1] in ["M" ,"m" ,"MS", "ms"]:
        #Feed Z
        pg.moveTo(1320, 775)
        pg.click(clicks=2)
        if entry_array[0] == "5":
            pg.write("50")
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("1000")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(1)
        if entry_array[0] in ["1", "2"]:
            pg.write("40") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("2000")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(1)
        if entry_array[0] in ["3", "4"]:
            pg.write("50") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.press("1500")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["8", "8.5", "9"]:
            pg.write("60") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("600")      
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["6", "7"]:
            pg.write("60") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("600")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["10", "11", "12", "10.5"]:
            pg.write("50") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("500")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["13", "14", "15", "16", "17", "18", "19", "20"]:
            pg.write("40") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("400")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(0.5)
        else:
            print("No data available")
        #Technology
        pg.moveTo(138,311)
        pg.click()
        time.sleep(.1)
        #Shortest Distance
        pg.moveTo(297,330)
        pg.click()
        time.sleep(.1)
        #Drill cycle type
        pg.moveTo(620,294)
        pg.click()
        time.sleep(.1)
        #Peck
        pg.moveTo(445,341)
        pg.click()
        time.sleep(0.5)
        #Data
        pg.moveTo(627,437)
        pg.click()
        time.sleep(0.5)
        #Step Down
        pg.moveTo(1027,435)
        pg.click()
        time.sleep(0.5)
        if entry_array[0] =="5":
            #Enter value
            pg.write(".3")
            time.sleep(0.5)
        if entry_array[0] in ["1", "2"]:
            #Enter value
            pg.write(".05")
            time.sleep(0.5)
        if entry_array[0] in ["8", "8.5", "9"]:
            #Enter value
            pg.write(".65")
            
            time.sleep(0.5)
        if entry_array[0] in ["10", "11", "12", "10.5"]:
            #Enter value
            pg.write(".75")
        
            time.sleep(0.5)
        if entry_array[0] in ["13", "14", "15", "16", "17", "18", "19", "20"]:
            #Enter value
            pg.write(".7")
            time.sleep(0.5)
        if entry_array[0] in ["3", "4"]:
            #Enter value
            pg.write(".2")
            time.sleep(0.5)
        if entry_array[0] in ["6", "7"]:
            #Enter value
            pg.write(".4")
            time.sleep(0.5)
        else:
            print("")
        
        #delay
        pg.moveTo(1018,487)
        pg.click()
        pg.write(".001")
        time.sleep(0.5)
        #Ok
        pg.moveTo(875,606)
        pg.click()
    if entry_array[1] in ["P", "p","P20", "p20"]:
        #Feed Z
        pg.moveTo(1320, 775)
        pg.click(clicks=2)
        if entry_array[0] == "5":
            pg.write("50")
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("1000")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(1)
        if entry_array[0] in ["1", "2"]:
            pg.write("40") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("2000")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(1)
        if entry_array[0] in ["3", "4"]:
            pg.write("50") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.press("1500")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["8", "8.5", "9"]:
            pg.write("60") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("600")      
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["6", "7"]:
            pg.write("60") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("600")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["10", "11", "12", "10.5"]:
            pg.write("50") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("500")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["13", "14", "15", "16", "17", "18", "19", "20"]:
            pg.write("40") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("400")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(0.5)
        else:
            print("No data available")
        #Technology
        pg.moveTo(138,311)
        pg.click()
        time.sleep(.1)
        #Shortest Distance
        pg.moveTo(297,330)
        pg.click()
        time.sleep(.1)
        #Drill cycle type
        pg.moveTo(620,294)
        pg.click()
        time.sleep(.1)
        #Peck
        pg.moveTo(445,341)
        pg.click()
        time.sleep(0.5)
        #Data
        pg.moveTo(627,437)
        pg.click()
        time.sleep(0.5)
        #Step Down
        pg.moveTo(1027,435)
        pg.click()
        time.sleep(0.5)
        if entry_array[0] =="5":
            #Enter value
            pg.write(".3")
            time.sleep(0.5)
        if entry_array[0] in ["1", "2"]:
            #Enter value
            pg.write(".05")
            time.sleep(0.5)
        if entry_array[0] in ["8", "8.5", "9"]:
            #Enter value
            pg.write(".65")
            
            time.sleep(0.5)
        if entry_array[0] in ["10", "11", "12", "10.5"]:
            #Enter value
            pg.write(".75")
        
            time.sleep(0.5)
        if entry_array[0] in ["13", "14", "15", "16", "17", "18", "19", "20"]:
            #Enter value
            pg.write(".7")
            time.sleep(0.5)
        if entry_array[0] in ["3", "4"]:
            #Enter value
            pg.write(".2")
            time.sleep(0.5)
        if entry_array[0] in ["6", "7"]:
            #Enter value
            pg.write(".4")
            time.sleep(0.5)
        else:
            print("")
        
        #delay
        pg.moveTo(1018,487)
        pg.click()
        pg.write(".001")
        time.sleep(0.5)
        #Ok
        pg.moveTo(875,606)
        pg.click()
 

def process_bullnose(entry_array):
    # Write your automation logic for Bull Nose here
    print(f"Bull Nose Input: {entry_array}")
    #Click on operation
    pg.moveTo(130, 480)
    pg.click()
    pg.press("d")
    #pg.click(button='right')
    time.sleep(0.5)
    #Tools
    pg.moveTo(118, 267)
    pg.click()
    time.sleep(0.5)
    #Select
    pg.moveTo(378, 604)
    pg.click()
    time.sleep(0.5)
    #10.5
    pg.moveTo(566, 567)
    pg.click(clicks=2)#Double Click
    time.sleep(0.5)
    #Diameter
    pg.moveTo(1353, 527)
    pg.click(clicks=2)
    time.sleep(0.5)
    pg.write(entry_array[0])
    time.sleep(0.5)
    #Cutting Condition
    pg.moveTo(1784, 458)
    pg.click()
    time.sleep(0.5)
    if entry_array[1] in ["M" ,"m" ,"MS", "ms"]:
        #Feed Z
        pg.moveTo(1320, 775)
        pg.click(clicks=2)
        if entry_array[0] == "5":
            pg.write("50")
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("1000")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(1)
        if entry_array[0] in ["1", "2"]:
            pg.write("40") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("2000")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(1)
        if entry_array[0] in ["3", "4"]:
            pg.write("50") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.press("1500")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["8", "8.5", "9"]:
            pg.write("60") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("600")      
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["6", "7"]:
            pg.write("60") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("600")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["10", "11", "12", "10.5"]:
            pg.write("50") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("500")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["13", "14", "15", "16", "17", "18", "19", "20"]:
            pg.write("40") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("400")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(0.5)
        else:
            print("No data available")
        #Technology
        pg.moveTo(138,311)
        pg.click()
        time.sleep(.1)
        #Shortest Distance
        pg.moveTo(297,330)
        pg.click()
        time.sleep(.1)
        #Drill cycle type
        pg.moveTo(620,294)
        pg.click()
        time.sleep(.1)
        #Peck
        pg.moveTo(445,341)
        pg.click()
        time.sleep(0.5)
        #Data
        pg.moveTo(627,437)
        pg.click()
        time.sleep(0.5)
        #Step Down
        pg.moveTo(1027,435)
        pg.click()
        time.sleep(0.5)
        if entry_array[0] =="5":
            #Enter value
            pg.write(".3")
            time.sleep(0.5)
        if entry_array[0] in ["1", "2"]:
            #Enter value
            pg.write(".05")
            time.sleep(0.5)
        if entry_array[0] in ["8", "8.5", "9"]:
            #Enter value
            pg.write(".65")
            
            time.sleep(0.5)
        if entry_array[0] in ["10", "11", "12", "10.5"]:
            #Enter value
            pg.write(".75")
        
            time.sleep(0.5)
        if entry_array[0] in ["13", "14", "15", "16", "17", "18", "19", "20"]:
            #Enter value
            pg.write(".7")
            time.sleep(0.5)
        if entry_array[0] in ["3", "4"]:
            #Enter value
            pg.write(".2")
            time.sleep(0.5)
        if entry_array[0] in ["6", "7"]:
            #Enter value
            pg.write(".4")
            time.sleep(0.5)
        else:
            print("")
        
        #delay
        pg.moveTo(1018,487)
        pg.click()
        pg.write(".001")
        time.sleep(0.5)
        #Ok
        pg.moveTo(875,606)
        pg.click()
    if entry_array[1] in ["P", "p","P20", "p20"]:
        #Feed Z
        pg.moveTo(1320, 775)
        pg.click(clicks=2)
        if entry_array[0] == "5":
            pg.write("50")
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("1000")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(1)
        if entry_array[0] in ["1", "2"]:
            pg.write("40") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("2000")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(1)
        if entry_array[0] in ["3", "4"]:
            pg.write("50") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.press("1500")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["8", "8.5", "9"]:
            pg.write("60") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("600")      
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["6", "7"]:
            pg.write("60") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("600")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["10", "11", "12", "10.5"]:
            pg.write("50") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("500")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["13", "14", "15", "16", "17", "18", "19", "20"]:
            pg.write("40") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("400")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(0.5)
        else:
            print("No data available")
        #Technology
        pg.moveTo(138,311)
        pg.click()
        time.sleep(.1)
        #Shortest Distance
        pg.moveTo(297,330)
        pg.click()
        time.sleep(.1)
        #Drill cycle type
        pg.moveTo(620,294)
        pg.click()
        time.sleep(.1)
        #Peck
        pg.moveTo(445,341)
        pg.click()
        time.sleep(0.5)
        #Data
        pg.moveTo(627,437)
        pg.click()
        time.sleep(0.5)
        #Step Down
        pg.moveTo(1027,435)
        pg.click()
        time.sleep(0.5)
        if entry_array[0] =="5":
            #Enter value
            pg.write(".3")
            time.sleep(0.5)
        if entry_array[0] in ["1", "2"]:
            #Enter value
            pg.write(".05")
            time.sleep(0.5)
        if entry_array[0] in ["8", "8.5", "9"]:
            #Enter value
            pg.write(".65")
            
            time.sleep(0.5)
        if entry_array[0] in ["10", "11", "12", "10.5"]:
            #Enter value
            pg.write(".75")
        
            time.sleep(0.5)
        if entry_array[0] in ["13", "14", "15", "16", "17", "18", "19", "20"]:
            #Enter value
            pg.write(".7")
            time.sleep(0.5)
        if entry_array[0] in ["3", "4"]:
            #Enter value
            pg.write(".2")
            time.sleep(0.5)
        if entry_array[0] in ["6", "7"]:
            #Enter value
            pg.write(".4")
            time.sleep(0.5)
        else:
            print("")
        
        #delay
        pg.moveTo(1018,487)
        pg.click()
        pg.write(".001")
        time.sleep(0.5)
        #Ok
        pg.moveTo(875,606)
        pg.click()
 

def process_ballcutter(entry_array):
    # Write your automation logic for Ball Cutter here
    print(f"Ball Cutter Input: {entry_array}")
    #Click on operation
    pg.moveTo(130, 480)
    pg.click()
    pg.press("d")
    #pg.click(button='right')
    time.sleep(0.5)
    #Tools
    pg.moveTo(118, 267)
    pg.click()
    time.sleep(0.5)
    #Select
    pg.moveTo(378, 604)
    pg.click()
    time.sleep(0.5)
    #10.5
    pg.moveTo(566, 567)
    pg.click(clicks=2)#Double Click
    time.sleep(0.5)
    #Diameter
    pg.moveTo(1353, 527)
    pg.click(clicks=2)
    time.sleep(0.5)
    pg.write(entry_array[0])
    time.sleep(0.5)
    #Cutting Condition
    pg.moveTo(1784, 458)
    pg.click()
    time.sleep(0.5)
    if entry_array[1] in ["M" ,"m" ,"MS", "ms"]:
        #Feed Z
        pg.moveTo(1320, 775)
        pg.click(clicks=2)
        if entry_array[0] == "5":
            pg.write("50")
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("1000")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(1)
        if entry_array[0] in ["1", "2"]:
            pg.write("40") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("2000")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(1)
        if entry_array[0] in ["3", "4"]:
            pg.write("50") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.press("1500")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["8", "8.5", "9"]:
            pg.write("60") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("600")      
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["6", "7"]:
            pg.write("60") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("600")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["10", "11", "12", "10.5"]:
            pg.write("50") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("500")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["13", "14", "15", "16", "17", "18", "19", "20"]:
            pg.write("40") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("400")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(0.5)
        else:
            print("No data available")
        #Technology
        pg.moveTo(138,311)
        pg.click()
        time.sleep(.1)
        #Shortest Distance
        pg.moveTo(297,330)
        pg.click()
        time.sleep(.1)
        #Drill cycle type
        pg.moveTo(620,294)
        pg.click()
        time.sleep(.1)
        #Peck
        pg.moveTo(445,341)
        pg.click()
        time.sleep(0.5)
        #Data
        pg.moveTo(627,437)
        pg.click()
        time.sleep(0.5)
        #Step Down
        pg.moveTo(1027,435)
        pg.click()
        time.sleep(0.5)
        if entry_array[0] =="5":
            #Enter value
            pg.write(".3")
            time.sleep(0.5)
        if entry_array[0] in ["1", "2"]:
            #Enter value
            pg.write(".05")
            time.sleep(0.5)
        if entry_array[0] in ["8", "8.5", "9"]:
            #Enter value
            pg.write(".65")
            
            time.sleep(0.5)
        if entry_array[0] in ["10", "11", "12", "10.5"]:
            #Enter value
            pg.write(".75")
        
            time.sleep(0.5)
        if entry_array[0] in ["13", "14", "15", "16", "17", "18", "19", "20"]:
            #Enter value
            pg.write(".7")
            time.sleep(0.5)
        if entry_array[0] in ["3", "4"]:
            #Enter value
            pg.write(".2")
            time.sleep(0.5)
        if entry_array[0] in ["6", "7"]:
            #Enter value
            pg.write(".4")
            time.sleep(0.5)
        else:
            print("")
        
        #delay
        pg.moveTo(1018,487)
        pg.click()
        pg.write(".001")
        time.sleep(0.5)
        #Ok
        pg.moveTo(875,606)
        pg.click()
    if entry_array[1] in ["P", "p","P20", "p20"]:
        #Feed Z
        pg.moveTo(1320, 775)
        pg.click(clicks=2)
        if entry_array[0] == "5":
            pg.write("50")
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("1000")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(1)
        if entry_array[0] in ["1", "2"]:
            pg.write("40") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("2000")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(1)
        if entry_array[0] in ["3", "4"]:
            pg.write("50") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.press("1500")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["8", "8.5", "9"]:
            pg.write("60") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("600")      
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["6", "7"]:
            pg.write("60") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("600")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["10", "11", "12", "10.5"]:
            pg.write("50") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("500")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(.5)
        if entry_array[0] in ["13", "14", "15", "16", "17", "18", "19", "20"]:
            pg.write("40") #Feed Z value
            time.sleep(0.5)
            #RPM
            pg.moveTo(1574,730)
            pg.click(clicks=2)
            pg.write("400")
            time.sleep(0.5)
            pg.click(1710,839)#press ok tick
            time.sleep(0.5)
        else:
            print("No data available")
        #Technology
        pg.moveTo(138,311)
        pg.click()
        time.sleep(.1)
        #Shortest Distance
        pg.moveTo(297,330)
        pg.click()
        time.sleep(.1)
        #Drill cycle type
        pg.moveTo(620,294)
        pg.click()
        time.sleep(.1)
        #Peck
        pg.moveTo(445,341)
        pg.click()
        time.sleep(0.5)
        #Data
        pg.moveTo(627,437)
        pg.click()
        time.sleep(0.5)
        #Step Down
        pg.moveTo(1027,435)
        pg.click()
        time.sleep(0.5)
        if entry_array[0] =="5":
            #Enter value
            pg.write(".3")
            time.sleep(0.5)
        if entry_array[0] in ["1", "2"]:
            #Enter value
            pg.write(".05")
            time.sleep(0.5)
        if entry_array[0] in ["8", "8.5", "9"]:
            #Enter value
            pg.write(".65")
            
            time.sleep(0.5)
        if entry_array[0] in ["10", "11", "12", "10.5"]:
            #Enter value
            pg.write(".75")
        
            time.sleep(0.5)
        if entry_array[0] in ["13", "14", "15", "16", "17", "18", "19", "20"]:
            #Enter value
            pg.write(".7")
            time.sleep(0.5)
        if entry_array[0] in ["3", "4"]:
            #Enter value
            pg.write(".2")
            time.sleep(0.5)
        if entry_array[0] in ["6", "7"]:
            #Enter value
            pg.write(".4")
            time.sleep(0.5)
        else:
            print("")
        
        #delay
        pg.moveTo(1018,487)
        pg.click()
        pg.write(".001")
        time.sleep(0.5)
        #Ok
        pg.moveTo(875,606)
        pg.click()
 
def process_boring(entry_array):
    # Write your automation logic for Ball Cutter here
    print(f"Boring Input: {entry_array}")

# Define the function for the "Drawing" button
def drawing_task():
    # Example GUI tasks using pyautogui
    pg.moveTo(200, 200)  # Move the mouse to position (200, 200)
    pg.click()  # Click at the current position
    time.sleep(0.5)
    pg.write("Starting 10000")  # Type out some text
    time.sleep(0.5)
    pg.press('enter')  # Press Enter
    pg.moveTo(300, 300)  # Move to another position
    pg.click()
    # Add more pyautogui tasks as per your requirement
    print("Drawing task complete.")


# Creating labels and entry fields for each tool
drill_label = tk.Label(root, text='Drill (e.g., 5 P)', font=('calibre', 10, 'bold'))
drill_entry = tk.Entry(root, textvariable=drill_var, font=('calibre', 10, 'normal'))

endmill_label = tk.Label(root, text='Endmill (e.g., 12 M R)', font=('calibre', 10, 'bold'))
endmill_entry = tk.Entry(root, textvariable=endmill_var, font=('calibre', 10, 'normal'))

bullnose_label = tk.Label(root, text='Bull Nose (e.g., 8 MS F)', font=('calibre', 10, 'bold'))
bullnose_entry = tk.Entry(root, textvariable=bullnose_var, font=('calibre', 10, 'normal'))

ballcutter_label = tk.Label(root, text='Ball Cutter (e.g., 10 P20 S)', font=('calibre', 10, 'bold'))
ballcutter_entry = tk.Entry(root, textvariable=ballcutter_var, font=('calibre', 10, 'normal'))

#boring_label = tk.Label(root, text='Boring Tool (e.g., 10 P20 F)', font=('calibre', 10, 'bold'))
#boring_entry = tk.Entry(root, textvariable=boring_var, font=('calibre', 10, 'normal'))


# Bind the Enter key to the submit function
drill_entry.bind('<Return>', submit)
endmill_entry.bind('<Return>', submit)
bullnose_entry.bind('<Return>', submit)
ballcutter_entry.bind('<Return>', submit)
#boring_entry.bind('<Return>', submit)


#creating button for boring
boring_button = tk.Button(root, text="Boring", command=process_boring)
# Creating a button that will also call the submit function
sub_btn = tk.Button(root, text='Submit', command=submit)

# Create a button labeled "Drawing"
drawing_button = tk.Button(root, text="Drawing", command=drawing_task)



# Place the button on the window using grid or pack
#drawing_button.pack(pady=20)  # You can use .grid() if you prefer

# Placing the labels and entry fields in the required position using grid method
drill_label.grid(row=0, column=0)
drill_entry.grid(row=0, column=1)

endmill_label.grid(row=1, column=0)
endmill_entry.grid(row=1, column=1)

bullnose_label.grid(row=2, column=0)
bullnose_entry.grid(row=2, column=1)

ballcutter_label.grid(row=3, column=0)
ballcutter_entry.grid(row=3, column=1)

boring_button.grid(row=4, column=0, padx=10, pady=10)
drawing_button.grid(row=4, column=1, padx=10, pady=10)

sub_btn.grid(row=5, column=0, columnspan=2, pady=20)

# Running the infinite loop for the window to display
root.mainloop()
