from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    if country_name == 'Iran, Islamic Rep.':
        return 'ir'
    if country_name == 'Yemen, Rep.':
        return 'ye'
    if country_name == 'Tanzania':
        return 'tz'
    if country_name == 'Venezuela, RB':
        return 've'
    if country_name == 'Vietnam':
        return 'vn'
    if country_name == 'Slovak Republic':
        return 'sk'
    if country_name == 'Moldova':
        return 'md'
    if country_name == 'Macedonia, FYR':
        return 'mk'
    if country_name == 'Bolivia':
        return 'bo'
    if country_name == 'Congo, Dem. Rep.':
        return 'cd'
    if country_name == 'Congo, Rep.':
        return 'cg'
    if country_name == 'Egypt, Arab Rep.':
        return 'eg'
    if country_name == 'Libya':
        return 'ly'
    if country_name == 'Gambia, The':
        return 'gm'
    return None
