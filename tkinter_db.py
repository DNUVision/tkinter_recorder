from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Tkinter DB")
root.geometry("400x600")

# Create a DB or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
            )""")
'''

# Create Function to delete a record
def delete():
    # Create a DB or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE FROM addresses WHERE oid= " + delete_box.get())



    # Commit changes to DB
    conn.commit()

    # Close connection to the DB
    conn.close()

# Create Update Function for Database
def edit():
    # Create a DB or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute(""" UPDATE addresses SET
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode
            
            WHERE oid = :oid""",
              {"first": f_name_updator.get(),
               "last": l_name_updator.get(),
               "address": address_updator.get(),
               "city": city_updator.get(),
               "state": state_updator.get(),
               "zipcode": zipcode_updator.get(),
               "oid": record_id
               })

    # Commit changes to DB
    conn.commit()

    # Close connection to the DB
    conn.close()

    updator.destroy()
def update():
    global updator
    updator = Tk()
    updator.title("Update a Record")
    updator.geometry("400x200")

    # Create a DB or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    record_id = delete_box.get()
    # Query Database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
    # print(records)

    # Create Global Variables for text box names
    global f_name_updator
    global l_name_updator
    global address_updator
    global city_updator
    global state_updator
    global zipcode_updator

    # Create text boxes
    f_name_updator = Entry(updator, width=30)
    f_name_updator.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_updator = Entry(updator, width=30)
    l_name_updator.grid(row=1, column=1, padx=20)

    address_updator = Entry(updator, width=30)
    address_updator.grid(row=2, column=1, padx=20)

    city_updator = Entry(updator, width=30)
    city_updator.grid(row=3, column=1, padx=20)

    state_updator = Entry(updator, width=30)
    state_updator.grid(row=4, column=1, padx=20)

    zipcode_updator = Entry(updator, width=30)
    zipcode_updator.grid(row=5, column=1, padx=20)


    # create text box labels
    f_name_label_updator = Label(updator, text="First Name")
    f_name_label_updator.grid(row=0, column=0, pady=(10, 0))

    l_name_label_updator = Label(updator, text="Last Name")
    l_name_label_updator.grid(row=1, column=0)

    address_label_updator = Label(updator, text="Address")
    address_label_updator.grid(row=2, column=0)

    city_label_updator = Label(updator, text="City")
    city_label_updator.grid(row=3, column=0)

    state_label_updator = Label(updator, text="State")
    state_label_updator.grid(row=4, column=0)

    zipcode_label_updator = Label(updator, text="Zip Code")
    zipcode_label_updator.grid(row=5, column=0)

    # Create a Save Button to save edited record
    update_btn = Button(updator, text="Save Record", command= edit)
    update_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

    # Loop through results
    for record in records:
        f_name_updator.insert(0, record[0])
        l_name_updator.insert(0, record[1])
        address_updator.insert(0, record[2])
        city_updator.insert(0, record[3])
        state_updator.insert(0, record[4])
        zipcode_updator.insert(0, record[5])

# Create Submit Function for Database
def submit():
    # Create a DB or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    #Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  "f_name": f_name.get(),
                  "l_name": l_name.get(),
                  "address": address.get(),
                  "city": city.get(),
                  "state": state.get(),
                  "zipcode": zipcode.get()
              })


    # Commit changes to DB
    conn.commit()

    # Close connection to the DB
    conn.close()


    #Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create Query Function for Database
def query():
    # Create a DB or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Query Database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)

    # Iteratre through records
    print_records = ""
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text = print_records)
    query_label.grid(row = 12, column = 0, columnspan = 2)


    # Commit changes to DB
    conn.commit()

    # Close connection to the DB
    conn.close()


# Create text boxes
f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20, pady = (10, 0))

l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1, padx = 20)

address = Entry(root, width = 30)
address.grid(row = 2, column = 1, padx = 20)

city = Entry(root, width = 30)
city.grid(row = 3, column = 1, padx = 20)

state = Entry(root, width = 30)
state.grid(row = 4, column = 1, padx = 20)

zipcode = Entry(root, width = 30)
zipcode.grid(row = 5, column = 1, padx = 20)

delete_box = Entry(root, width = 30)
delete_box.grid(row = 9, column = 1, padx = 20)


# create text box labels
f_name_label = Label(root, text ="First Name")
f_name_label.grid(row = 0, column = 0, pady = (10, 0))

l_name_label = Label(root, text ="Last Name")
l_name_label.grid(row = 1, column = 0)

address_label = Label(root, text ="Address")
address_label.grid(row = 2, column = 0)

city_label = Label(root, text ="City")
city_label.grid(row = 3, column = 0)

state_label = Label(root, text ="State")
state_label.grid(row = 4, column = 0)

zipcode_label = Label(root, text ="Zip Code")
zipcode_label.grid(row = 5, column = 0)

delete_box_label = Label(root, text = "ID Number")
delete_box_label.grid(row = 9, column = 0)

# Create Submit Button
submit_btn = Button(root, text = "Add Record to Database", command = submit)
submit_btn.grid(row = 6, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# Create a Query Button
query_btn = Button(root, text = "Show Records", command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)

# Create a Delete Button
delete_btn = Button(root, text = "Delete Record", command = delete)
delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 135)

# Create an Update Button
update_btn = Button(root, text = "Update Record", command = update)
update_btn.grid(row = 11, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 135)

# Commit changes to DB
conn.commit()

# Close connection to the DB
conn.close()


#Button(root, text = "Exit Program", command = quit).pack()

root.mainloop()