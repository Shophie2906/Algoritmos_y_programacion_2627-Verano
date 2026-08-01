from App import App
from db import db

def main():
    app = App(db)
    app.start()

main()