import requests
import discord
import json
from datetime import datetime
from discord.ext import commands


bot = commands.Bot("&")


@bot.event
async def on_ready():
    print(f"Estou pronto! Estou conectado como {bot.user}")

@bot.command(name="oi")
async def mandar_oi(ctx):
    name = ctx.author.name

    resposta = "Olá, " + name

    await ctx.send(resposta)

@bot.command(name="Apod")
async def apod(ctx, *expression):
    expression = " ".join(expression)
    expression = expression.split()
    if len(expression) == 1:
        dict = requests.get(f"https://api.nasa.gov/planetary/apod?count={expression[0]}&api_key=JVbbhqTC3JJECdmFhLvlDl2cVfm9anqypt5qK3b5")
    elif len(expression) == 0:
        dict = requests.get(f"https://api.nasa.gov/planetary/apod?&api_key=JVbbhqTC3JJECdmFhLvlDl2cVfm9anqypt5qK3b5")
    else:
        dict = requests.get(f"https://api.nasa.gov/planetary/apod")

    if dict.status_code == 200 and expression != "":
        dict = json.loads(dict.content)
        if len(expression) == 0:
            if dict["explanation"].find(".") != -1:
                ponto = dict["explanation"].find(".")
                dict["explanation"] = dict["explanation"][:ponto + 1]
            embed = discord.Embed(
                title = "**Astronomy Picture of the Day**",
                description = f"```\n{dict['title']}\n```",
                color = 0x7B68EE,
            )
            embed.set_footer(text = "Data taken from " + "https://api.nasa.gov", icon_url = bot.user.avatar_url)

            embed.add_field(name = "Explanation", value = f"```\n{dict['explanation']}\n```", inline = False)

            if "jpg" in dict["url"] or "gif" in dict["url"]:
                embed.set_image(url = dict["url"])
            else:
                embed.add_field(name = "url_video", value = f"```\n{c['url']}\n```", inline = False)

            await ctx.send(embed=embed)

        else:
            count = 0
            for c in dict:
                count += 1
                if c["explanation"].find(".") != -1:
                    ponto = c["explanation"].find(".")
                    c["explanation"] = c["explanation"][:ponto + 1]
                embed = discord.Embed(
                    title = f"**Curiosity: {count}**",
                    description = f"```\n{c['title']}\n```",
                    color = 0x7B68EE,
                )
                embed.set_footer(text = "Data taken from " + "https://api.nasa.gov", icon_url = bot.user.avatar_url)

                embed.add_field(name = "Explanation", value = f"```\n{c['explanation']}\n```", inline = False)
                if "jpg" in c["url"] or "gif" in c["url"]:
                    embed.set_image(url = c["url"])
                else:
                    embed.add_field(name = "url_video", value = f"```\n{c['url']}\n```", inline = False)

                await ctx.send(embed=embed)

    else:
        embed = discord.Embed(
            title = "Error",
            description = "Invalid input value!!",
            color = 0xff0000,
        )
        embed.set_thumbnail(url = "https://c.tenor.com/bMm1uEq_VPYAAAAC/miia-sweating.gif")

        await ctx.send(embed=embed)

@bot.command(name="Asteroids")
async def Asteroids(ctx, *expression):
    expression = " ".join(expression)
    expression = expression.split()
    if len(expression) == 2:
        dict = requests.get(f"https://api.nasa.gov/neo/rest/v1/feed?start_date={expression[0]}&end_date={expression[1]}&api_key=JVbbhqTC3JJECdmFhLvlDl2cVfm9anqypt5qK3b5")
        expression = "/".join(expression)
    else:
        dict = requests.get(f"https://api.nasa.gov/neo/rest/v1/feed?start_date={''.join(expression)}&end_date={''.join(expression)}&api_key=JVbbhqTC3JJECdmFhLvlDl2cVfm9anqypt5qK3b5")
        expression = "".join(expression)

    if dict.status_code == 200 and expression != "":
        dict = json.loads(dict.content)
        embed = discord.Embed(
            title = "Near Earth Objects",
            description = f"```\nAsteroids based on their closest approach date ({expression}) to Earth.\n```",
            color = 0x7B68EE,
        )
        embed.set_author(name = bot.user.name, icon_url = bot.user.avatar_url)
        embed.set_footer(text = "Feito por " + "https://api.nasa.gov", icon_url = bot.user.avatar_url)

        for c in dict["near_earth_objects"]:
            for i in dict["near_earth_objects"][c]:
                embed.add_field(name = i["name"], value = f"Estimated diameter_min: ```\n{float(i['estimated_diameter']['meters']['estimated_diameter_min']):.2f} m\n``` Estimated diameter_max: ```\n{float(i['estimated_diameter']['meters']['estimated_diameter_max']):.2f} m\n``` Velocity: ```\n{float(i['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']):.2f} Km/h\n```", inline = False)


    else:
        embed = discord.Embed(
            title = "Error",
            description = "Invalid input value!!",
            color = 0xff0000,
        )
        if "error" in dict:
            embed.add_field(name = "Specified Error", value = f"{dict['message']}")

        embed.set_thumbnail(url = "https://c.tenor.com/bMm1uEq_VPYAAAAC/miia-sweating.gif")


    await ctx.send(embed=embed)

