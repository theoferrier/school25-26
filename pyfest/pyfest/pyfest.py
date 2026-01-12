# The initial lineup
lineup = [
    ("Ken Karson", "Rap", 67),
    ("Yeat", "Rap", 41),
    ("Playboi Carti", "Rap", 61)
]

# 1. Add the headliner
headliner = ("Esdeekid", "UK Rap", 93)
lineup.append(headliner)

print("\n--- Py-Fest 2026 Stage Manager ---")
print("   1. View Lineup & Total Time")
print("        2. Add a New Band")
print("    3. Move First Band to End")
print("     4. Remove Band by Name")
print("   5. Move Band by Specific Name")
print("            6. Exit")
option = int(input("Select an option (1-6): "))
while option != 6:
    if option = 1:
        print("\n--- Current Lineup ---")
        total_time = 0
    if option = 2:
        new_band = str(input("Enter the band's name: "))
        new_genre = str(input("Enter the band's genre: "))
        new_playtime = int(input("Enter the band's play time"))
    if option = 3:
        late_band = lineup.pop(0)