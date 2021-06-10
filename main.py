import requests

token = "Ihr Token"
if (token == "Ihr Token"):
    raise Exception("401 Bitte geben Sie ihr Toke ein")
def getLicked(amount):
    print("Suchen Ihrer Songs")
    returned = []
    offset = 0
    if (amount > 50):
        limit = 50
    else:
        limit = amount
    for i in range(int(amount / 50)):
        url = "https://api.spotify.com/v1/me/tracks?market=ES&limit=" + str(limit) + "&offset=" + str(offset)
        data = {
            "access_token" : token
        }
        result = requests.get(url, params=data)
        if (str(result.status_code) == str(401)):
            print("Ihr Code ist abgelaufen")
            break
        for ii in result.json()["items"]:
            returned.append(ii)
        offset += 50
    return returned

def sort(searchFor, data):
    print("Filtern")
    listSortOut = []
    for i in data:
        found = False
        thingsSearchIn = ["name", "album", "id", "artists"]
        for ii in thingsSearchIn:
            if (searchFor.lower() in str(i["track"][ii]).lower()):
                found = True
                print("found")
        if (found):
            listSortOut.append(i)
    return listSortOut

def removeLike(id):
    print("Löschen")
    url = "https://api.spotify.com/v1/me/tracks?ids=" + str(id)
    data = {
        "Authorization" : "Bearer " + token
    }
    return requests.delete(url, headers=data)

word = input("Keyword: ")
input("Are you sure you want to do that?")
input("You cant undo this!")
input("Press Enter to run.")
listRemoved = ""
amount = int(input("Durchsuchende Songs: "))
count = 0
for i in range(100):
    print("\n \n \n")
print("Lehnen Sie sich zurück, dies kann ein wenig dauern")
found = sort(word, getLicked(amount))

for i in found:
    count += 1
    listRemoved += i["track"]["name"] + "\n"
    removeLike(i["track"]["id"])
    print(len(found)-count)

file = open("removed.txt", 'r')
before = file.read()
file.close()
fileWrite = open("removed.txt", 'a')
fileWrite.write(before + "\n" + listRemoved)
fileWrite.close()
