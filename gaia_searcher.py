import math
import os
#from astroquery.gaia import Gaia
from astropy.io.votable import parse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def download_data():
    username = os.getenv("GAIAUSER")  # Gaia username and password stored as env vars
    password = os.getenv("GAIAPASS")
    Gaia.login(user=username, password=password)
    job = Gaia.launch_job_async("SELECT random_index, teff_val, lum_val \
    FROM gaiadr2.gaia_source \
    WHERE random_index<=2000000 \
    AND teff_val IS NOT NULL \
    AND lum_val IS NOT NULL", dump_to_file=True)

    Gaia.logout()

    return job


def open_votable():
    votable = parse("async_20210607024922.vot")
    vot = votable.get_first_table()
    t = vot.to_table()

    return t.to_pandas()


def spectral_classifier(row: pd.Series) -> str:
    # M<3500 K<5000 G<6000 F<7500 A<10000 B<30000 O<60000
    temperature = row["teff_val"]

    def sub_classifier(min: int, max: int, temp: int) -> int:
        s_c = math.floor(((temp - min) * 10) / (max - min))

        return s_c

    if temperature < 3500:
        primary_class = "M"
        sub_class = sub_classifier(0, 3500, temperature)
    elif temperature < 5000:
        primary_class = "K"
        sub_class = sub_classifier(3500, 5000, temperature)
    elif temperature < 6000:
        primary_class = "G"
        sub_class = sub_classifier(5000, 6000, temperature)
    elif temperature < 7500:
        primary_class = "F"
        sub_class = sub_classifier(6000, 7500, temperature)
    elif temperature < 10000:
        primary_class = "A"
        sub_class = sub_classifier(7500, 10000, temperature)
    elif temperature < 30000:
        primary_class = "B"
        sub_class = sub_classifier(10000, 30000, temperature)
    elif temperature < 60000:
        primary_class = "O"
        sub_class = sub_classifier(30000, 60000, temperature)
    else:
        primary_class = "X"
        sub_class = 0

    stellar_class = primary_class + str(sub_class)
    return stellar_class

df = open_votable()
df['spectral_class'] = df.apply(spectral_classifier, axis=1)

#lum_array = df[["teff_val", "lum_val"]].to_numpy()

#plt.imsave("plot.png", lum_array)


print(df)
