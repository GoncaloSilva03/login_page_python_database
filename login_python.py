#import
import PySimpleGUI as lay
import mysql.connector

#db


mydb = mysql.connector.connect(
  host="localhost", #DB_HOST
  user="*********", #DB_USERNAME
  password="******", #DB_PASSWORD
  database="login_python" #DB_NAME
)

mycursor = mydb.cursor()

#layout
layout = [
    [lay.Text("", key="msg", background_color="Black", text_color="White", pad=(93,0))],
    [lay.Text("Username", background_color="Black")],
    [lay.Input(key="user", size=200)],
    [lay.Text("Password", background_color="Black")],
    [lay.Input(key="password", password_char="*", size=200)],
    [lay.Checkbox(text="Save",background_color="Black")],
    [lay.Button("Login", button_color="Blue", auto_size_button=True, size=(200,20), pad=(20,20))],
    ]

window = lay.Window('Login Page', layout=layout, background_color="black", size=(400,240))

#login validations
while True:
    event, values = window.read()

    if event == lay.WIN_CLOSED:
        break

    elif event == "Login":
        mycursor.execute("select * from users")

        for x in mycursor:
            username_validation = x[0]
            password_validation = x[1]

        user = values["user"]
        password = values["password"]

        if password == password_validation and user == username_validation:
            window["msg"].update("Welcome, " + x[2] + " " + x[3])

        else:
            window["msg"].update("Incorrect Username or Password!")
