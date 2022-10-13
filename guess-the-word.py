from tkinter import *
from random import randint

def startNewRound():
    global wordStar, wordComp
    wordComp = "ІНТЕРНЕТ"                                                   #загадуємо слово
    wordStar = "*" * len(wordComp)                                          #формуємо строку з *
    wordLabel["text"] = wordStar                                            #встановлюємо текст в мітку
    wordLabel.place(x=WIDTH // 2 - wordLabel.winfo_reqwidth() // 2, y=50)   #центруємо мітку для виводу слова

def getWordsFromFile():
    pass

def saveTopScore():
    pass

def getTopScore():
    pass

def pressKey(event):
    pass

def compareWord(s1, s2):
    res = 0                                                             #результат, що повертається
    for i in range(len(s1)):                                            #Порівнюємо s1 та s2 посимвольно
        if (s1[i] != s2[i]):                                            #якщо символи різні то збільшуємо res
            res += 1
    #print(f"{res}")
    return res


def getWordStar(ch):
    ret = ""                                                            #Змінна для результату
    for i in range(len(wordComp)):
        if (wordComp[i] == ch):
            ret += ch
        else:
            ret += wordStar[i]
    return ret

def pressLetter(n):
    global wordStar
    btn[n]["text"] = "."
    btn[n]["state"] = "disabled"
    oldWordStar = wordStar
    wordStar = getWordStar(stringAlphabet[n])
    count = compareWord(wordStar, oldWordStar)                          #Знаходимо відмінності між старою та новою версією
    wordLabel["text"] = wordStar
    
    print(f"Ви натиснули на букву {stringAlphabet[n]}")

def updateInfo():
    pass

#Створення вікна
root = Tk()                       #в root зберігається посилання на вікно в пам'яті
root.resizable(False, False)      #забороняємр зміну розмірів вікна
root.title("Вгадай слово")        #Встановлюємо заголовок

#Налаштування геометрії вікна
WIDTH = 810  #Ширина
HEIGHT = 320 #Висота
SCR_WIDTH = root.winfo_screenwidth()   #Ширина екрану в пікселях
SCR_HEIGHT = root.winfo_screenheight() #Висота екрану в пікселях
POS_X = SCR_WIDTH // 2 - WIDTH // 2    #Координата по Х
POS_Y = SCR_HEIGHT // 2 - HEIGHT // 2  #Координата по Y
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
#все теж саме що і зверху але в однну строку
#root.geometry(f"{810}x{320}+{root.winfo_screenwidth() // 2 - 810 // 2}+{root.winfo_screenheight() // 2 - 320 // 2}")

wordLabel = Label(font="consolas 35")               #Мітка для вивода слова, яке людина вгадує
scoreLabel = Label(font=", 12")                     #Мітка для відображення поточних очків і рекорду
topScoreLabel = Label(font=", 12")
userTryLabel =Label(font=", 12")                    #Мітка попиток що залишилися

#Встановлюємо мітки у вікні
scoreLabel.place(x=10, y=165)
topScoreLabel.place(x=10, y=190)
userTryLabel.place(x=10, y=215)

score = 0           # поточні очки
topScore = 1000     # рекорд
userTry = 10        # кількість спроб

#st = ord("А")                                      # для визначення символу на кнопці по коду
btn = []                                            # список для кнопок
stringAlphabet = "АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"  # укр абетка


for i in range(len(stringAlphabet)):
    btn.append(Button(text=stringAlphabet[i], width=2, font="cosolas 15"))
    btn[i].place(x=215 + (i % 11) * 35, y=150 + i //11 * 50)
    btn[i]["command"] = lambda x=i: pressLetter(x)

wordComp = ""                                       #Визначаємо глобально: "загадене слово"
wordStar = ""                                       #Визначаємо глобально: "слово з зірочками"

#стартуємо
startNewRound()

root.mainloop()