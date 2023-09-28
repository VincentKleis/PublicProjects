from requests import get

test = get("https://cdn.watchgoblinslayer.com/file/mangap/1828/10001000/39.jpg")
if str(test) == "<Response [404]>":
    print(test)
if str(test) == "<Response [200]>":
    print(test)