@bot.command(name="Location")
async def Location(ctx, *expression):
    expression = " ".join(expression)
    expression = expression.split()
    print(expression)
    if len(expression) == 3:
        request = requests.get(f"https://api.nasa.gov/planetary/earth/assets?lon={expression[0]}&lat={expression[1]}&date={expression[2]}&dim=0.15&api_key=JVbbhqTC3JJECdmFhLvlDl2cVfm9anqypt5qK3b5")
    else:
        request = requests.get("https://api.nasa.gov/planetary/earth/assets?lon={expression[0]}&lat={expression[1]}&date={expression[2]}&dim=0.15&api_key=JVbbhqTC3JJECdmFhLvlDl2cVfm9anqypt5qK3b5")

    try:
        dict = json.loads(request.content)
    except:
        pass

    if request.status_code == 200 and expression != "":
        embed = discord.Embed(
            title = "Location on earth",
            color = 0x7B68EE,
        )
        embed.set_author(name = bot.user.name, icon_url = bot.user.avatar_url)
        embed.set_footer(text = "Data taken from " + "https://api.nasa.gov", icon_url = bot.user.avatar_url)

        embed.add_field(name = "**\nLon:\n**", value = f"```\n{expression[0]}\n```")
        embed.add_field(name = "**\nLat:\n**", value = f"```\n{expression[1]}\n```")
        embed.add_field(name = "**\nDate:\n**", value = f"```\n{expression[2]}\n```")

        embed.set_image(url = dict["url"])
    else:
        embed = discord.Embed(
            title = "Error",
            description = "Invalid input Value!!",
            color = 0xff0000,
        )
        try:
            if "error" in dict:
                embed.add_field(name = "Specified Error", value = f"{dict['message']}")
            elif "imagery" in dict["msg"]:
                if len(expression) == 3:
                    embed.add_field(name = "Specified Error", value = dict["msg"] + f" ({expression[2]})")
        except:
            pass

        embed.set_thumbnail(url = "https://c.tenor.com/bMm1uEq_VPYAAAAC/miia-sweating.gif")

    await ctx.send(embed=embed)

@bot.command(name="Mars")
async def Mars(ctx, *expression):
    expression = " ".join(expression)
    expression = expression.split()
    if len(expression) == 3:
        request = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?&camera={expression[1]}&earth_date={expression[2]}&api_key=JVbbhqTC3JJECdmFhLvlDl2cVfm9anqypt5qK3b5")
    elif len(expression) == 2:
        request = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?&camera={expression[0]}&earth_date={expression[1]}&api_key=JVbbhqTC3JJECdmFhLvlDl2cVfm9anqypt5qK3b5")
    else:
        request = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?&earth_date=&api_key=DEMO_KEY")

    try:
        dict = json.loads(request.content)
    except:
        pass

    if request.status_code == 200 and expression != "" and dict["photos"] != []:
        embed = discord.Embed(
            title = "Mars Rover Photos",
            color = 0x7B68EE,
        )
        await ctx.send(embed=embed)

        count = 0
        page = 1

        if expression[0].isnumeric() == True:
            solicitações = expression[0]
        else:
            solicitações = 1

        while True:
            for c in dict["photos"]:
                count += 1
                embed = discord.Embed(
                    title = f"Photo: {count}",
                    color = 0x7B68EE,
                )

                embed.set_footer(text = "Data taken from " + "https://api.nasa.gov", icon_url = bot.user.avatar_url)
                embed.set_image(url = c["img_src"])

                await ctx.send(embed=embed)


                if count == int(solicitações):
                    break


            if count == int(solicitações):
                break

            page += 1
            dict = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?&page={page}&camera={expression[1]}&earth_date={expression[2]}&api_key=JVbbhqTC3JJECdmFhLvlDl2cVfm9anqypt5qK3b5")
            dict = json.loads(dict.content)

            if dict["photos"] == []:
                embed = discord.Embed(
                    title = "You have reached the limit of fotos available for this camera and date"
                )
                embed.set_thumbnail(url = "https://i.pinimg.com/564x/d2/dd/23/d2dd239786847c20c01081a9a1f2b66b.jpg")

                await ctx.send(embed=embed)

                break

    else:
        embed = discord.Embed(
            title = "Error",
            description = "Invalid input value!!",
            color = 0xff0000,
        )
        try:
            if "error" in dict:
                embed.add_field(name = "Specified Error", value = f"{dict['message']}")
            elif dict["photos"] == []:
                if len(expression) == 3 or len(expression) == 2:
                    embed.add_field(name = "Specified Error", value = "There is no photo for the specific camera and date.")
        except:
            pass

        embed.set_thumbnail(url = "https://c.tenor.com/bMm1uEq_VPYAAAAC/miia-sweating.gif")

        await ctx.send(embed=embed)

