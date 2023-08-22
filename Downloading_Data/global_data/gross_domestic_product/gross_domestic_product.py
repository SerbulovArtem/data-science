import csv
from alpha_converter_3_to_2 import convert_alpha_3_to_2
import pygal
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

filename = 'gross_domestic_product_1960_2022.csv'

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

    dataset_1, dataset_2, dataset_3, dataset_4, dataset_5, dataset_6 = {}, {}, {}, {}, {}, {}
    for code, gdp in pygal_dataset.items():
        if gdp < 10_000_000_000:
            dataset_1[code] = gdp
        elif gdp < 100_000_000_000:
            dataset_2[code] = gdp
        elif gdp < 500_000_000_000:
            dataset_3[code] = gdp
        elif gdp < 1_000_000_000_000:
            dataset_4[code] = gdp
        elif gdp < 5_000_000_000_000:
            dataset_5[code] = gdp
        else:
            dataset_6[code] = gdp


wm_style = RS('#004C99', base_style=LCS)

wm = pygal.maps.world.World(fill=True, interpolate='cubic', style=wm_style)

wm.title = 'Gross Domestic Product (Annual in USD) 2022'

wm.add('<10b - ' + str(len(dataset_1)), dataset_1)
wm.add('<100b - ' + str(len(dataset_2)), dataset_2)
wm.add('<500b - ' + str(len(dataset_3)), dataset_3)
wm.add('<1tr - ' + str(len(dataset_4)), dataset_4)
wm.add('<5tr - ' + str(len(dataset_5)), dataset_5)
wm.add('>5tr - ' + str(len(dataset_6)), dataset_6)

wm.render_to_file('gdp_2022_visual.svg')
