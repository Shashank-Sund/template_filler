import docx
from tkinter import *

# Main Window and Title
top = Tk()
top.title("Template Filler")

# opens a new window to capture Pre-Prod Template information
def createPreProdWindow():

    # new window
    newWindow = Toplevel(top)
    newWindow.title("CR for Pre-Production")

    # labels and entry fields

    # PC / BLI / PC & BLI selection
    pc_bli_label = Label(newWindow, text="Type : ", pady=10)
    TYPE = ['PC and BLI', 'PC', 'BLI']
    pc_bli_var = StringVar(newWindow)
    pc_bli_var.set(TYPE[0])
    pc_bli = OptionMenu(newWindow, pc_bli_var, TYPE[0], TYPE[1], TYPE[2])

    # Deployment start date
    release_date_label = Label(newWindow, text="Pre-Prod Release Date : ", pady=10)
    release_date_var = StringVar()
    release_date = Entry(newWindow, textvariable=release_date_var)

    # Link to EOT
    eot_label = Label(newWindow, text="EOT Link : ", pady=10)
    eot_var = StringVar()
    eot = Entry(newWindow, textvariable=eot_var)

    # CI Version Number
    ci_version_label = Label(newWindow, text="CI Version No. : ", pady=10)
    ci_version_var = StringVar()
    ci_version = Entry(newWindow, textvariable=ci_version_var)

    # PolicyCenter RC Version Number
    pc_rc_label = Label(newWindow, text="PC RC No. : ", pady=10)
    pc_rc_var = StringVar()
    pc_rc = Entry(newWindow, textvariable=pc_rc_var)

    # BLI RC Version Number
    bli_rc_label = Label(newWindow, text="BLI RC No. : ", pady=10)
    bli_rc_var = StringVar()
    bli_rc = Entry(newWindow, textvariable=bli_rc_var)

    # Middleware option
    middleware_label = Label(newWindow, text="Middleware? : ", pady=10)
    MIDDLEWARE = ['Yes', 'No']
    middleware_var = StringVar(newWindow)
    middleware_var.set(MIDDLEWARE[0])
    middleware = OptionMenu(newWindow, middleware_var, MIDDLEWARE[0], MIDDLEWARE[1])

    # fills out Pre-Prod template (Submit button event handling)
    def fillPreProd():
        # file = open('c:\\Dev\\Template_Filler\\templates\\preprodtemplate.docx', 'rb')
        # filedata = docx.Document(file)
        print(middleware_var.get())
        print(bli_rc_var.get())

    # Spacing for Submit button
    empty_label = Label(newWindow, text="")
    empty_label2 = Label(newWindow, text="")
    submitBtn = Button(newWindow, text='Submit', padx=20, command=fillPreProd)

    # Layout of all Labels and Entry Fields
    pc_bli_label.grid(row=0, column=0)
    pc_bli.grid(row=0, column=1)
    release_date_label.grid(row=1, column=0)
    release_date.grid(row=1, column=1)
    eot_label.grid(row=2, column=0)
    eot.grid(row=2, column=1)
    ci_version_label.grid(row=3, column=0)
    ci_version.grid(row=3, column=1)
    pc_rc_label.grid(row=4, column=0)
    pc_rc.grid(row=4, column=1)
    bli_rc_label.grid(row=5, column=0)
    bli_rc.grid(row=5, column=1)
    middleware_label.grid(row=6, column=0)
    middleware.grid(row=6, column=1)
    empty_label.grid(row=7, column=0)
    empty_label2.grid(row=7, column=1)
    submitBtn.grid(row=8, column=1)

def enterProd():

    # new window
    newWindow = Toplevel(top)
    newWindow.title("CR for Production")

def enterProdStaging():

    # new window
    newWindow = Toplevel(top)
    newWindow.title("CR for Production")

# Main Window Buttons
crPreProdBtn = Button(top, text='CR for Pre-Production', padx=40, pady=10, command = createPreProdWindow)
crProdBtn = Button(top, text="CR for Production", padx=51, pady=10, command = enterProd)
crProdStagingBtn = Button(top, text="CR for Production Staging (Sandbox)", pady=10, command = enterProdStaging)

# Main Window Heading and Spacing
heading = Label(top, text="Select the template to be filled below:", padx=50)
headingSpace = Label(top, text="")
heading.grid(row=0, column=0)
headingSpace.grid(row=1, column=0)

# Layout of Main Window
crPreProdBtn.grid(row=2, column=0)
crProdBtn.grid(row=3, column=0)
crProdStagingBtn.grid(row=4, column=0)

# Run Script
top.mainloop()
