from tkinter import *
import sqlite3
from tkinter import messagebox


root = Tk()
root.title('Databases')
root.geometry('500x500')

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create a cursor (something that goes off to fetch things for us
c = conn.cursor()

# Create Table (the tables are what actually store the info in the database
''' c.execute("""CREATE TABLE addresses ( 
            first_name text,
            last_name text,
            address text,
            city text, 
            state text,
            zipcode integer)
            """)
'''

# Create a function to save the changes made in the editor window
def save():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_id = id_box.get()

    # Update the entry in the table
    c.execute('''UPDATE addresses SET
            first_name = :first,
            last_Name = :last,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode
            
            WHERE oid = :oid''',
            {'first': f_name_editor.get(),
             'last': l_name_editor.get(),
             'address': address_editor.get(),
             'city': city_editor.get(),
             'state': state_editor.get(),
             'zipcode': zipcode_editor.get(),

             'oid': record_id
             })

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    # Close the editor window
    editor.destroy()


# Create Function to update a record
def update():
    # Account for an empty id box
    if id_box.get() == '':
        messagebox.showerror('Update Record', 'Please enter a valid User Id')
    else:
        global editor
        # Create a new window to update the info
        editor = Tk()
        editor.title('Update A Record')
        editor.geometry('400x250')

        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()

        # Grab the id from the id box that we'll need to update that record
        record_id = id_box.get()

        # Query the database and pull all the info for that specific id
        c.execute('SELECT * FROM addresses WHERE oid=' + record_id)
        records = c.fetchall()

        # Create global text box variables so we can use them outside of this function
        global f_name_editor, l_name_editor, address_editor, city_editor, state_editor, zipcode_editor

        # Create our text boxes for all of the fields in the table
        f_name_editor = Entry(editor, width=30)
        f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
        l_name_editor = Entry(editor, width=30)
        l_name_editor.grid(row=1, column=1, padx=20)
        address_editor = Entry(editor, width=30)
        address_editor.grid(row=2, column=1, padx=20)
        city_editor = Entry(editor, width=30)
        city_editor.grid(row=3, column=1, padx=20)
        state_editor = Entry(editor, width=30)
        state_editor.grid(row=4, column=1, padx=20)
        zipcode_editor = Entry(editor, width=30)
        zipcode_editor.grid(row=5, column=1, padx=20)


        # Create text box labels
        f_name_label = Label(editor, text='First Name')
        f_name_label.grid(row=0, column=0, pady=(10, 0))
        l_name_label = Label(editor, text='Last Name')
        l_name_label.grid(row=1, column=0)
        address_label = Label(editor, text='Address')
        address_label.grid(row=2, column=0)
        city_label = Label(editor, text='City')
        city_label.grid(row=3, column=0)
        state_label = Label(editor, text='State')
        state_label.grid(row=4, column=0)
        zipcode_label = Label(editor, text='Zipcode')
        zipcode_label.grid(row=5, column=0)

        # Create a save Button to save updated record
        save_btn = Button(editor, text="Save Record", command=save)
        save_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=130)

        # Loop through results and update the editor fields with the user's info
        for record in records:
            f_name_editor.insert(0, record[0])
            l_name_editor.insert(0, record[1])
            address_editor.insert(0, record[2])
            city_editor.insert(0, record[3])
            state_editor.insert(0, record[4])
            zipcode_editor.insert(0, record[5])

        # Commit Changes
        conn.commit()
        # Close Connection
        conn.close()

# Create Function to delete record
def delete():

    # We have to reestablish the connection to the db and recreate the cursor in our function!!
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    # Delete a record
    c.execute('DELETE from addresses WHERE oid=' + id_box.get()) # Make sure you concatenate the get
    id_box.delete(0,END) # clear the id box
    query_label.config(text = '') # refresh the records on the screen

    # Create pop up window that confirms deletion of record
    messagebox.showinfo('Databases', 'Record Successfully Deleted')

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()



# Create Submit function for database
def submit():
    # We have to reestablish the connection to the db and recreate the cursor in our function!!
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    # Insert into Table
    c.execute('INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)',
              {'f_name': f_name.get(),
              'l_name': l_name.get(),
              'address': address.get(),
              'city': city.get(),
              'state': state.get(),
              'zipcode': zipcode.get(),
              })


    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    # Clear text boxes so the text isn't sitting there
    f_name.delete(0,END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create query function
def query():
    global query_label
    # We have to reestablish the connection to the db and recreate the cursor in our function!!
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    # Query the database
    ''' SELECT everything, unique id FROM our database table
    sqlite already creates the unique ids for us'''
    c.execute('SELECT *, oid FROM addresses')
    records = c.fetchall() # reads all the records into memory and converts to a list
    # Variable to keep track of the records that we'll print to the screen
    print_records = 'First Name, Last Name, Address, City, State, Zipcode \n\n'

    # Loop through results
    for record in records:
        # Update our print variable with each record in the database
        print_records += str(record) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

# Create our text boxes for all of the fields in the table
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)
id_box = Entry(root,width=30)
id_box.grid(row=9, column=1, pady=(7,0))

# Create text box labels
f_name_label = Label(root, text='First Name')
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text='Last Name')
l_name_label.grid(row=1, column=0)
address_label = Label(root, text='Address')
address_label.grid(row=2, column=0)
city_label = Label(root, text='City')
city_label.grid(row=3, column=0)
state_label = Label(root, text='State')
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text='Zipcode')
zipcode_label.grid(row=5, column=0)
id_box_label = Label(root,text='ID Number:')
id_box_label.grid(row=9, column=0)

# Create Submit button
submit_button = Button(root, text='Add Record to Database', command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=131)

# Create Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=131)

# Create Update Button
delete_btn = Button(root, text="Update Record", command=update)
delete_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=130)

# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()