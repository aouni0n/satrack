# Satrack

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description

Satrack is a Python program that allows you to obtain the current location of various satellites, including the International Space Station (ISS) and NOAA 15, 18, and 19. The program fetches the satellite location data using APIs and displays the longitude and latitude information.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

1. Clone the repository:
   `$ git clone https://github.com/aouni0n/satrack`
   `$ cd satrack`

2. Install the required dependencies. Make sure you have Python and the `requests` library installed:
   `$ pip install requests`

3. Obtain the API key:
To fetch the location of NOAA satellites, you need to sign up on [N2YO.com](https://www.n2yo.com/) and obtain an API key. Replace `"YOUR_API_KEY"` in the `get_satellite_location` function in the `satellite_locator.py` file with your own API key.

## Usage

1. Run the program: `$ python satellite_locator.py`
 
3. Choose a satellite from the provided options:

   - ISS
   - NOAA 15
   - NOAA 18
   - NOAA 19

3. The program will fetch and display the current location (longitude and latitude) of the selected satellite.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Contact

If you have any questions or want to reach out regarding this project, feel free to contact me at aounabbasaws@gmail.com.


