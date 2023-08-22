import csv
from alpha_converter_3_to_2 import convert_alpha_3_to_2
import pygal
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

filename = 'gdp_pr_capita_ppp.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    pygal_dataset = {}
    for row in reader:
        country_code = row[1]
        try:
            gdp_2022 = int(float(row[66]))
        except ValueError as e:
            gdp_2022 = 0
            print(e)
        code = convert_alpha_3_to_2(country_code)
        if code:
            pygal_dataset[code] = gdp_2022

    dataset_1, dataset_2, dataset_3, dataset_4, dataset_5, dataset_6, dataset_7 = {}, {}, {}, {}, {}, {}, {}
    for code, gdp in pygal_dataset.items():
        if gdp < 1_000:
            dataset_1[code] = gdp
        elif gdp < 2_500:
            dataset_2[code] = gdp
        elif gdp < 5_000:
            dataset_3[code] = gdp
        elif gdp < 10_000:
            dataset_4[code] = gdp
        elif gdp < 25_000:
            dataset_5[code] = gdp
        elif gdp < 50_000:
            dataset_6[code] = gdp
        else:
            dataset_7[code] = gdp


wm_style = RS('#004C99', base_style=LCS)

wm = pygal.maps.world.World(fill=True, interpolate='cubic', style=wm_style)

wm.title = 'GDP per capita PPP (current International USD) 2022'

wm.add('<1 000 - ' + str(len(dataset_1)), dataset_1)
wm.add('<2 500 - ' + str(len(dataset_2)), dataset_2)
wm.add('<5 000 - ' + str(len(dataset_3)), dataset_3)
wm.add('<10 000 - ' + str(len(dataset_4)), dataset_4)
wm.add('<25 000 - ' + str(len(dataset_5)), dataset_5)
wm.add('<50 000 - ' + str(len(dataset_6)), dataset_6)
wm.add('>50 000 - ' + str(len(dataset_7)), dataset_7)

wm.render_to_file('gdp_pr_capita_ppp_visual.svg')
