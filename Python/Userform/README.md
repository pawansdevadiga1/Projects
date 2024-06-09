# Tkinter User Form Application

This is a simple Tkinter-based GUI application that creates a user form with fields for entering a username and password. When the form is submitted, the entered values are printed to the console.

## Detailed Explanation

1. **Importing Tkinter:**
    ```python
    from tkinter import *
    ```
    This line imports all the classes and functions from the Tkinter module, which is used for creating graphical user interfaces in Python.

2. **Creating the Root Window:**
    ```python
    root = Tk()
    ```
    This line creates the main application window.

3. **Defining the `getvalue` Function:**
    ```python
    def getvalue():
        print(f"Username: {uservalue.get()}")
        print(f"Password: {passvalue.get()}")
    ```
    This function retrieves the values entered in the username and password fields and prints them to the console when the "Submit" button is clicked.

4. **Setting the Window Title:**
    ```python
    root.title("Userform")
    ```
    This line sets the title of the main application window to "Userform".

5. **Resizing the Window:**
    ```python
    root.geometry("396x218")
    root.minsize(396, 218)
    root.maxsize(396, 218)
    ```
    These lines set the dimensions of the window to 396x218 pixels and prevent the window from being resized.

6. **Adding a Heading:**
    ```python
    Label(root, text="User Form", font="cascadia 25 bold").grid(row=0, column=3)
    ```
    This line creates a label with the text "User Form" and a font size of 25 in bold. The label is placed in the first row and fourth column of the grid layout.

7. **Creating Labels for Username and Password:**
    ```python
    username = Label(root, text="Username", font="cascadia 15 bold")
    password = Label(root, text="Password", font="cascadia 15 bold")

    username.grid(row=1, column=2)
    password.grid(row=2, column=2)
    ```
    These lines create labels for the username and password fields, set their font to 15 in bold, and place them in the grid layout.

8. **Creating Entry Fields for Username and Password:**
    ```python
    uservalue = StringVar()
    passvalue = StringVar()

    userentry = Entry(root, textvariable=uservalue)
    passentry = Entry(root, textvariable=passvalue)

    userentry.grid(row=1, column=3)
    passentry.grid(row=2, column=3)
    ```
    These lines create entry fields for the username and password. `StringVar` is used to store the values entered in these fields. The entry fields are placed in the grid layout.

9. **Adding a Submit Button:**
    ```python
    Button(root, text="Submit", command=getvalue).grid(row=7, column=3)
    ```
    This line creates a button with the text "Submit". When clicked, it calls the `getvalue` function. The button is placed in the grid layout.

10. **Running the Main Loop:**
    ```python
    root.mainloop()
    ```
    This line starts the Tkinter event loop, which waits for user interaction and updates the GUI accordingly.

## How to Run the Program

1. Save the code in a file with a `.py` extension, for example, `main.py`.
2. Run the file using Python:
    ```bash
    python main.py
    ```
3. A window will appear with the user form. Enter the username and password, and click "Submit" to print the entered values to the console.
