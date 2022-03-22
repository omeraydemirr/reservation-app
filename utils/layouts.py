import PySimpleGUI as sg
sg.theme('Dark Brown 1')

headings = ['DATE', 'DAY', 'OPTION 1', 'OPTION 2']

january_layout = [[sg.T('January ')], [sg.Text('  ')] +
                  [sg.Text(h, size=(14, 1)) for h in headings]]
february_layout = [[sg.T('February ')], [sg.Text(
    '  ')] + [sg.Text(h, size=(14, 1)) for h in headings]]
march_layout = [[sg.T('March ')], [sg.Text('  ')] +
                [sg.Text(h, size=(14, 1)) for h in headings]]
april_layout = [[sg.T('April ')], [sg.Text('  ')] +
                [sg.Text(h, size=(14, 1)) for h in headings]]
may_layout = [[sg.T('May ')], [sg.Text('  ')] +
              [sg.Text(h, size=(14, 1)) for h in headings]]
june_layout = [[sg.T('June ')], [sg.Text('  ')] +
               [sg.Text(h, size=(14, 1)) for h in headings]]
july_layout = [[sg.T('July ')], [sg.Text('  ')] +
               [sg.Text(h, size=(14, 1)) for h in headings]]
august_layout = [[sg.T('August ')], [sg.Text('  ')] +
                 [sg.Text(h, size=(14, 1)) for h in headings]]
september_layout = [[sg.T('September ')], [sg.Text(
    '  ')] + [sg.Text(h, size=(14, 1)) for h in headings]]
october_layout = [[sg.T('October ')], [sg.Text('  ')] +
                  [sg.Text(h, size=(14, 1)) for h in headings]]
november_layout = [[sg.T('November ')], [sg.Text(
    '  ')] + [sg.Text(h, size=(14, 1)) for h in headings]]
december_layout = [[sg.T('December ')], [sg.Text(
    '  ')] + [sg.Text(h, size=(14, 1)) for h in headings]]

