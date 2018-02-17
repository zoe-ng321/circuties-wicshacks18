from bs4 import BeautifulSoup

import pandas as pd

import requests as rq

import numpy as np

import matplotlib.pyplot as plt

import urllib

file = r'dataonmassshootings.csv'
df = pd.read_csv(file)

plt.figure(1)
plt.bar(df["Incident_Date"][:31], df["Killed"][:31])
plt.xticks(rotation=90)
plt.xlabel('Date')
plt.ylabel('# Killed')
plt.title("Number of People Killed in Mass Shooting in 2018")

plt.figure(2)
plt.bar(df["Incident_Date"][:31], df["Injured"][:31])
plt.xticks(rotation=90)
plt.xlabel('Date')
plt.ylabel('# Killed')
plt.title("Number of People Injured in Mass Shooting in 2018")

plt.figure(3)
plt.bar(df["Incident_Date"][31:377], df["Killed"][31:377])
plt.xticks(rotation=90)
plt.xlabel('Date')
plt.ylabel('# Killed')
plt.title("Number of People Killed in Mass Shooting in 2017")


plt.show()
