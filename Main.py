import qrcode
from tkinter import *
from tkinter import messagebox

# Creating the window
win = Tk()
win.title('QR Code Generator')
win.geometry('650x600')
win.config(bg='DarkTurquoise')

# Function to generate the QR code and save it
def generateCode():
    try:
        qr = qrcode.QRCode(
            version=None,   # Automatically adjusts size
            box_size=10,
            border=5
        )

        qr.add_data(text.get())
        qr.make(fit=True)
        img = qr.make_image()

        fileDir = loc.get() + '\\' + name.get()
        img.save(f'{fileDir}.png')

        messagebox.showinfo("QR Code Generator", "QR Code is saved successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Label for the window
headingFrame = Frame(win, bg="azure", bd=5)
headingFrame.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)
headingLabel = Label(headingFrame, text="Generate QR Code", bg='azure',
                     font=('Times', 20, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Text/URL input
Frame1 = Frame(win, bg="DarkTurquoise")
Frame1.place(relx=0.1, rely=0.17, relwidth=0.7, relheight=0.25)

label1 = Label(Frame1, text="Enter the text/URL: ", bg="DarkTurquoise",
               fg='azure', font=('FiraMono', 13, 'bold'))
label1.place(relx=0.05, rely=0.15, relheight=0.1)

text = Entry(Frame1, font=('Century 12'))
text.place(relx=0.05, rely=0.40, relwidth=1, relheight=0.25)

# Save location input
Frame2 = Frame(win, bg="DarkTurquoise")
Frame2.place(relx=0.1, rely=0.40, relwidth=0.7, relheight=0.25)

label2 = Label(Frame2, text="Enter the location to save the QR Code:",
               bg="DarkTurquoise", fg='azure', font=('FiraMono', 13, 'bold'))
label2.place(relx=0.05, rely=0.15, relheight=0.1)

loc = Entry(Frame2, font=('Century 12'))
loc.place(relx=0.05, rely=0.40, relwidth=1, relheight=0.25)

# QR Code image name
Frame3 = Frame(win, bg="DarkTurquoise")
Frame3.place(relx=0.1, rely=0.63, relwidth=0.7, relheight=0.25)

label3 = Label(Frame3, text="Enter the name of the QR Code:",
               bg="DarkTurquoise", fg='azure', font=('FiraMono', 13, 'bold'))
label3.place(relx=0.05, rely=0.15, relheight=0.1)

name = Entry(Frame3, font=('Century 12'))
name.place(relx=0.05, rely=0.40, relwidth=1, relheight=0.25)

# Generate button
button = Button(win, text='Generate Code', font=('FiraMono', 15),
                command=generateCode)
button.place(relx=0.35, rely=0.90, relwidth=0.30, relheight=0.06)

win.mainloop()
