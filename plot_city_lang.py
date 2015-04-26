import street_languages

city_info_dict = {}
city_info_dict['montreal'] = {'geofile': 'montreal_canada/test_montreal_canada-roads.geojson'}
#city_info_dict['montreal'] = {'geofile': 'montreal_canada/montreal_canada-roads.geojson'}
city_info_dict['calgary'] = {'geofile': 'calgary_canada/calgary_canada-roads.geojson'}
city_info_dict['fredericton'] = {'geofile': 'fredericton_canada/fredericton_canada-roads.geojson'}
city_info_dict['halifax'] = {'geofile': 'halifax_canada/halifax_canada-roads.geojson'}
city_info_dict['hamilton'] = {'geofile': 'hamilton_canada/hamilton_canada-roads.geojson'}
city_info_dict['kamloops'] = {'geofile': 'kamloops_canada/kamloops_canada-roads.geojson'}
city_info_dict['mississauga'] = {'geofile': 'mississauga_canada/mississauga_canada-roads.geojson'}
city_info_dict['ottawa'] = {'geofile': 'ottawa_canada/ottawa_canada-roads.geojson'}

city_info_dict['hampton-roads'] = {'geofile': 'hampton-roads_virginia/hampton-roads_virginia-roads.geojson'}


def plot_cities(city_list):
    """Plotting cities from a list
    """
    cities_longlat_list = []
    cities_lang_frac_fr = []
    cities_lang_frac_en = []
    fcsv = open('city.csv', 'a')
    for icity in city_list:
        igeofname = city_info_dict[icity]['geofile']
        istr_lang = street_languages.City(igeofname, icity)
        istr_lang.set_language_stats()
        print istr_lang
        #print istr_lang.get_city_longlat()
        istr_en = istr_lang.get_fraction_language('en')
        istr_fr = istr_lang.get_fraction_language('fr')
        ilonglat = istr_lang.get_city_longlat()
        cities_longlat_list.append(ilonglat)
        cities_lang_frac_en.append(istr_en)
        cities_lang_frac_fr.append(istr_fr)
        icsvline = "{} {} {} {}\n".format(icity, istr_en, istr_fr,
                                        ilonglat[0], ilonglat[1])
        fcsv.write(icsvline)
        print icsvline
    print cities_longlat_list
    print cities_lang_frac_fr

if __name__ == "__main__":
    plot_cities(['montreal', ])
    #plot_cities(['ottawa', ])
