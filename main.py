from itertools import islice
import PySimpleGUI as sg
import datetime ,os ,MySQLdb
import pandas as pd
from unidecode import unidecode
from utils.layouts import *

from dotenv import load_dotenv
load_dotenv()


def create_date_table(start='', end=''):
    start_ts = pd.to_datetime(start).date()

    end_ts = pd.to_datetime(end).date()

    dates = pd.DataFrame(index=pd.date_range(start_ts, end_ts))
    dates.index.name = 'Date'

    days_names = {
        i: name
        for i, name
        in enumerate(['Monday', 'Tuesday', 'Wednesday',
                      'Thursday', 'Friday', 'Saturday',
                      'Sunday'])
    }

    dates['Day'] = dates.index.dayofweek.map(days_names.get)
    dates.reset_index(inplace=True)
    #dates.index.name = 'date_id'
    return dates



start_key = []
new_rows = []
def button_function(index):
    if not start_key:
        cnx = MySQLdb.connect(user=os.environ['DBUSER'], password=os.environ['DBPASSWORD'],
                              host=os.environ['DBHOST'],
                              database=os.environ['DATABASE'], port=int(os.environ['DBPORT']))
        cursor = cnx.cursor()

        #cursor.execute("SELECT status FROM Program FORCE INDEX(id) WHERE id= %s", (index,))
        cursor.execute("SELECT * FROM Program")

        rows = cursor.fetchall()
        new_rows.append(rows)
        start_key.append(1)
        second_row = new_rows[0]
        for row in second_row:
            if int(index) == row[0]:
                if row[1] == "Paid":
                    return "red"
                elif row[1] == "Reserved":
                    return "yellow"
                else:
                    return "white"

    else:

        second_row = new_rows[0]
        for row in second_row:
            if int(index) == row[0]:
                if row[1] == "Paid":
                    return "red"
                elif row[1] == "Reserved":
                    return "yellow"
                else:
                    return "white"

    return "white"
def create_task(conn, task):
    cur = conn.cursor()
    cur.execute("INSERT INTO Program(id,status,detail) VALUES(%s,%s,%s) ON DUPLICATE KEY UPDATE id = VALUES(id) , status = VALUES(status) , detail = VALUES(detail)",
                (unidecode(task[0]), unidecode(task[1]), unidecode(task[2]),))
    conn.commit()
    return cur.lastrowid


start_key = []
new_rows = []
def button_function(index):
    if not start_key:
        cnx = MySQLdb.connect(user=os.environ['DBUSER'], password=os.environ['DBPASSWORD'],
                              host=os.environ['DBHOST'],
                              database=os.environ['DATABASE'], port=int(os.environ['DBPORT']))
        cursor = cnx.cursor()

        #cursor.execute("SELECT status FROM Program FORCE INDEX(id) WHERE id= %s", (index,))
        cursor.execute("SELECT * FROM Program")

        rows = cursor.fetchall()
        new_rows.append(rows)
        start_key.append(1)
        second_row = new_rows[0]
        for row in second_row:
            if int(index) == row[0]:
                if row[1] == "Paid":
                    return "red"
                elif row[1] == "Reserved":
                    return "yellow"
                else:
                    return "white"

    else:

        second_row = new_rows[0]
        for row in second_row:
            if int(index) == row[0]:
                if row[1] == "Paid":
                    return "red"
                elif row[1] == "Reserved":
                    return "yellow"
                else:
                    return "white"

    return "white"



def saved_button(value):
    if value == "Paid":
        return "red"
    elif value == "Reserved":
        return "yellow"
    else:
        return "white"


def get_detail(index):
    new_index = index.split("-", 1)[0]
    cnx = MySQLdb.connect(user=os.environ['DBUSER'], password=os.environ['DBPASSWORD'],
                          host=os.environ['DBHOST'],
                          database=os.environ['DATABASE'], port=int(os.environ['DBPORT']))
    cursor = cnx.cursor()
    cursor.execute("SELECT detail FROM Program WHERE id= %s", (new_index,))
    rows = cursor.fetchall()
    if len(rows) != 0:
        for row in rows:
            return row[0]
    detail = "date:\n\nphone:\n\nreserved:\n\npaid:\n\n"
    upper_text = detail.upper()
    return upper_text


