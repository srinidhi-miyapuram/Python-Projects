
# We need to provide the date in the format MM-DD-YYYY in the console/terminal
# Ex:- python filename 8-11-2024
# below code will give the week of the day you want to find out

import typer
from datetime import datetime

app = typer.Typer()

@app.command()
def find(name):
    ls = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    day = datetime.strptime(name, "%m-%d-%Y").date()
    num = day.weekday()
    print(f"The day of the week of {name} is {ls[num]}")

    

app()