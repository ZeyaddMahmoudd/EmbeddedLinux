import webbrowser

fav = ["google", "facebook", "twitter", "youtube"]
choice = 0

def choose():
    print("Please select your website:")
    for i in range(len(fav)):
        print(str(i+1) + "-" + fav[i])
    choice = int(input()) - 1
    return choice

url = "https://www." + fav[choose()] + ".com"

def Firefox(url):
    webbrowser.get('firefox').open(url)

Firefox(url)