import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
from InstalingBOT import InstalingBOT as Bot
from Utilities import resoursce_path
from User import User
from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('INSTALING SCRAPER 1.0')
        self.geometry('300x250')
        self.resizable(False,False)
        #self.iconbitmap("/home/dzik77/Dev/InstalingBot/logo.png")
        #self.iconbitmap(resoursce_path("logo.ico")) to fix

#        icon = Image.open("logo.png")  # Convert your .ico to .png
 #       icon = ImageTk.PhotoImage(icon)
  #      self.iconphoto(True, icon)

        self.login = tk.StringVar()
        self.password = tk.StringVar()
        self.remember = tk.BooleanVar()
        self.parentAccount = tk.BooleanVar()
        self.user = User()
        self.login.set(self.user.login)
        self.password.set(self.user.password)
        self.remember.set(True)
        self.parentAccount.set(self.user.parentAccount)

        self.bot = Bot()

        self.signin = ttk.Frame(self)
        self.signin.pack(padx=10, pady=10, fill='x', expand=True)

        showWords = ttk.Button(self.signin, text="show my words", command=self.show_words)
        showWords.pack(expand = True, anchor = tk.NE)

        loginLabel = ttk.Label(self.signin, text = 'Login:')
        loginLabel.pack(fill='x',expand = True)

        loginEntry = ttk.Entry(self.signin, textvariable=self.login)
        loginEntry.pack(fill='x', expand=True)
        loginEntry.focus()

        passwordLabel = ttk.Label(self.signin, text="Haslo:")
        passwordLabel.pack(fill='x', expand=True)

        passwordEntry = ttk.Entry(self.signin, textvariable=self.password)
        passwordEntry.pack(fill='x', expand=True)

        rememberMe = ttk.Checkbutton(self.signin, text="Zapamietaj mnie", variable=self.remember)
        rememberMe.pack(anchor=tk.W, expand=True)

        parrentAccountButton = ttk.Checkbutton(self.signin, text="Konto rodzica", variable=self.parentAccount)
        parrentAccountButton.pack(anchor=tk.W, expand=True)

        StartSessionButton = ttk.Button(self.signin, text='Zacznij sesje')
        StartSessionButton['command'] = self.start_session
        StartSessionButton.pack()

    def start_session(self):

        if not self.login.get() or not self.password.get():
            return

        if self.remember.get():
            self.user.dump_me(self.login.get(), self.password.get(), self.parentAccount.get())
        else:
            self.user.clear_me(self.parentAccount.get())

        self.bot.init_login_password(self.login.get(), self.password.get())

        bot_functions = [
            self.bot.open_web_browser,
            self.bot.cookies,
            self.bot.login,
            self.bot.make_session,
            self.bot.logout
        ]
        if self.parentAccount.get():
            bot_functions.insert(3,self.bot.get_session_parent_account)

        for func in bot_functions:
            if func() == 1:
                self.bot.save_progress()
                self.bot.close_web_browser()
                return

        self.bot.save_progress()
        self.bot.close_web_browser()

    def show_words(self):
        self.bot.show_my_words()