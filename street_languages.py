from __future__ import division
import geopandas as gpd
import whichLanguage

class City(object):
    """Geographic object with info about the street language
    """
    def __init__(self, geofname, city_name, testing=False):
        print("Creating getting the data frame from {}".format(geofname))
        self.df = gpd.read_file(geofname)
        self.cityname = city_name
        if testing:
            ntest = 1000
            print('Testing mode using only {} entries'.format(ntest))
            self.df = self.df.head(n=10)
        self.df = self.df[~self.df['name'].isin([None, ])]
        self.street_en = None
        self.street_fr = None

    def set_language_stats(self):
        """Fill the stats about the street language
        """
        nenglish = 0
        nfrench = 0
        self.df['lang'] = self.df['name'].apply(lambda w: whichLanguage.whichLanguage(w.encode("utf-8")))
        n_total = self.df.shape[0]
        n_fr = (self.df['lang']>0).sum()
        n_en = (self.df['lang']<0).sum()
        #print "nfr = %d, ntot = %d"%(n_fr, n_total)
        self.street_fr = n_fr/n_total
        self.street_en = n_en/n_total
        #self.street_fr = self.df[self.df['lang']<0].count()/self.df.shape[0]
        #self.street_en = 0.4
        #self.street_fr = 0.7

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
        raise ValueError

    def get_city_longlat(self):
        """Returns city longitude,latitude
        """
        rep_point = self.df.iloc[0]['geometry'].representative_point()
        #return self.df.iloc[0]['geometry'].representative_point()
        return (rep_point.x, rep_point.y)


if __name__ == '__main__':
    mtldata = "/Users/jean-francoisrajotte/projects/street_lang/montreal_canada/montreal_canada-roads.geojson"
    #mtldata = "/Users/jean-francoisrajotte/projects/street_lang/montreal_canada/test_montreal_canada-roads.geojson"
    btesting = False
    mtl = City(mtldata, 'Montreal', btesting)
    mtl.set_language_stats()
    #print mtl.df.head()
    print mtl
    print mtl.get_fraction_language('fr')
