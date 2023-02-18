import PySimpleGUI as sg

# Import the necessary modules from the code
import contextlib
import sys
from pyke import knowledge_engine
from pyke import krb_traceback
engine = knowledge_engine.engine(__file__)

# Define the layout of the GUI
layout = [
    [sg.Text('Enter your symptoms:')],
    [sg.InputText()],
    [sg.Button('Check for Dental Abscess')]
]

# Create the window
window = sg.Window('Dental Abscess Checker', layout)

# Set up the event loop
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    elif event == 'Check for Dental Abscess':
        symptoms = values[0]
        engine.reset()  # Allows us to run tests multiple times.
        engine.activate('bc_simple_rules_questions')
        try:
            with engine.prove_goal(
                    'bc_simple_rules_questions.what_to_should($bring)') as gen:
                for vars, plan in gen:
                    sg.popup(f'You should bring: {vars["bring"]}')
        except Exception:
            krb_traceback.print_exc()
            sys.exit(1)

window.close()
