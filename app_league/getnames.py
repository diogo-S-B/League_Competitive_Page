from mwrogue.esports_client import EsportsClient
import asyncio


async def getImage(name):
    if name == 'LYON (2024 American Team)':
        name = 'LYON'
    elif name == 'Ninjas in Pyjamas.CN':
        name = 'Ninjas in Pyjamas'
    elif name == "Anyone's Legend":
        name = "Red Canids"

    lowername = name.lower()
    name_mappings = {
        'red': 'Red Canids',
        'geng': 'Gen',
        'gen g': 'Gen',
        'blg': 'Bilibili Gaming',
        'edg': 'EDward Gaming',
        'weibo': 'Weibo Gaming',
        'wbg': 'Weibo Gaming',
        'nip': 'Ninjas in Pyjamas',
        'fpx': 'FunPlus Phoenix',
        'omg': 'Oh My God',
        'ig': 'Invictus Gaming',
        'lng': 'LNG Esports',
        'al': "Anyone's Legend",
        'rng': 'Royal Never Give Up',
        'tt': 'ThunderTalk Gaming',
        'up': 'Ultra Prime',
        'tes': 'Top Esports',
        'top': 'Top Esports',
        'jdg': 'JD Gaming',
        'lgd': 'LGD Gaming',
        'we': 'Team WE',
    }
    
    name = name_mappings.get(lowername, name)

    site = await asyncio.to_thread(EsportsClient, "lol")

    response = await asyncio.to_thread(
        site.cargo_client.query,
        tables="Teams=TS",
        fields="TS.Name, TS.Region, TS.Image, TS.Short",
        where=f"TS.Name = '{name}' OR TS.Short = '{name}'"
    )

    if not response:
        return None, None  # Caso não encontre resultados, evita erro

    imagem = response[0]['Image'].replace(' ', '_')
    name = response[0]['Name']
    
    return imagem, name



