import tkinter
from PIL import ImageTk,Image

class MangaReader:
    def __init__(self):
        '''
        pass your custom variables here
        '''
        self.mainWindow = tkinter.Tk()
        self.mainWindow.title('Manga Reader')

    def setup_gui(self):
        '''
        use this to setup the gui
        '''
        #setting up 'next' and 'prev' buttons for pages and chapters
        tkinter.Button(self.mainWindow,text='Prev Chapter').grid(row=0,column=0)
        tkinter.Button(self.mainWindow,text='Next Chapter').grid(row=0,column=2)
        tkinter.Button(self.mainWindow,text='Prev Page').grid(row=3,column=0)
        tkinter.Button(self.mainWindow,text='Next Page').grid(row=3,column=2)
        #canvas for image
        load = Image.open("11.jpg")
        render = ImageTk.PhotoImage(load)
        img = tkinter.Label(self.mainWindow, image=render)
        img.image = render
        img.grid(row=1,column=1)
    def run(self):
        '''
        call this function to start running the GUI
        '''
        self.setup_gui()
        self.mainWindow.mainloop()  

obj = MangaReader()
obj.run()
