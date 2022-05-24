import sqlite3, tkinter, re
from tkinter import messagebox

# configs
root = tkinter.Tk()
root.title('address_book_app')
root.geometry('400x400+375+200')
root.configure(background='dark grey')


conn = sqlite3.connect('address_book.db')

c = conn.cursor()


# c.execute("""CREATE TABLE addresses (
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer
# )""")
def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    delete_regex = re.compile(r'\d+')
    match = delete_regex.findall(str(deleter.get()))

    if match:
        success = tkinter.messagebox.askokcancel('SUCCESS', 'Deleted the record with this ID = ' + deleter.get())
        c.execute("DELETE FROM addresses WHERE oid= " + deleter.get())

    else:
        m = tkinter.messagebox.showerror('ERROR', 'ID must be a number')
        deleter.delete(0, tkinter.END)

    conn.commit()
    conn.close()


def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              }
              )

    conn.commit()
    conn.close()

    f_name.delete(0, tkinter.END)
    l_name.delete(0, tkinter.END)
    address.delete(0, tkinter.END)
    city.delete(0, tkinter.END)
    state.delete(0, tkinter.END)
    zipcode.delete(0, tkinter.END)


# update
def update():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    record_id = deleter.get()

    # column : value to refer to it
    c.execute("""UPDATE addresses SET 
    first_name = :first,
    last_name = :last,
    address = :address,
    city = :city,
    state = :state,
    zipcode = :zipcode
    
                WHERE oid = :oid""",
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zipcode': zipcode_editor.get(),
                  'oid': record_id
              })

    conn.commit()
    conn.close()

    editor.destroy()


# edit
def edit():

    # globals
    global editor
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    record_id = deleter.get()

    delete_regex = re.compile(r'\d+')
    match = delete_regex.findall(str(deleter.get()))

    if match:
        success = tkinter.messagebox.askokcancel('SUCCESS', 'Found the record with this ID = ' + deleter.get())

        # open new window
        editor = tkinter.Tk()
        editor.title('Update Record')
        editor.geometry('400x200+800+200')
        editor.configure(background='dark grey')

        # text boxes
        f_name_editor = tkinter.Entry(editor, width=50)
        f_name_editor.grid(row=0, column=1, padx=20, pady=(25, 0))
        l_name_editor = tkinter.Entry(editor, width=50)
        l_name_editor.grid(row=1, column=1, padx=20)
        address_editor = tkinter.Entry(editor, width=50)
        address_editor.grid(row=2, column=1, padx=20)
        city_editor = tkinter.Entry(editor, width=50)
        city_editor.grid(row=3, column=1, padx=20)
        state_editor = tkinter.Entry(editor, width=50)
        state_editor.grid(row=4, column=1, padx=20)
        zipcode_editor = tkinter.Entry(editor, width=50)
        zipcode_editor.grid(row=5, column=1, padx=20)

        # labels
        f_name_label_editor = tkinter.Label(editor, text='First Name', bg='dark grey', fg='black')
        f_name_label_editor.grid(row=0, column=0, pady=(25, 0))
        l_name_label_editor = tkinter.Label(editor, text='Last Name', bg='dark grey', fg='black')
        l_name_label_editor.grid(row=1, column=0)
        address_label_editor = tkinter.Label(editor, text='Address', bg='dark grey', fg='black')
        address_label_editor.grid(row=2, column=0)
        city_label_editor = tkinter.Label(editor, text='City', bg='dark grey', fg='black')
        city_label_editor.grid(row=3, column=0)
        state_label_editor = tkinter.Label(editor, text='State', bg='dark grey', fg='black')
        state_label_editor.grid(row=4, column=0)
        zipcode_label_editor = tkinter.Label(editor, text='ZIPCode', bg='dark grey', fg='black')
        zipcode_label_editor.grid(row=5, column=0)

        edit_button = tkinter.Button(editor, text='update', bg='grey',command=update)
        edit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=120)

        c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
        # query
        records = c.fetchall()

        for record in records:
            f_name_editor.insert(0, record[0])
            l_name_editor.insert(0, record[1])
            address_editor.insert(0, record[2])
            city_editor.insert(0, record[3])
            state_editor.insert(0, record[4])
            zipcode_editor.insert(0, record[5])

    else:
        m = tkinter.messagebox.showerror('ERROR', 'ID must be a number')
        deleter.delete(0, tkinter.END)

    conn.commit()
    conn.close()


# query
def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    # query
    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()
    print_record = ''

    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1]) + \
                        '\t' + str(record[6]) + '\n'

    query_label = tkinter.Label(root, text=print_record)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()


# text boxes
f_name = tkinter.Entry(root, width=50)
f_name.grid(row=0, column=1, padx=20, pady=(25, 0))
l_name = tkinter.Entry(root, width=50)
l_name.grid(row=1, column=1, padx=20)
address = tkinter.Entry(root, width=50)
address.grid(row=2, column=1, padx=20)
city = tkinter.Entry(root, width=50)
city.grid(row=3, column=1, padx=20)
state = tkinter.Entry(root, width=50)
state.grid(row=4, column=1, padx=20)
zipcode = tkinter.Entry(root, width=50)
zipcode.grid(row=5, column=1, padx=20)
deleter = tkinter.Entry(root, width=50)
deleter.grid(row=9, column=1, padx=20, pady=(25, 0))

# labels
f_name_label = tkinter.Label(root, text='First Name', bg='dark grey', fg='black')
f_name_label.grid(row=0, column=0, pady=(25, 0))
l_name_label = tkinter.Label(root, text='Last Name', bg='dark grey', fg='black')
l_name_label.grid(row=1, column=0)
address_label = tkinter.Label(root, text='Address', bg='dark grey', fg='black')
address_label.grid(row=2, column=0)
city_label = tkinter.Label(root, text='City', bg='dark grey', fg='black')
city_label.grid(row=3, column=0)
state_label = tkinter.Label(root, text='State', bg='dark grey', fg='black')
state_label.grid(row=4, column=0)
zipcode_label = tkinter.Label(root, text='ZIPCode', bg='dark grey', fg='black')
zipcode_label.grid(row=5, column=0)
delete_label = tkinter.Label(root, text='ID Number', bg='dark grey', fg='black')
delete_label.grid(row=9, column=0, pady=(25, 0))

# buttons
submit_button = tkinter.Button(root, text='Add Record To Database', bg='grey', command=submit)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5, ipadx=100)
query_button = tkinter.Button(root, text='Show Records', bg='grey',command=query)
query_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5, ipadx=127)
delete_button = tkinter.Button(root, text='Delete Record', bg='grey',command=delete)
delete_button.grid(row=10, column=0, columnspan=2, padx=10, pady=5, ipadx=127)
update_button = tkinter.Button(root, text='Edit Record', bg='grey',command=edit)
update_button.grid(row=11, column=0, columnspan=2, padx=10, pady=5, ipadx=132)

conn.commit()
conn.close()

root.mainloop()