def get_status(index):
    new_index = index.split("-", 1)[0]
    cnx = MySQLdb.connect(user=os.environ['DBUSER'], password=os.environ['DBPASSWORD'],
                          host=os.environ['DBHOST'],
                          database=os.environ['DATABASE'], port=int(os.environ['DBPORT']))
    cursor = cnx.cursor()
    cursor.execute("SELECT status FROM Program WHERE id = %s", (new_index,))

    rows = cursor.fetchall()

    if len(rows) != 0:
        for row in rows:
            return row[0]
    return "Free"

def create_task(conn, task):
    cur = conn.cursor()
    cur.execute("INSERT INTO Program(id,status,detail) VALUES(%s,%s,%s) ON DUPLICATE KEY UPDATE id = VALUES(id) , status = VALUES(status) , detail = VALUES(detail)",
                (unidecode(task[0]), unidecode(task[1]), unidecode(task[2]),))
    conn.commit()
    return cur.lastrowid




sg.theme('Dark Brown 1')
days_in_year = create_date_table(start="2022-01-01", end="2022-12-31")
days_df1 = days_in_year.loc[:, 'Date']
days_df2 = pd.DataFrame(days_in_year)

for index, row in islice(days_df2.iterrows(), 1, None):
    date = row['Date']
    datem = datetime.datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S")
    month = datem.month
    key_1 = str(index) + "-" + \
        row['Date'].strftime("%m/%d/%Y") + "," + row['Day']
    key_2 = "0" + str(index) + "-" + \
        row['Date'].strftime("%m/%d/%Y") + "," + row['Day']
    if month == 1:
        january_layout += [sg.Text(row['Date'].strftime("%m/%d/%Y"), size=(14, 1)), sg.Text(row['Day'], size=(14, 1)),
                           sg.Button("13/17", size=(14, 1), key=key_1,
                                     button_color=button_function(str(index))),
                           sg.Button("19/23", size=(14, 1), key=key_2, button_color=button_function("0"+str(index))), ],
    elif month == 2:
        february_layout += [sg.Text(row['Date'].strftime("%m/%d/%Y"), size=(14, 1)), sg.Text(row['Day'], size=(14, 1)),
                            sg.Button("13/17", size=(14, 1), key=key_1,
                                      button_color=button_function(str(index))),
                            sg.Button("19/23", size=(14, 1), key=key_2, button_color=button_function("0"+str(index))), ],
    elif month == 3:
        march_layout += [sg.Text(row['Date'].strftime("%m/%d/%Y"), size=(14, 1)), sg.Text(row['Day'], size=(14, 1)),
                         sg.Button("13/17", size=(14, 1), key=key_1,
                                   button_color=button_function(str(index))),
                         sg.Button("19/23", size=(14, 1), key=key_2, button_color=button_function("0"+str(index))), ],
    elif month == 4:
        april_layout += [sg.Text(row['Date'].strftime("%m/%d/%Y"), size=(14, 1)), sg.Text(row['Day'], size=(14, 1)),
                         sg.Button("13/17", size=(14, 1), key=key_1,
                                   button_color=button_function(str(index))),
                         sg.Button("19/23", size=(14, 1), key=key_2, button_color=button_function("0"+str(index))), ],
    elif month == 5:
        may_layout += [sg.Text(row['Date'].strftime("%m/%d/%Y"), size=(14, 1)), sg.Text(row['Day'], size=(14, 1)),
                       sg.Button("13/17", size=(14, 1), key=key_1,
                                 button_color=button_function(str(index))),
                       sg.Button("19/23", size=(14, 1), key=key_2, button_color=button_function("0"+str(index))), ],
    elif month == 6:
        june_layout += [sg.Text(row['Date'].strftime("%m/%d/%Y"), size=(14, 1)), sg.Text(row['Day'], size=(14, 1)),
                        sg.Button("13/17", size=(14, 1), key=key_1,
                                  button_color=button_function(str(index))),
                        sg.Button("19/23", size=(14, 1), key=key_2, button_color=button_function("0"+str(index))), ],
    elif month == 7:
        july_layout += [sg.Text(row['Date'].strftime("%m/%d/%Y"), size=(14, 1)), sg.Text(row['Day'], size=(14, 1)),
                        sg.Button("13/17", size=(14, 1), key=key_1,
                                  button_color=button_function(str(index))),
                        sg.Button("19/23", size=(14, 1), key=key_2, button_color=button_function("0"+str(index))), ],
    elif month == 8:
        august_layout += [sg.Text(row['Date'].strftime("%m/%d/%Y"), size=(14, 1)), sg.Text(row['Day'], size=(14, 1)),
                          sg.Button("13/17", size=(14, 1), key=key_1,
                                    button_color=button_function(str(index))),
                          sg.Button("19/23", size=(14, 1), key=key_2, button_color=button_function("0"+str(index))), ],
    elif month == 9:
        september_layout += [sg.Text(row['Date'].strftime("%m/%d/%Y"), size=(14, 1)), sg.Text(row['Day'], size=(14, 1)),
                             sg.Button("13/17", size=(14, 1), key=key_1,
                                       button_color=button_function(str(index))),
                             sg.Button("19/23", size=(14, 1), key=key_2, button_color=button_function("0"+str(index))), ],
    elif month == 10:
        october_layout += [sg.Text(row['Date'].strftime("%m/%d/%Y"), size=(14, 1)), sg.Text(row['Day'], size=(14, 1)),
                           sg.Button("13/17", size=(14, 1), key=key_1,
                                     button_color=button_function(str(index))),
                           sg.Button("19/23", size=(14, 1), key=key_2, button_color=button_function("0"+str(index))), ],
    elif month == 11:
        november_layout += [sg.Text(row['Date'].strftime("%m/%d/%Y"), size=(14, 1)), sg.Text(row['Day'], size=(14, 1)),
                            sg.Button("13/17", size=(14, 1), key=key_1,
                                      button_color=button_function(str(index))),
                            sg.Button("19/23", size=(14, 1), key=key_2, button_color=button_function("0"+str(index))), ],
    elif month == 12:
        december_layout += [sg.Text(row['Date'].strftime("%m/%d/%Y"), size=(14, 1)), sg.Text(row['Day'], size=(14, 1)),
                            sg.Button("13/17", size=(14, 1), key=key_1,
                                      button_color=button_function(str(index))),
                            sg.Button("19/23", size=(14, 1), key=key_2, button_color=button_function("0"+str(index))), ],

