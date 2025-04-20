
workers1 = {
    "color": "green",
    "height": "2cm",
    "weight": "20kg",
    "tribe": "Hausa"}

workers2 = {
    "color": "yellow",
    "height": "3cm",
    "weight": "25kg",
    "tribe": "yoruba"}

peoples = [workers1, workers2,]
for people in peoples[0:1]:
    print(workers1)
    print(workers2)

cat = {
    "color": "white",
    "sound": "mew!"}
dog = {
    "color": "black",
    "sound": "wawn!"}
pet = [cat, dog]

for pets in pet[0:1]:
    print(pet)
    print(dog)

favourites_places ={
    "Aminu":"Kano",
    "Ahmad":"Jigawa",
    "Kamalu":"Katsina"
    ,"Khadija":"Abuja"}
    
print("What is your favourite place")
for favourite_place in favourites_places.values():
    print(f'my favourite place is {favourite_place}')
favourites_places["Ahmad"]= "favourite number:2"
favourites_places["Aminu"]= "favourite number:9"
favourites_places["Kamalu"]=  "favourite number:8"
favourites_places["Khadija"]=  "favourite number:12"

print(favourites_places)
cities={} 
Kano={
    "country:""Nigeria",
    "population:""20 Million",
    "fact:""Hausa land"}

Ilorin= {
    "country:""Nigeria",
    "population:""10 millions",
    "fact:""Yoruba land"}

madina= {
    "country:""Mecca",
    "population:" "3 millions",
    "fact:""land of prophet (SAW)"}

cities = [Kano,Ilorin,madina]
print(f"Madina:{cities[2]}")
print(f"kano:{cities[0]}")
print(f"Ilorin:{cities[1]}")
