from mwrogue.esports_client import EsportsClient
from django.shortcuts import render, redirect
from django.contrib import messages
from app_league import getPlayers
from app_league import getnames
import datetime as dt
import asyncio



def home(request):
    return render(request, 'home.html')


async def teamname(request):
        try:
            teamname = request.POST.get('teamname', None)
            
            date = "2025-01-25"
            date = dt.datetime.strptime(date, "%Y-%m-%d").date()
            count = 1
            try:
                name_list = await getnames.getImage(teamname)
                name = str(name_list[1])
            except:
                print('Erro')

            site = await asyncio.to_thread(EsportsClient, "lol")
            response = await asyncio.to_thread(
                site.cargo_client.query,
                tables= "MatchSchedule=MS, Tournaments=T",
                limit= 50,
                join_on= "MS.OverviewPage = T.OverviewPage",
                fields="T.Name=Tournament, MS.Team1, MS.Team2, MS.Winner, MS.Team1Score, MS.Team2Score",
                where=f"MS.Team1 = '{name}' OR MS.Team2 = '{name}'",
                order_by = "MS.DateTime_UTC DESC")
            
            listas = {"Times": [],
                    "Player_Images": [],
                    "Team_Images": [],
                    "Player_Names": []}

            
            try:
                nameteam_list = await getnames.getImage(name)
            except:
                print('Error')
            nameteam = str(nameteam_list[0])




            for c in response:
                li = []
                li.clear()
                time1 = c["Team1"]
                time2 = c["Team2"]
                gg = c["Winner"]
                

                image_url = f"https://lol.fandom.com/wiki/Special:FilePath/{nameteam}"
            
                

                if c["Team1Score"] != None and c["Team2Score"]:
                    if count <= 5:
                        li.append(time1)
                        li.append(time2)
                        li.append(gg)
                        if c["Team1Score"] != None:
                            li.append(f'{c["Team1Score"]} x {c["Team2Score"]}')
                        elif c["Team1Score"] == None:
                            li.append(f' X ')


                        if c['Team1Score'] == None and c['Team2Score']  == None:
                            li.append('-')
                        else:
                            if c["Winner"] == "1" and time1 == name or c["Winner"] == "2" and time2 == name:
                                li.append('Vitória')
                            else:
                                li.append('Derrota')
                    
                        count += 1
                        listas["Times"].append(li)

            listas["Player_Images"].append(await getPlayers.gets(name))
            listas["Player_Names"].append(await getPlayers.get_playerImages(name))
            listas["Team_Images"].append(image_url)
            return render(request, "sul.html", {'listas': listas})

        except:
            messages.error(request, 'Time não encontrado!')
            return redirect('home')




async def ltanorth(request):
    site = await asyncio.to_thread(EsportsClient, "lol")
    try:
        response = await asyncio.to_thread(
            site.cargo_client.query,
            tables="ScoreboardGames=SG, Tournaments=T",
            join_on="SG.OverviewPage=T.OverviewPage",
            fields="T.Name, SG.DateTime_UTC, SG.Team1, SG.Team2, T.Prizepool",
            where="SG.DateTime_UTC >= '2019-08-01 00:00:00' AND T.Name = 'LTA North 2025 Split 1'",
        )
    except:            
        messages.error(request, 'Muitas requisições, por gentileza aguardar até 1 ~ 2 minutos')
        return redirect('home')
    imagepath = 'https://lol.fandom.com/wiki/Special:FilePath/'
    

    teams = {c['Team1'] for c in response}


    try:
        image_results = await asyncio.gather(*(getnames.getImage(team) for team in teams))
    except:            
        messages.error(request, 'Muitas requisições, por gentileza aguardar até 1 ~ 2 minutos')
        return redirect('home')


    team_images = [imagepath + img[0] if img else None for img in image_results]
    n = 0
    lista = []
    for c in teams:
        lista.append([c,team_images[n]])
        n+=1
    


    listas = {
        'Teams': []
        # 'Teams': list(teams),
        # 'TeamImage': team_images
    }
    listas["Teams"].append(sorted(lista))

    return render(request, "ltanorth.html", {'listas': listas})



