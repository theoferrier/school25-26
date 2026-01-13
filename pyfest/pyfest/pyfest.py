lineup = [
    ("Ken Karson", "Rap", 67),
    ("Yeat", "Rap", 41),
    ("Playboi Carti", "Rap", 61)
]

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
    if option == 1:
        print("\n--- Current Lineup ---")
        total_time = 0
        for band in lineup:
            print(f"{band[0]}  {band[1]}  {band[2]} mins")
            total_time += band[2]
        print(f"Total Performance Time: {total_time} mins\n")
    elif option == 2:
        band_name = input("Enter the band's name: ")
        genre = input("Enter the band's genre: ")
        performance_time = int(input("Enter the band's performance time (in mins): "))
        lineup.append((band_name, genre, performance_time))
    elif option == 3:
        first_band = lineup.pop(0)
        lineup.append(first_band)
    elif option == 4:
        name = input("Enter the name of the band to remove: ")
        lineup = [band for band in lineup if band[0] != name]
    elif option == 5:
        band_name = input("Enter the name of the band to move: ")
        # Find the band tuple by name
        band_to_move = None
        for band in lineup:
            if band[0] == band_name:
                band_to_move = band
                break
        if band_to_move:
            lineup.remove(band_to_move)
            lineup.append(band_to_move)
        else:
            print(f"Band '{band_name}' not found in lineup.")
     else:
         break