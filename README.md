# street_lang
Cities street language classification
This project calculates and plots the fraction of streets
assumed to be english or french based bi- and trigrams frequency.

## Installation
This code has been tested on python 2.7
The following modules need to be install

* [geopandas](https://github.com/geopandas/geopandas)
* [mplleaflet](https://github.com/jwass/mplleaflet)

## Usage
This code comes with a limited list of preprocessed cities.
To plot them, simply type (in the root directory)
`python plot_city_lang.py`

## Adding more cities
More cities can be added by copying data from the [OpenStreetMap metro extract page](https://mapzen.com/metro-extracts/) (using the format IMPOSM GEOJSON).

## Credits

* Jean-Francois Rajotte
* Philippe Brouillard
