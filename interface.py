import curses
import curses.panel
import ueberzug.lib.v0 as ueberzug
from result import Result

class Block:
    def __init__(self, result, x, y, canvas):
        self.result = result
        self.x = x
        self.y = y
        self.image = 0;
        self.window = curses.newwin(13,24, x, y)
        self.window.box()
        self.window.addstr(9, 0, self.result.title)
        self.window.addstr(10, 1, self.result.channel)
        self.window.addstr(11, 1, self.result.date)
    def add_image(self, canvas):
        # picy, picx = self.window.getyx()
        # self.window.addstr(6, 0, "" + str( picy ) + " " + str( picx ))
        self.image = canvas.create_placement(self.result.ID, x=33, y=4, max_width=22)
        # self.image = canvas.create_placement(self.result.ID, x=33, y=4, scaler = ueberzug.ScalerOption.CONTAIN.value)
        self.image.path = './2.jpg'
        self.image.visibility = ueberzug.Visibility.VISIBLE

    def remove(self):
        ...

def run(stdscr):
    with ueberzug.Canvas() as c:

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

        win_search = curses.newwin(3,cols-34, 1, 32)
        win_search.box()
        win_search.addstr(1, 2, "Search:   ")
        panel_search = curses.panel.new_panel(win_search)

        # an example result
        result = Result("C++ Tutorial for Beginners - Full Course", "freeCodeCamp.org", "2018-08-24T17:11:35Z", "vLnPwxZdW4Y", "https://i.ytimg.com/vi/vLnPwxZdW4Y/hqdefault.jpg")
        block = Block(result, 4, 33, c)
        block.add_image(c)
        panel = curses.panel.new_panel(block.window)


        curses.panel.update_panels()
        curses.doupdate()

        stdscr.refresh()
        stdscr.getkey()

if __name__ == "__main__":
    curses.wrapper(run)

