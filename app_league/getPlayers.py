import asyncio
from mwrogue.esports_client import EsportsClient
import datetime as dt


date = "2025-01-25"
date = dt.datetime.strptime(date, "%Y-%m-%d").date()

async def get_playerImages(teamName):

    site = await asyncio.to_thread(EsportsClient, "lol")

    response = await asyncio.to_thread(
        site.cargo_client.query,

        tables= "ScoreboardPlayers=PI",
        fields="PI.Team, PI.Name, PI.Role",
        where=f"PI.Team = '{teamName}' AND Role IN ('Support','Top','Jungle','Mid','Bot') AND DateTime_UTC > '{date}'",
        order_by = "PI.Role"
    )

    teste = []
    n = ''
    for c in response:
        
        if n != c['Name']:
            if c['Name'].lower() not in 'dynquedo aegis winsome wiz grevthar gumayusi':
                teste.append([c['Name'], c['Role']])
                n = c['Name']

    return teste




async def gets(name):

    site = await asyncio.to_thread(EsportsClient, "lol")

    response = await asyncio.to_thread(
        site.cargo_client.query,
        tables="PlayerImages=TS",
        fields="TS.FileName, TS.Tournament, TS.Team",
        where=f"TS.Team = '{name}'",
        order_by= "TS.Tournament DESC"
    )

    lista = await get_playerImages(name)
    lista_images = []
    for c in lista:
        for entry in response:
            if c[0] in entry.get('FileName', ''):  # Ensure 'FileName' exists
                lista_images.append('https://lol.fandom.com/wiki/Special:FilePath/'+entry["FileName"])
                break

    return lista_images


