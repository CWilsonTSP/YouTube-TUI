import curses
import curses.panel

def run(stdscr):
    # Clear the screen
    stdscr.clear()
    curses.curs_set(0)
    rows, cols = stdscr.getmaxyx()

    win_playlists = curses.newwin(12,30,0,0)
    win_playlists.box()
    win_playlists.addstr(1, 1, "Playlists", curses.A_STANDOUT)
    win_playlists.addstr(2, 1, "History*")
    win_playlists.addstr(3, 1,"Watch Later")
    win_playlists.addstr(4, 1, "Custom Playlist")

    panel_playlist = curses.panel.new_panel(win_playlists)

    win_subscriptions = curses.newwin(23,30,12,0)
    win_subscriptions.box()
    win_subscriptions.addstr(1,1,"Subscriptions", curses.A_STANDOUT)
    win_subscriptions.addstr(2,1,"*Generic name here")
    win_subscriptions.addstr(3,1,"*Generic name here")
    win_subscriptions.addstr(4,1,"*Generic name here")
    win_subscriptions.addstr(5,1,"*Generic name here")
    win_subscriptions.addstr(6,1,"*Generic name here")
    win_subscriptions.addstr(7,1," Generic name here")
    win_subscriptions.addstr(8,1," Generic name here")
    win_subscriptions.addstr(9,1," Generic name here")
    win_subscriptions.addstr(10,1," Generic name here")
    panel_subscriptions = curses.panel.new_panel(win_subscriptions)

    win_content = curses.newwin(rows-2,cols-30, 0, 30)
    win_content.box()
    panel_content = curses.panel.new_panel(win_content)

    curses.panel.update_panels()
    curses.doupdate()

    stdscr.refresh()
    stdscr.getkey()

if __name__ == "__main__":
    curses.wrapper(run)