layout = [
    [sg.Column([[sg.TabGroup([
        [sg.Tab('January', january_layout)],
        [sg.Tab('February', february_layout)],
        [sg.Tab('March', march_layout)],
        [sg.Tab('April', april_layout)],
        [sg.Tab('May', may_layout)],
        [sg.Tab('June', june_layout)],
        [sg.Tab('July', july_layout)],
        [sg.Tab('August', august_layout)],
        [sg.Tab('September', september_layout)],
        [sg.Tab('October', october_layout)],
        [sg.Tab('November', november_layout)],
        [sg.Tab('December', december_layout)],


    ])]], scrollable=True, vertical_scroll_only=True,)],  # size=(700,800)
    [sg.Button('Close')]]

window = sg.Window('Reservation Application by Ömer Aydemir',
                   layout, font='Courier 12')

while True:
    event, values = window.read()
    id_array = []
    id_array = [event.split('-', 1)[0]]
    new_event = event
    sg.ChangeLookAndFeel('BrownBlue')

    layout = [
        [sg.Text(event.split("-", 1)[1] + '    ' + 'Program', size=(30, 1),
                 justification='center', font=("Helvetica", 20), relief=sg.RELIEF_RIDGE)],
        [sg.Multiline(default_text=get_detail(event),
                      size=(65, 30), font=("Helvatica", 14))],
        [sg.InputOptionMenu(('Paid', 'Reserved', 'Free'),
                            default_value=get_status(event))],
        [sg.Submit(tooltip='Click to submit this form', button_text="Save"), sg.Cancel(button_text="Back")]]

    new_window = sg.Window(
        'Program', layout, default_element_size=(40, 1), grab_anywhere=False)
    event, values = new_window.read()
    #text = sg.popup_get_text('Title', "asdasdas")
    #sg.popup('Results', 'The value returned from PopupGetText', text)
    if event == "Save":
        conn = MySQLdb.connect(user=os.environ['DBUSER'], password=os.environ['DBPASSWORD'],
                               host=os.environ['DBHOST'],
                               database=os.environ['DATABASE'], port=int(os.environ['DBPORT']))
        with conn:
            task1 = (id_array[0], values[1], values[0])
            s_val = id_array[0]
            create_task(conn, task1)
            try:
                element = window.FindElement(new_event).Update(
                    button_color=saved_button(values[1]))
            except Exception as e:
                print(e)

        new_window.close()
    if event == "Back":
        new_window.close()

window.close()
