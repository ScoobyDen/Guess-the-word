from tkinter import *
from random import randint
from tkinter import messagebox

def pressKey(event):
    #print(f"Клавіша: {event.keycode}")
    #CTRL
    if (event.keycode == 17):
        wordLabel["text"] = wordComp

    ch = event.char.upper()
    if (len(ch) == 0):
        return 0
    #print(ch)
    for i in range(len(stringAlphabet)):
        if (ch == stringAlphabet[i]):
            pressLetter(i)

def startNewRound():
    global wordStar, wordComp
    wordComp = dictionary[randint(0, len(dictionary) - 1)]                  #загадуємо слово
    wordStar = "*" * len(wordComp)                                          #формуємо строку з *
    wordLabel["text"] = wordStar                                            #встановлюємо текст в мітку
    wordLabel.place(x=WIDTH // 2 - wordLabel.winfo_reqwidth() // 2, y=50)   #центруємо мітку для виводу слова
    
    for i in range(len(stringAlphabet)):
        btn[i]["text"] = stringAlphabet[i]
        btn[i]["state"] = "normal"

    userTry = 10
    
    updateInfo()

def getWordsFromFile():
    ret = []                                                                #Змінна спсиок для результату, що повертається
    #ставимо блок перевірки помилки
    try:
        #отримуємо діскріптор зверніть увагу на кодіровку, в файлі повинно використовуватися utf-8
        f = open("word.txt", "r", encoding="utf-8")

        for l in f.readlines():                                             #читаємо построков
            l = l.replace("\n", "")                                         #обов'язково вбираємо останній символ переносу строки
            ret.append(l)                                                   #додаємо слово в список
    
        f.close()                                                           #не забуваємо закрити файл
    except:
        print("Проблема з файлом. Программа припиняє роботу")
        quit(0)

    return ret


def saveTopScore():
    global topScore

    topScore = score

    try:
        f = open("top.txt", "w", encoding="utf-8")
        f.write(str(topScore))
        f.close()
    except:
        messagebox.showinfo("Помилка", "Виникла проблема з файлом при зберігання очків рекорду")

def getTopScore():
    try:
        f = open("top.txt", "r", encoding="utf-8")
        m = int(f.readline())
        f.close()
    except:
        m = 0
    return m

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
    global wordStar, score, userTry

    if (btn[n]["text"] == "."):                                         #Перевіряємо, якщо клавіша вже була нажата, то прериваємо метод
        return 0
    btn[n]["text"] = "."
    btn[n]["state"] = "disabled"
    oldWordStar = wordStar
    wordStar = getWordStar(stringAlphabet[n])
    count = compareWord(wordStar, oldWordStar)                          #Знаходимо відмінності між старою та новою версією
    wordLabel["text"] = wordStar

    if (count > 0):
        score += count * 5
    else:
        score -= 20
        if (score < 0):                                                 #Перевіряємо, щоб очки не звалилися в від'ємне значення
            score = 0
        userTry -= 1

    updateInfo() 
    print(f"Ви натиснули на букву {stringAlphabet[n]}")

    if (wordComp == wordStar):
        score += score // 2                                             #додаємо 50% очков
        updateInfo()                                                    #оновлюємо інформацію
        #якщо заработано більше, ніж рекордна кількість, то повідомлюємо і записіємо рекорд
        if (score > topScore):
            messagebox.showinfo("Вітаю!", f"Ви побили рекорд! Вгадане слово: {wordComp}")
            saveTopScore()           
        else:
            messagebox.showinfo("Ви вгадали!", f"Вгадане слово: {wordComp}")      
        startNewRound()
    elif (userTry <= 0):
        messagebox.showinfo("Бу!", "Відведена кількість спроб закінчилася, спробуй ще!")
        quit(0)

def updateInfo():
    scoreLabel["text"] = f"Ваші очки: {score}"
    topScoreLabel["text"] = f"Кращий рещултат: {topScore}"
    userTryLabel["text"] = f"Залишилось спроб: {userTry}"

#Створення вікна
root = Tk()                       #в root зберігається посилання на вікно в пам'яті
root.resizable(False, False)      #забороняємр зміну розмірів вікна
root.title("Вгадай слово")        #Встановлюємо заголовок

root.bind("<Key>", pressKey)      #обробник клавіш

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

score = 0                       # поточні очки
topScore = getTopScore()        # рекорд
userTry = 10                    # кількість спроб

st = ord("А")                                      # для визначення символу на кнопці по коду
btn = []                                            # список для кнопок
stringAlphabet = "АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"  # укр абетка


for i in range(len(stringAlphabet)):
    btn.append(Button(text=stringAlphabet[i], width=2, font="cosolas 15"))
    btn[i].place(x=215 + (i % 11) * 35, y=150 + i //11 * 50)
    btn[i]["command"] = lambda x=i: pressLetter(x)

wordComp = ""                                       #Визначаємо глобально: "загадене слово"
wordStar = ""                                       #Визначаємо глобально: "слово з зірочками"

dictionary = getWordsFromFile()

#стартуємо
startNewRound()

root.mainloop()
