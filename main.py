from tkinter import *
from PIL import ImageTk, Image
from currency_converter import CurrencyConverter

#####################################
# create currency converter object
c = CurrencyConverter()

# create the root window
root = Tk()

################################
################################
def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")

    if uservalue.get() == "BCS201003" or passvalue.get() == "Owais_13579":
        print("Congratulations! complete registration")

    #################
        #############
        label2.grid_forget()
        ##########
        ###########
        user.grid_forget()
        password.grid_forget()
        userentry.grid_forget()
        passentry.grid_forget()
        b11.destroy()
        userpass_label = Label(f3, text="Good times create week people\nWeek people create bad times\nBad times create strong people\nStronge people create good time\nThanku for Registration", bg="Blue", fg="White", padx=10, pady=10, font="TimesNewRoman 7",
        borderwidth=1, relief=RIDGE)
        Title_label.destroy()
        userpass_label.pack(anchor="se")
        user.grid_rowconfigure(0, minsize=0)
        password.grid_rowconfigure(0, minsize=0)
        user.grid_columnconfigure(0, minsize=0)
        password.grid_columnconfigure(0, minsize=0)
        userentry.grid_rowconfigure(0, minsize=0)
        passentry.grid_rowconfigure(0, minsize=0)
        userentry.grid_columnconfigure(0, minsize=0)
        passentry.grid_columnconfigure(0, minsize=0)

        # define function to convert currency
        def convert_currency():
            # get input values from user
            cash = float(entry_cash.get())
            city1 = entry_city1.get()
            city2 = entry_city2.get()

            # convert cash from city1 to city2
            result = c.convert(cash, city1, city2)

            # update result label
            label_result.config(text=f"{cash} {city1} is equal to {result} {city2}")

        # create input widgets
        label_cash = Label(root, text="Enter the amount of cash to convert:")
        entry_cash = Entry(root)
        label_city1 = Label(root, text="Enter the currency code to convert from (e.g. EUR):")
        entry_city1 = Entry(root)
        label_city2 = Label(root, text="To (e.g. USD):")
        entry_city2 = Entry(root)

        # create button to convert currency
        button_convert = Button(root, text="Convert", command=convert_currency)

        # create label to display result
        label_result = Label(root, text="")

        # add widgets to grid
        label_cash.grid(row=0, column=0)
        entry_cash.grid(row=0, column=1)
        label_city1.grid(row=1, column=0)
        entry_city1.grid(row=1, column=1)
        label_city2.grid(row=2, column=0)
        entry_city2.grid(row=2, column=1)
        button_convert.grid(row=3, column=0)
        label_result.grid(row=4, column=0)
        ######################################


    else:
        print("Registration, Not complete")
################################
################################



root.geometry("600x602")
root.minsize(100, 100)
root.maxsize(1200, 800)
root.title("Student: Muhammad Saad Hussain\t\t\t\t\t\t\t\t\t\t\t\t\t\tOwner: Muhammad Owais :)")

#############################
user = Label(root, text="Username")
password = Label(root, text="Password")
user.grid()
password.grid(row=1)


# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1, padx=10 , pady=10)
passentry.grid(row=1, column=1, padx=10 , pady=10)

b11=Button(root, text="Submit", command=getvals)
b11.grid(row=1, column=2)


# frame 1
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.grid(row=2, columnspan=2, sticky="ns")

# frame 2
f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f2.grid(row=0, column=2, rowspan=2, sticky="ne")

# frame 3
f3 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f3.grid(row=0, column=2, rowspan=2, sticky="ne")

Title_label = Label(f1, text="Currency Value", bg="Blue", fg="White", padx=10, pady=10, font="TimesNewRoman 20", borderwidth=3, relief=SUNKEN)
Title_label.pack(fill=X)

def MSH():
    print("Muhammad Saad Hussain")
    print("BCS201003")

b1=Button(f1, fg="red", text="Developer", command=MSH)
b1.pack()

label1 = Label(f2, text="BCS201003\n")
label1.pack(side=LEFT, anchor="nw")

# load the image
image = Image.open("C:\\Users\\S\\PycharmProjects\\pythonProject\\PhotoImage\\1.jpg")

# convert the image to a Tkinter PhotoImage
photo = ImageTk.PhotoImage(image)

# set the maximum size of the image to 300x300 pixels
image.max_size = (300, 200)
image.thumbnail(image.max_size, Image.LANCZOS)

# create a label to display the image
label2 = Label(root, image=photo)
label2.grid(row=0, column=3, rowspan=3, padx=10, pady=10)

# start the event loop
root.mainloop()
