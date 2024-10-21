import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
from InstalingBOT import InstalingBOT as Bot
from Utilities import resoursce_path
from User import User

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('INSTALING SCRAPER 1.0')
        self.geometry('300x170')
        self.resizable(False,False)
        self.iconbitmap(resoursce_path("logo.ico"))

        self.login = tk.StringVar()
        self.password = tk.StringVar()
        self.remember = tk.BooleanVar()
        self.user = User()
        self.login.set(self.user.login)
        self.password.set(self.user.password)
        self.remember.set(True)

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

        StartSessionButton = ttk.Button(self.signin, text='Zacznij sesje')
        StartSessionButton['command'] = self.start_session
        StartSessionButton.pack()

    def start_session(self):

        if not self.login.get() or not self.password.get():
            return

        #no risk no reward
        #ans = askyesno(message="Bot is vulnerable for detection wich will temporarly ban your account. Are you sure you want to continue with risk?")

        #if not ans:
        #    self.destroy()
        #    return

        if self.remember.get():
            self.user.dump_me(self.login.get(), self.password.get())
        else:
            self.user.clear_me()

        self.bot.init_login_password(self.login.get(),self.password.get())
        if self.bot.open_web_browser() or self.bot.cookies() or self.bot.login() or self.bot.make_session() or self.bot.logout():
            self.bot.save_progress()
            self.bot.close_web_browser()
        else:
            self.bot.save_progress()
            self.bot.close_web_browser()

    def show_words(self):
        self.bot.show_my_words()