@bot.command(name="Search")
async def search(ctx, *expression):
    expression = " ".join(expression)
    expression =  expression.split()
    if expression != []:
        if expression[0].isnumeric() == True:
            search = " ".join(expression[1:])
        else:
            search = " ".join(expression[0:])

    if len(expression) >= 1:
        request = requests.get(f"https://images-api.nasa.gov/search?title={search}")
    else:
        request = requests.get("https://images-api.nasa.gov/search?")

    try:
        dict = json.loads(request.content)
    except:
        pass

    if request.status_code == 200 and expression != [] and dict["collection"]["items"] != []:
        count = 0
        page = 1

        if expression[0].isnumeric() == True:
            solicitações = expression[0]
        else:
            solicitações = 1

        while True:
            for c in dict["collection"]["items"]:
                count += 1
                if len(c["data"][0]["description"]) < 1000:

                    if c["data"][0]["description"].find(".") != -1:
                        ponto = c["data"][0]["description"].find(".")
                        c["data"][0]["description"] = c["data"][0]["description"][:ponto + 1]
                    if c["data"][0]["title"].find(".") != -1:
                        ponto = c["data"][0]["title"].find(".")
                        c["data"][0]["title"] = c["data"][0]["title"][:ponto + 1]

                    embed = discord.Embed(
                        title = c["data"][0]["title"],
                        description = f"```\n{c['data'][0]['description']}\n```",
                        color = 0x7B68EE,
                    )
                    embed.set_footer(text = "Data taken from " + "https://api.nasa.gov", icon_url = bot.user.avatar_url)

                    embed.set_image(url = c["links"][0]["href"])
                    await ctx.send(embed=embed)

                    if int(solicitações) == count:
                        break
                else:
                    count -= 1

            if int(solicitações) == count:
                    break

            page += 1
            dict = requests.get(f"https://images-api.nasa.gov/search?title={search}&page={page}")
            dict = json.loads(dict.content)

            if dict["collection"]["items"] == []:
                embed = discord.Embed(
                    title = "You have reached the limit of items for this search."
                )
                embed.set_thumbnail(url = "https://i.pinimg.com/564x/d2/dd/23/d2dd239786847c20c01081a9a1f2b66b.jpg")

                await ctx.send(embed=embed)

                break

    else:
        embed = discord.Embed(
            title = "Error",
            description = "Invalid input value!!",
            color = 0xff0000,
        )
        try:
            if "error" in dict:
                embed.add_field(name = "Specified Error", value = f"{dict['message']}")
            elif dict["collection"]["items"] == [] and expression != []:
                if len(expression) >= 1:
                    embed.add_field(name = "Specified Error", value = "There is no data for this search.")
        except:
            pass

        embed.set_thumbnail(url = "https://c.tenor.com/bMm1uEq_VPYAAAAC/miia-sweating.gif")

        await ctx.send(embed=embed)

@bot.command(name="Info")
async def Info(ctx, *expression):
    expression = " ".join(expression)
    expression = expression.split()
    if expression == []:
        embed = discord.Embed(
            title = "**Info**",
            description = "```\nRemember that you can only make 1000 requests per hour.\n```",
            color = 0x7B68EE,
        )
        embed.set_author(name = bot.user.name, icon_url = bot.user.avatar_url)
        embed.set_footer(text = "Data taken from " + "https://api.nasa.gov", icon_url = bot.user.avatar_url)

        embed.set_thumbnail(url = "https://i.kym-cdn.com/photos/images/newsfeed/001/338/454/f61.png")

        embed.add_field(name="&Apod", value = "```\n&Apod = Astronomy Picture of the Day.\n``` ```\n&Apod {integer} = Returns a number of random curiosities that will be selected according to the number placed.\n```", inline = False)
        embed.add_field(name="&Asteroids", value = "```\n&Asteroids {YYYY-MM-DD} = Returns asteroids based on their closest approach date to Earth.\n```", inline = False)
        embed.add_field(name="&Location", value = "```\n&Location {longitude} {latitude} {YYYY-MM-DD} = Returns a satellite image based on its longitude, latitude, and creation date.```\n", inline = False)
        embed.add_field(name="&Mars", value = """```\nCamera types = {fhaz: Front Hazard Avoidance Camera; rhaz: Rear Hazard Avoidance Camera; mast: Mast Camera; chemcam: Chemistry and Camera Complex; mahli: Mars Hand Lens Imager; mardi: Mars Descent Imager; navcam: Navigation Camera; pancam: Panoramic Camera; minites: Miniature Thermal Emission Spectrometer (Mini-TES)}.\n```
        ```\n&Mars {integer} {camera abreviation name} {YYYY-MM-DD} = Returns a number of photos based on the number entered (if no integer is entered, only one photo will be returned), your camera type, and your creation date.\n```""", inline = False)
        embed.add_field(name="&Search", value = "```\n&Search {integer} {search} = Returns search results in the NASA database based on the number entered (if no integer is entered, only one search will be returned) and the words entered related to the titles of the searches.```\n", inline = False)

    else:
        embed = discord.Embed(
            title = "Error",
            description = "This command don't accept any input!",
            color = 0xff0000,
        )

        embed.set_thumbnail(url = "https://c.tenor.com/bMm1uEq_VPYAAAAC/miia-sweating.gif")


    await ctx.send(embed=embed)




bot.run("{token}")
