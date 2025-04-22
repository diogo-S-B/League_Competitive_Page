from mwrogue.esports_client import EsportsClient
import datetime as dt

def getLTASul():
    site = EsportsClient("lol")
    response = site.cargo_client.query(
        tables= "Teams=TS",
        fields="TS.Name, TS.Region, TS.Image, TS.Short",
        where = f"TS.Name = '{name}' OR TS.Short = '{name}'")

    imagem = response[0]['Image']
    name = response[0]['Name']
    return imagem.replace(' ', '_'), name