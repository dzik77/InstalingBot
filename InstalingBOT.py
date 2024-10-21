from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.remote.webelement import WebElement
from Utilities import resoursce_path
import time
import random
import pickle
import os
import math

class InstalingBOT:

    DEFAULT_NEW_WORD_PERCENTAGE = 50.0
    WORD_MAX_VALUE = 100.0
    EPSILON = 1e-9
    Words = {}

    manageOptionsPath = '/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[2]'
    confirmChoicesPath = '/html/body/div[2]/div[2]/div[2]/div[3]/div[2]/button[2]'

    LoginButtonPath = '/html/body/nav/a[2]'
    LoginPath = '/html/body/div[1]/div[3]/form/div/div[1]/div[1]'
    PasswordPath = '/html/body/div/div[3]/form/div/div[1]/*'
    ShowPasswordPath = '/html/body/div[1]/div[3]/form/div/div[1]/div[2]/div[1]/a/i'
    ConfirmLoginPath = '/html/body/div[1]/div[3]/form/div/div[3]/button'

    StartSessionPath = '/html/body/div[1]/div[2]/div/p[1]/a'
    StartSession2Path = '//*[@id="start_session_button"]'
    ContinueSessionPath = '//*[@id="continue_session_button"]'

    SpanishQueryPath = '/html/body/div/div[8]/div[1]/div[1]'
    QueryPath = '/html/body/div/div[8]/div[1]/div[2]/div[2]'
    PromptPath = '//*[@id="answer"]'
    SubmitPath = '//*[@id="check"]'
    SpanishAnswerPath = '/html/body/div/div[9]/div[1]/div[1]'
    AnswerPath = '//*[@id="word"]'
    NextPath = '//*[@id="nextword"]' #//*[@id="next_word"]
    NextGoodPath = '//*[@id="next_word"]'

    BackToMainPath = '//*[@id="return_mainpage"]'
    LogOutPath = '/html/body/div[1]/div[2]/div/p[10]/a'

    def __init__(self):

        self.ChromeOptions = webdriver.ChromeOptions()
        self.ChromeOptions.add_argument("--disable-search-engine-choice-screen")
        self.ChromeOptions.add_argument("--disable-blink-features=AutomationControlled")
        self.ChromeOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.ChromeOptions.add_experimental_option("useAutomationExtension", False)
        self.ChromeOptions.headless = False

        self.Wordspath = resoursce_path("Words.pkl")
        if os.path.getsize(self.Wordspath) > 0:
            with open(self.Wordspath,"rb") as pickle_file:
                self.Words = pickle.load(pickle_file)
    def open_web_browser(self):
        try:
            self.driver = webdriver.Chrome(options=self.ChromeOptions)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            self.driver.maximize_window()
            self.driver.get('https://instaling.pl/')
        except WebDriverException as e:
            print(f"Error: {str(e)}")
            return 1
        return 0

    def close_web_browser(self):
        self.driver.close()
    def init_login_password(self,login:str, password:str):
        self.loginData = login
        self.passwordData = password
    def save_progress(self):
        for v in self.Words.values():
            v[3] = False
        with open(self.Wordspath,"wb") as pickle_file:
            pickle.dump(self.Words,pickle_file)

    def cookies(self) -> int:
        try:

            manageOptions = self.driver.find_element(By.XPATH, self.manageOptionsPath)
            self.move_to_click(manageOptions)

            confirmChoices = self.driver.find_element(By.XPATH, self.confirmChoicesPath)
            self.move_to_click(confirmChoices)
        except NoSuchElementException as e:
            print(f"ERROR: {str(e)}, XPATH Changed")
            return 1
        except WebDriverException as e:
            print(f"Error: {str(e)}")
            return 1
        return 0
    def login(self) -> int:

        try:

            loginButton = self.driver.find_element(By.XPATH, self.LoginButtonPath)
            self.move_to_click(loginButton)

            loginEnter = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.LoginPath)))
            self.slow_type(loginEnter,self.loginData)

            showPassword = self.driver.find_element(By.XPATH, self.ShowPasswordPath)
            self.move_to_click(showPassword)

            passwordEnter = self.driver.find_element(By.XPATH,self.PasswordPath)
            #self.slow_type(passwordEnter,self.passwordData)
            #ActionChains(self.driver).move_to_element(passwordEnter).send_keys(self.passwordData).perform()
            kps = 0.303030303030  # average kps
            action = ActionChains(self.driver).move_to_element(passwordEnter).pause(
                random.uniform(kps - 0.05, kps + 0.05))
            for char in self.passwordData:
                action.send_keys(char)
                action.pause(random.uniform(kps - 0.05, kps + 0.05))
            action.perform()

            time.sleep(random.uniform(0.8,2.0)) #Data enter

            enterData = self.driver.find_element(By.XPATH, self.ConfirmLoginPath)
            self.move_to_click(enterData)

        except NoSuchElementException as e:
            print(f"NO such element: {str(e)}")
            return 1
        except TimeoutException as e:
            print(f"TLE: {str(e)}")
            return 1
        except WebDriverException as e:
            print(f"Error: {str(e)}")
            return 1
        return 0

    def logout(self) -> int:
        try:
            time.sleep(random.uniform(0.5,1.0)) # logout
            logout = WebDriverWait(self.driver,3).until(EC.presence_of_element_located((By.XPATH,self.LogOutPath)))
            self.move_to_click(logout)
        except TimeoutException as e:
            print(f"TLE: {str(e)}")
            return 1
        except WebDriverException as e:
            print(f"Error: {str(e)}")
            return 1
        return 0
    def make_session(self) -> int:

        try:

            startSession = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.StartSessionPath)))
            self.move_to_click(startSession)

            startSession2 = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.StartSession2Path)))
            if not startSession2.is_displayed():
                startSession2 = self.driver.find_element(By.XPATH,self.ContinueSessionPath)

            self.move_to_click(startSession2)

        except NoSuchElementException as e:
            print(f"ERROR: {str(e)}")
            return 1
        except TimeoutException as e:
            print(f"TLE: {str(e)}")
            return 1
        except WebDriverException as e:
            print(f"Error: {str(e)}")
            return 1

        time.sleep(random.uniform(0.5,1.0))
        backToMenu = None
        session = True
        while(session):
            try:
                time.sleep(random.uniform(0.5,1.0))
                query = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.QueryPath)))
                submit = self.driver.find_element(By.XPATH, self.SubmitPath)

                Qrtext = query.text
                val = self.Words.get(query.text)
                if val is not None:
                    if val[3] or random.uniform(0,100) <= val[1]:
                        prompt = self.driver.find_element(By.XPATH, self.PromptPath)
                        self.slow_type(prompt,val[0])
                    else:
                        val[3] = True

                time.sleep(random.uniform(0.5,1.0))
                self.move_to_click(submit)

                time.sleep(random.uniform(0.5,1.0))
                next = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.NextPath)))
                # out dated, there is only one button
                #if not next.is_displayed():
                #    next = WebDriverWait(self.driver, 10).until(
                #        EC.presence_of_element_located((By.XPATH, self.NextGoodPath)))
                #    Ans = True

                if val is None:
                    answer = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.AnswerPath)))
                    self.Words[Qrtext] = [answer.text, self.DEFAULT_NEW_WORD_PERCENTAGE, 1, True]
                else:
                    self.Words.get(Qrtext)[1] = self.progress(val[1],val[2])
                    self.Words.get(Qrtext)[2] += 1

                self.move_to_click(next)

                backToMenu = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.BackToMainPath)))
                if backToMenu.is_displayed():
                    session = False


            except NoSuchElementException as e:
                print(f"ERROR: {str(e)}")
                session = False
                return 1
            except TimeoutException as e:
                print(f"TLE: {str(e)}")
                session = False
                return 1
            except WebDriverException as e:
                print(f"Error: {str(e)}")
                return 1

        try:
            self.move_to_click(backToMenu)
        except NoSuchElementException as e:
            print(f"ERROR: {str(e)}")
            return 1
        except TimeoutException as e:
            print(f"TLE: {str(e)}")
            return 1
        except WebDriverException as e:
            print(f"Error: {str(e)}")
            return 1
        return 0


    def move_to_click(self,button):
        ActionChains(self.driver).move_to_element(button).click(button).perform()

    def slow_type(self, input: WebElement, text: str):
        kps = 0.303030303030  # average kps
        action = ActionChains(self.driver).move_to_element(input).click(input).pause(random.uniform(kps - 0.05, kps + 0.05))
        for char in text:
            action.send_keys(char)
            action.pause(random.uniform(kps - 0.05, kps + 0.05))
        action.perform()

    def progress(self, value, call_count):
        K = 10
        if (abs(50.0 - value) < self.EPSILON):
            Increment = K
        else:
            Increment = K / (math.sqrt(call_count))
        value += Increment
        if (abs(self.WORD_MAX_VALUE - value) < self.EPSILON):
            value = self.WORD_MAX_VALUE
        return value

    def show_my_words(self):
        cnt = 1
        for k,v in self.Words.items():
            print(f'{cnt}: Query="{k}" : Answer="{v[0]}", Knowledge={v[1]}, ProgressCallCount={v[2]}, SecondTime={v[3]}')
            cnt+=1