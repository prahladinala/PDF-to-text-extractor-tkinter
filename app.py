from tkinter import *
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
# from functions import display_logo, display_textbox, extract_images

# START WITH root
root = Tk()

# SET WIDTH AND HEIGHT
canvas = Canvas(root, width=600, height=300)
# initalize the canvas
canvas.grid(columnspan=3, rowspan=3)
# columnspan=3 > splits canvas into 3 identical columns

# SETTING UP THE LOGO
logo = Image.open("logo.png")
# converting logo image to tkinter image
logo = ImageTk.PhotoImage(logo)
# placing logo in label
logo_label = Label(image=logo)
logo_label.image = logo
# place it inside window object
logo_label.grid(column=1,row=0)

# INSTRUCTIONS
instructions = Label(root, text="Select a PDF file on your computer to extract all its text", font="Raleway")
# placing instructions on grid > span across 3 columns > as text length is large
instructions.grid(columnspan=3, column=0, row=1)

# FUNCTION TO OPEN FILE
def open_file():
    # changing button text
    browse_text.set("Loading...")
    # open a file
    # mode='rb' > read only
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("Pdf File", "*.pdf")])
    # if file is selected
    if file:
        # store it in a variable
        read_pdf = PyPDF2.PdfFileReader(file)
        # loading pages in variable
        page = read_pdf.getPage(0)
        # getting page content
        page_content = page.extractText()
        
        # TEXT BOX > to show the text in the pdf
        text_box = Text(root, height=10, width=50, padx=15, pady=15)
        # setting text inside the text box
        text_box.insert(1.0, page_content)
        # setting text to center
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        # setting textbox inside a grid
        text_box.grid(column=1, row=3)

        # Set Loading to Browse again
        browse_text.set("Browse")

        



# BROWSER BUTTON
# variable for button text
browse_text = StringVar()
# Button
browse_btn = Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
# set browser text
browse_text.set("Browse")
# placing button to grid
browse_btn.grid(column=1, row=2)


# TO SETUP MARGIN
canvas = Canvas(root, width=600, height=250)
# initalize the canvas
canvas.grid(columnspan=3)
# columnspan=3 > splits canvas into 3 identical columns

root.mainloop()
# END WITH mainloop()

# ABOVE AND BELOW CODE WILL NOT APPEAR IN WINDOW