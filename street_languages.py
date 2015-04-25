import geopandas as gpd

class City(object):
    """Geographic object with info about the street language
    """
    def __init__(self, geofname, testing=False):
        print("Creating getting the data frame from {}".format(geofname))
        self.df = gpd.read_file(geofname)
        if testing:
            self.df = self.df.head(n=100)
        self.street_en = None
        self.street_fr = None

    def set_language_stats(self):
        """Fill the stats about the street language
        """
        self.street_en = 0.4
        self.street_fr = 0.7

    def __str__(self):
        out_str = "Data set size: {}x{}\n".format(self.df.shape[0],
                                                  self.df.shape[1])
        out_str += "English fraction: {}\nFrench fraction: {}".format(
            self.street_en, self.street_fr)
        return out_str

    def get_fraction_language(self, lang):
        """Return the fraction of french street names
        """
        if lang.lower() in ('fr', 'french'):
            return self.street_fr
        if lang.lower() in ('en', 'english'):
            return self.street_en


if __name__ == '__main__':
    #mtldata = "/Users/jean-francoisrajotte/projects/street_lang/montreal_canada/montreal_canada-roads.geojson"
    mtldata = "/Users/jean-francoisrajotte/projects/street_lang/montreal_canada/test_montreal_canada-roads.geojson"
    mtl = City(mtldata)
    mtl.set_language_stats()
    print mtl
    print mtl.get_fraction_language('fr')
