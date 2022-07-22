import tkinter as tk
from functools import partial

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

"""TODO:
1. Work through the tutorials at this link (in a new python file) to get an idea for how to use tkinter
    (a front end programming library in Python).
    https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter
2. Use the functions you made in the jupyter notebooks to load in the data and clean it. 
3. Use what you learned from the tkinter tutorial to make entries and labels for the time ranges
4. fill the plot function with the matplotlib code you developed as part of the jupyter notebook
5. Use what you learned from the tkinter tutorial to create two buttons 'clear' and 'submit' that
    the user can interact with
        a. the tutorial talks about how to get string entries from tk.Entries - use this to get
        your start and end strings

"""

def load_and_process_data():
    """
    this function should load in the raw csv files and output a clean,
    filtered dataframe containing both the read and set values.

    NOTE you can copy and paste from your jupyter notebook.
    """
    # ...your code here...
    return clean_dataframe


def _quit():
    window.quit()
    window.destroy()


def query_timerange(start, end, data):
    date_filter = data.index.to_series().between(start, end)
    subset = data.where(date_filter == True).dropna()
    return subset


def plotData(ax, data_filtered, canvas):
    """
    this function should plot the timerange of data that the user has
    specified. The passed dataframe should already be filtered to only
    include the relevant time ranges.
    """
    # first we clear the plot that was already on the axis
    ax.clear()
    # ...insert your plotting code here...

    # NOTE we need to call 'draw' on our canvas to see our plot update 
    canvas.draw()


def clear_plot_when_clear_button_is_clicked(ax, canvas):
    ax.clear()
    canvas.draw()


def execute_when_submit_button_clicked(ax, canvas, data):
    """
    This is the function that we want to be called whenever a user presses
    the submit button.
    """
    start_string = # add your code for retrieving the input data from a tk.Entry here
    end_string = # add your code for retrieving the input data from a tk.Entry here

    # the data from the user will come in as a string format but we want to convert
    # it to a datetime object like in the index of our dataframe. We do this by calling
    # the pandas.to_datetime() function on the string. 
    start = pd.to_datetime(start_string)
    end = pd.to_datetime(end_string)
    subset = query_timerange(start, end, data)
    plotData(ax, subset, canvas)


def execute_when_clear_button_clicked(ax, canvas):
    """
    This function is one that we want to be called whenever a user clicks
    the 'clear' button. It should remove any existing text from the entry
    boxes and we've also made sure that it clears the plot. 
    """
    # add your code for how to clear the tk.Entry boxes here
    # ...

    # then we clear the plot as well - I've implemented this for you
    clear_plot_when_clear_button_is_clicked(ax, canvas)


def createEntries():
    """
    In this function we want to create a form (for help see the
    'form' section of the tkinter tutorial) to allow the user to
    input their start and end ranges. We will need to create the
    frame that stores the labels and entries, as well as the labels
    and entries themselves. 
    """
    # Create a new frame `frm_form` to contain the Label
    # and Entry widgets for entering the time ranges
    frm_entries = # ...
    # Pack the frame into the window
    # ....

    # Create the Label and Entry widgets for "Start"
    lbl_start = # ...
    ent_start = # ...
    # Use the grid geometry manager to place the Label and
    # Entry widgets in the first and second columns of the
    # FIRST row of the grid
    # ...
    # ...

    # Create the Label and Entry widgets for "End"
    lbl_end = # ...
    ent_end = # ...
    # Use the grid geometry manager to place the Label and
    # Entry widgets in the first and second columns of the
    # SECOND row of the grid
    # ...
    # ...

    # pack the frame into the main window using the pack
    # method
    # ...

    # we then return the entries themselves to use their 
    # content elsewhere in the program
    return ent_start, ent_end


def createPlot():
    """
    In this function we create a frame that contains the plot
    for our data. 
    """
    # Create a new frame `frm_plots` to contain the Plots
    frm_plots = tk.Frame()
    fig, ax = plt.subplots(figsize=(7, 5))

    canvas = FigureCanvasTkAgg(fig, frm_plots)
    canvas.get_tk_widget().pack()

    # pack the frame into the main window using the pack
    # method
    frm_plots.pack()

    return canvas, ax


def createButtons():
    """"
    This function should create two buttons that sit side by side,
    one is a button the user can use to 'clear' their entries for
    the start and end time. The second should be a submit button
    that tells the program that we want to redraw the plot. 

    To help you (because it's quite complicated to explain), I've
    listed the command you should pass to the button to execute when
    it's clicked below. You will need to specify the other parameters
    like the button name etc.
    """
    # Create a new frame `frm_buttons` to contain the
    # Submit and Clear buttons. This frame fills the
    # whole window in the horizontal direction and has
    # 5 pixels of horizontal and vertical padding.
    frm_buttons = # ... 
    # pack the form into the window by calling the pack
    # method on the frm_buttons object.
    # ...

    # Create the "Submit" button (again, see the tutorial
    # for help creating the button) and pack it to the
    # right side of `frm_buttons`.
    # NOTE you can tell the button what function to run
    # when it's clicked by specifying this in the 'command'
    # parameter when you create the button. 
    btn_submit = tk.Button(
        master=#..., which frame should the button be part of?
        text=# ..., what do you want the text on the button to say?
        # link the submit function to this button so it's executed
        # every time it's clicked
        command=partial(execute_when_submit_button_clicked, ax, canvas, clean_data)
    )
    # now pack the button into the frame by calling the pack method
    # ... 

    # Create the "Clear" button and pack it in the same way
    btn_clear = tk.Button(
        master=#..., which frame should the button be part of?
        text=# ..., what do you want the text on the button to say?
        # link the clear entries function to this button so it's executed
        # every time it's clicked
        command=partial(execute_when_clear_button_clicked, ax, canvas)
    )
    # now pack the button into the frame by calling the pack method
    # ... 

    return


# Create a new window with the title "Main Magnet Data Viewer"
window = tk.Tk()
window.title("Main Magnet Data Viewer")
window.protocol("WM_DELETE_WINDOW", _quit)

clean_data = load_and_process_data()
ent_start, ent_end = createEntries()
canvas, ax = createPlot()
createButtons()


# Start the application
window.mainloop()
