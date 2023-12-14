import curses


def main(stdscr):
    # Initialisieren und Fenstergröße einstellen
    height, width = 10, 40
    start_y, start_x = 5, 5

    # Erstellen eines neuen Fensters
    win = curses.newwin(height, width, start_y, start_x)

    # Rahmen um das Fenster zeichnen
    win.box()

    # Einen Text in das Fenster schreiben
    win.addstr(1, 1, "Dies ist ein benutzerdefiniertes Fenster!")

    # Aktualisieren des Fensters, um die Änderungen anzuzeigen
    win.refresh()

    # Warten auf eine Tasteneingabe
    win.getch()


# Starten des curses-Programms
curses.wrapper(main)
