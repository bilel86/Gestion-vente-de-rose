import tkinter as tk
import mysql.connector
from tkinter import *
  
 
def submitact():
     
    user = Username.get()
    passw = password.get()
  
    print(f"The name entered by you is {user} {passw}")
  
    logintodb(user, passw)
  
 
def logintodb(user, passw):
     
    # If password is entered by the
    # user
    if passw:
        db = mysql.connector.connect(host ="localhost",
                                     user = user,
                                     password = passw,
                                     db ="rosedekairouan")
        cursor = db.cursor()
         
    # If no password is entered by the
    # user
    else:
        db = mysql.connector.connect(host ="localhost",
                                     user = user,
                                     db ="rosedekairouan")
        cursor = db.cursor()
         
    # A Table in the database
    savequery = "select * from account"
     
    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()
         
        # Printing the result of the
        # query
        for x in myresult:
            print(x)
        print("Query Executed successfully")
         
    except:
        db.rollback()
        print("Error occurred")
  
 
root = tk.Tk()
root.geometry("600x400+400+100")
root.title("Rose de kairouan")
  
 
# Defining the first row
lblfrstrow = tk.Label(root, text ="Username -", )
lblfrstrow.place(x = 150, y = 70)
 
Username = tk.Entry(root, width = 35)
Username.place(x = 250, y = 70, width = 160)
  
lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 150, y = 120)
 
password = tk.Entry(root, width = 35)
password.place(x = 250, y = 120, width = 160)
 
submitbtn = tk.Button(root, text ="Login",
                      bg ='blue', command = submitact)
submitbtn.place(x = 250, y = 205, width = 95)

bouton=tk.Button(root, text="Exit",bg='blue', command=root.quit)
bouton.place(x = 400, y = 205, width = 95)



 
root.mainloop()
