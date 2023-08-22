from i18n_modified import COUNTRIES_CODES_ALPHA_2_to_3

def convert_alpha_3_to_2(country_code):
    for alpha_2, alpha_3 in COUNTRIES_CODES_ALPHA_2_to_3.items():
        if country_code == alpha_3.upper():
            return alpha_2
    return None