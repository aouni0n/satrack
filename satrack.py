import requests

# Function to display ASCII art
def display_ascii_art():
    ascii_art = r'''
................................................,,........................................
............,.................................,+?:.......................,................
...........,.......................,,........:?%?.......................,,................
.........,,........................;?+,...,.:%*?+......................,,,................
.......,,..........................,%?*+,..,?*+%;....................,....................
....,...............................+?+**;.;%++%:.........................................
....,...............................,%+++%;??++%:+?:.............,,.......................
.....................................*?+++?%+++%??%;......................................
.....................................*%++++?+++?++%+......................................
....................................,??+++++++++++??......................................
....................................+S*++++++++++++%:.....................................
..................................,*%*+++++++++++++??,....................................
................................,+%%++++++++++++++++%?;,..................................
.............................,:*%?*+*++*+++++++++++++*%?*;:,..............................
..........................,:*??**+**+**++*++++++++++++++*???*+;:,.........................
......................,:;*??**+**++**+++*+++++++++++++**+++++*???*+;,.....................
...................,;+???*****+++**++++*++++++++++++++++**+++++++**???+:,.................
................,;*%?******+++***+++++?++++++++*+++++*+++++***+++++++**??*:,..............
.............,+?%?*****+++++***++++++?*+++++++++*+++++**++++++***++++++++?%?;,............
...........:*%?*+***++++++*?*+++++++**+++++++++++*++++++***++++++***+;;++++*%%+,..........
........,:*%?++**+++++++*?*++++++++**+++++++++++++*++++++++**+++++++**+++++++*%%;.........
.......:?%?++**++++++++*?*+++++++++**+++++++++++++**+++++++++**++++++++***+++++*%?:.......
.....,+S?++**+++++++++*?++++++++++*?+++++++++++++++?++++++++++***++++++++***+++++?%;......
....,*S*++**+++++++++*?+++++++++++?*+++++++++++++++**+++++++++++**+++++++++**+++++?S+.....
...,*S*++**++++++++++?*++++++++++*?*+++++++++++++++**++++++++++++**+++++++++**+++++?S;....
...+S?+++?++++++++++*?+++++++++++*?+++++++++++++++++?+++++++++++++?*+++++++++*?+++++?%:...
..,%%+++**++++++++++?*+++++++++++*?+++++++++++++++++?*++++++++++++*?++++++++++**+++++%?...
..;S*+++?++++++++++*?*+++++++++++*?+++++++++++++++++**+++++++++++++?*++++++++++?+++++?S:..
..*S*++**++++++++++*?++++++++++++*?+++++++++++++++++**+++++++++++++**++++++++++**++++*S+..
..?S+++**++++++++++*?++++++++++++*?+++++++++++++++++*?+++++++++++++*?++++++++++**+++++S*..
..*S+++**++++++++++*?++++++++++++*?++++++++++++++++++?+++++++++++++*?++++++++++**+++++S*..
..+S*+++?++++++++++*?*+++++++++++*?++++++++++++++++++?+++++++++++++*?++++++++++**++++*S+..
..:S?+++**++++++++++?*+++++++++++*?++++++++++++++++++?+++++++++++++*?++++++++++**++++?%:..
...?%++++*++++++++++*?+++++++++++*?++++++++++++++++++?+++++++++++++**++++++++++?+++++%*...
...:%?++++*++++++++++?*+++++++++++?+++;;+++++++++++++?+++++++++++++?++++++++++**++++?%:...
....;%*+++**+++++++++*?+++++++++++?*+++;;;++++++++++*?++++++++++++**+++++++++**++++?S;....
.....;%?+++**+++++++++*?++++++++++*?++++++++++++++++**+++++++++++**+++++++++**++++?S;.....
....,.:%?+++*?*++++++++*?++++++++++?++++++++++++++++**++++++++++*?+++++++++**++++?%;......
.......,?%*+++**++++++++*?+++++++++**+++++++++++++++*++++++++++*?*+++++++*?*+++*%?:.......
.........;%%*+++**+++++++*?*++++++++?+++++++++++++++*+++++++++*?++++++++**+++*%%+,........
..........,+%%*+++***++++++**+++++++**+++++++++++++**++++++++**+++++++**+++*%%+,..........
............,;?%?+++***+++++***++++++*+++++++++++++*+++++++***+++++***+++?%?+,............
...............:*???*++***+++++**+++++*+++++++++++**+++++***++++***++*?%%*;,..............
.................,:+???**++***+++**++++*++++++++++*++++**+++++**+**?%?*;,.................
.....................:;*????****+++++++++++++++++++++++++++***????*;:,....................
.........................,:;+**?????*******************?????*+;:,.........................
...............................,,,;?%*+++++;+;;++++***??::,,..............................
...................................+?+???;+?++?;%S*;%+:?+.................................
.................................:*?*??*++*?:+S;*%?;?**;?+,,:;,...........................
....,.........................,;*??*??**+:+*:?*?;??+%,+*;++*?*,...........................
.............................,;++;:***+:,;?;**,?+***?;.:++++:.............................
..................................,?*++***+**,.*%;,+*?;,..................................
..................................,++.,;;;;:...;;...,,:,..................................
...................................,,.....................................................

        ###     #######  ##     ## ##    ## ####  #######  ##    ## 
       ## ##   ##     ## ##     ## ###   ##  ##  ##     ## ###   ## 
      ##   ##  ##     ## ##     ## ####  ##  ##  ##     ## ####  ## 
     ##     ## ##     ## ##     ## ## ## ##  ##  ##     ## ## ## ## 
     ######### ##     ## ##     ## ##  ####  ##  ##     ## ##  #### 
     ##     ## ##     ## ##     ## ##   ###  ##  ##     ## ##   ### 
     ##     ##  #######   #######  ##    ## ####  #######  ##    ## 

    https://github.com/aouni0n
    '''

    print(ascii_art)

# Function to get satellite location
def get_satellite_location(satellite):
    url = f"http://api.open-notify.org/iss-now.json"  # API URL for ISS
    if satellite.startswith("NOAA"):
        satellite_number = satellite.split(" ")[1]
        url = f"https://www.n2yo.com/rest/v1/satellite/positions/{satellite_number}/41.702/-76.014/0/1/&apiKey=YOUR_API_KEY"  # Replace YOUR_API_KEY with your own API key from N2YO.com

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if satellite.startswith("NOAA"):
            info = data["positions"][0]
            longitude = info["satlongitude"]
            latitude = info["satlatitude"]
            print(f"Satellite: {satellite}")
            print(f"Longitude: {longitude}")
            print(f"Latitude: {latitude}")
        else:
            info = data["iss_position"]
            longitude = info["longitude"]
            latitude = info["latitude"]
            print(f"Satellite: {satellite}")
            print(f"Longitude: {longitude}")
            print(f"Latitude: {latitude}")
    else:
        print("Unable to fetch satellite data.")

# Main program
def main():
    display_ascii_art()

    print("Choose a satellite:")
    print("1. ISS")
    print("2. NOAA 15")
    print("3. NOAA 18")
    print("4. NOAA 19")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        get_satellite_location("ISS")
    elif choice == "2":
        get_satellite_location("NOAA 15")
    elif choice == "3":
        get_satellite_location("NOAA 18")
    elif choice == "4":
        get_satellite_location("NOAA 19")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()