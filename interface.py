from curses import wrapper

def run(stdscr):
    # Clear the screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    stdscr.addstr(1,1,"Playlists")
    stdscr.addstr(2,1,"History*")
    stdscr.addstr(3,1,"Watch Later")
    stdscr.addstr(4,1,"Custom Playlist")
    stdscr.addstr(6,1,"Subscriptions")
    stdscr.addstr(6,1,"*Generic name here")
    stdscr.addstr(7,1,"*Generic name here")
    stdscr.addstr(8,1,"*Generic name here")
    stdscr.addstr(9,1,"*Generic name here")
    stdscr.addstr(10,1,"*Generic name here")
    stdscr.addstr(11,1," Generic name here")
    stdscr.addstr(12,1," Generic name here")
    stdscr.addstr(13,1," Generic name here")

    stdscr.refresh()
    stdscr.getkey()

if __name__ == "__main__":
    wrapper(run)