async def lpl(request):
    site = await asyncio.to_thread(EsportsClient, "lol")
    try:
        response = await asyncio.to_thread(
            site.cargo_client.query,
            tables="ScoreboardGames=SG, Tournaments=T",
            join_on="SG.OverviewPage=T.OverviewPage",
            fields="T.Name, SG.DateTime_UTC, SG.Team1, SG.Team2, T.Prizepool",
            where="SG.DateTime_UTC >= '2019-08-01 00:00:00' AND T.Name = 'LPL 2025 Split 1'",
        )
    except:            
        messages.error(request, 'Muitas requisições, por gentileza aguardar até 1 ~ 2 minutos')
        return redirect('home')



    imagepath = 'https://lol.fandom.com/wiki/Special:FilePath/'
    

    teams = {c['Team1'] for c in response}

    try:
        image_results = await asyncio.gather(*(getnames.getImage(team) for team in teams))
    except:            
        messages.error(request, 'Muitas requisições, por gentileza aguardar até 1 ~ 2 minutos')
        return redirect('home')    

    team_images = [imagepath + img[0] if img else None for img in image_results]
    n = 0
    lista = []
    for c in teams:
        lista.append([c,team_images[n]])
        n+=1
    


    listas = {
        'Teams': []
    }
    listas["Teams"].append(sorted(lista))

    return render(request, "lpl.html", {'listas': listas})



async def lck(request):
    site = await asyncio.to_thread(EsportsClient, "lol")

    try:
        response = await asyncio.to_thread(
            site.cargo_client.query,
            tables="ScoreboardGames=SG, Tournaments=T",
            join_on="SG.OverviewPage=T.OverviewPage",
            fields="T.Name, SG.DateTime_UTC, SG.Team1, SG.Team2, T.Prizepool",
            where="SG.DateTime_UTC >= '2019-08-01 00:00:00' AND T.Name = 'LCK Cup 2025'",
        )
    except:            
        messages.error(request, 'Muitas requisições, por gentileza aguardar até 1 ~ 2 minutos')
        return redirect('home')

    imagepath = 'https://lol.fandom.com/wiki/Special:FilePath/'
    

    teams = {c['Team1'] for c in response}

    try:
        image_results = await asyncio.gather(*(getnames.getImage(team) for team in teams))
    except:            
        messages.error(request, 'Muitas requisições, por gentileza aguardar até 1 ~ 2 minutos')
        return redirect('home')
    
    team_images = [imagepath + img[0] if img else None for img in image_results]
    n = 0
    lista = []
    for c in teams:
        lista.append([c,team_images[n]])
        n+=1
    


    listas = {
        'Teams': []
        # 'Teams': list(teams),
        # 'TeamImage': team_images
    }
    listas["Teams"].append(sorted(lista))

    return render(request, "lck.html", {'listas': listas})




async def ltasouth(request):
    site = await asyncio.to_thread(EsportsClient, "lol")

    try:
        response = await asyncio.to_thread(
            site.cargo_client.query,
            tables="ScoreboardGames=SG, Tournaments=T",
            join_on="SG.OverviewPage=T.OverviewPage",
            fields="T.Name, SG.DateTime_UTC, SG.Team1, SG.Team2, T.Prizepool",
            where="SG.DateTime_UTC >= '2019-08-01 00:00:00' AND T.Name = 'LTA South 2025 Split 1'",
        )
    except:            
        messages.error(request, 'Muitas requisições, por gentileza aguardar até 1 ~ 2 minutos')
        return redirect('home')
    
    imagepath = 'https://lol.fandom.com/wiki/Special:FilePath/'
    

    teams = {c['Team1'] for c in response}

    try:
        image_results = await asyncio.gather(*(getnames.getImage(team) for team in teams))
    except:            
        messages.error(request, 'Muitas requisições, por gentileza aguardar até 1 ~ 2 minutos')
        return redirect('home')


    team_images = [imagepath + img[0] if img else None for img in image_results]
    n = 0
    lista = []
    for c in teams:
        lista.append([c,team_images[n]])
        n+=1
    


    listas = {
        'Teams': []
        # 'Teams': list(teams),
        # 'TeamImage': team_images
    }
    listas["Teams"].append(sorted(lista))

    return render(request, "ltasul.html", {'listas': listas})
