from flask import Flask, render_template
import requests
import json
import time
from cuttpy import Cuttpy
from urllib.parse import urlparse
import datetime

def decdeg2dms(dd):
    mnt,sec = divmod(dd*3600,60)
    deg,mnt = divmod(mnt,60)
    return str(deg),str(mnt),str(sec)

app = Flask(__name__)

@app.route('/redo')
def redo():
    response = requests.get('https://monolithtracker.com/json-export')
    data = response.json()

    response = requests.get('https://monolithtracker.com/json-export-scaled-images')
    imagedata = response.json()

    shortener = Cuttpy("18bd1d3e0bbe131f91f5c5e1d38cb47927ba5")

    global content
    content = []

    for number in range(0,len(data)):

        t0= time.time()

        name = data[number]["title"][0]["value"]
        print("["+str(number)+"/"+str(len(data))+"]"+"-"+str(name))
	      # ^ This line prints each monolith's name and progress through the program, so it's a nice little status checker
	
        image = ("https://www.monolithtracker.com"+imagedata[number]["600x400"].split(",")[0])
    	  # image = data[number]["field_monolith_image"][0]["url"] <-- This is legacy imaging

        t1 = round(time.time() - t0,2)
        print("          Name/Image: ", t1)
        t0= time.time()

        monolithurl = "https://monolithtracker.com/node/"+str(data[number]["nid"][0]["value"])+"?mtm_campaign=exportpdf"
        monolithshorturl = str(shortener.shorten(monolithurl+"&mtm_kwd=short-url").shortened_url)
        monolithshorturlqr = str(shortener.shorten(monolithurl+"&mtm_kwd=qr").shortened_url)

        t1 = round(time.time() - t0,2)
        print("          urls: ", t1)
        t0= time.time()

        if len(data[number]["field_location_accuracy"]) == 1:
            accuracy = data[number]["field_location_accuracy"][0]["value"]
        else:
            accuracy = "No Data"

        if len(data[number]["field_spotted_date"]) == 1:
            spotteddate = data[number]["field_spotted_date"][0]["value"]
        else:
            spotteddate = "No Data"

        if len(data[number]["field_disappearance_date"]) == 1:
            gonedate = data[number]["field_disappearance_date"][0]["value"]
        else:
            gonedate = "Hasn't Disappeared Yet"

        if len(data[number]["field_monolith_classification"]) == 1:
            classification = data[number]["field_monolith_classification"][0]["value"]
        else:
            classification = "No Data"

        if len(data[number]["field_material"]) == 1:
            material = data[number]["field_material"][0]["value"]
        else:
            material = "No Data"

        if len(data[number]["field_height"]) == 1:
            height = data[number]["field_height"][0]["value"]
        else:
            height = "No Data"

        if len(data[number]["body"]) == 1:
            body = data[number]["body"][0]["value"]
        else:
            body = ("No Data")

        t1 = round(time.time() - t0,2)
        print("          location/spotted/dissapeared/class/material/height/body: ", t1)
        t0= time.time()

        if len(data[number]["field_texture"]) > 1:
            textures=[]
            for texture in data[number]["field_texture"]:
                textures.append(texture["value"])
            textures = " / ".join(textures)
        else:
            texture = ("No Data")
        
        t1 = round(time.time() - t0,2)
        print("          textures: ", t1)
        t0= time.time()

        if len(data[number]["field_top_geometry"]) > 1:
            top_geometry=[]
            for geometry in data[number]["field_top_geometry"]:
                top_geometry.append(geometry["value"])
            top_geometry = " / ".join(top_geometry)
        else:
            top_geometry = ("No Data")

        t1 = round(time.time() - t0,2)
        print("          topgeo : topgeo", t1)
        t0= time.time()

        if len(data[number]["field_construction"]) > 1:
            constructions=[]
            for construction in data[number]["field_construction"]:
                constructions.append(construction["value"])
                construction = " / ".join(constructions)
        else:
            construction = ("No Data")

        t1 = round(time.time() - t0,2)
        print("          constr: ", t1)
        t0= time.time()

        if len(data[number]["field_notes"]) == 1:
            notes = (data[number]["field_notes"][0]["value"])
        else:
            notes = ("No Notes have been written.")
        
        t1 = round(time.time() - t0,2)
        print("          notes: ", t1)
        t0= time.time()

        if len(data[number]["field_text_symbols"]) == 1:
            text_symbols = (data[number]["field_text_symbols"][0]["value"])

        if len(data[number]["field_text_symbols"]) > 1:
            symbols=[]
            for symbol in data[number]["field_text_symbols"]:
                symbols.append(symbol["value"])
                text_symbols = " / ".join(symbols)
        else:
            text_symbols = ("No Data")
        
        t1 = round(time.time() - t0,2)
        print("          text-symbols: ", t1)
        t0= time.time()

        latlon = (data[number]["field_location"][0]["latlon"])
        lattitude = (data[number]["field_location"][0]["lat"])
        longitude = (data[number]["field_location"][0]["lon"])

        articles = []
        for article in data[number]["field_articles_media"]:
            url = urlparse(str(article["uri"])).geturl()
            
            response = shortener.shorten(url)
            
            if (response.code) == 7:
                articles.append(str(article["title"])+" - "+str(response.shortened_url))
                
            else:
                articles.append(str(article["title"])+" - "+"Error "+str(response.code)+" : This URL Wouldn't Shorten") 
        
        print(articles)

        t1 = round(time.time() - t0,2)
        print("          articles: ", t1)
        t0= time.time()      

        geohack = ("""https://geohack.toolforge.org/geohack.php?params="""+decdeg2dms(lattitude)[0]+"""_"""+decdeg2dms(lattitude)[1]+"""_"""+decdeg2dms(lattitude)[2]+"""_N_"""+decdeg2dms(longitude)[0]+"""_"""+decdeg2dms(longitude)[1]+"""_"""+decdeg2dms(longitude)[2]+"""_E""")
        shortgeohack = shortener.shorten(geohack).shortened_url

        t1 = round(time.time() - t0,2)
        print("          coords: ", t1)
        t0= time.time()

        content.append({"name" : str(name),
                        "image" : str(image),
                        "monolithshorturl" : str(monolithshorturl),
                        "monolithshorturlqr" : str(monolithshorturlqr),
                        "accuracy" : str(accuracy),
                        "spotteddate" : str(spotteddate),
                        "gonedate" : str(gonedate),
                        "classification" : str(classification),
                        "material" : str(material),
                        "height" : str(height),
                        "body" : str(body),
                        "texture": str(texture),
                        "top_geometry" : str(top_geometry),
                        "construction" : str(construction),
                        "notes" : str(notes),
                        "text_symbols" : str(text_symbols),
                        "lattitude" : str(lattitude),
                        "longitude" : str(longitude),
                        "articles" : articles,
                        "shortgeohack"  : str(shortgeohack)
                    })

        t1 = round(time.time() - t0,2)
        print("          packaging: ", t1)                

    global lendata
    lendata = str(len(data))

    global timestamp
    timestamp = ('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))

    return("200")

@app.route('/')
def index():
  if not 'content' in globals():
    return("data uncollected")
  else:
    return(render_template('output.html',content=content,lendata=lendata, timestamp=timestamp))


app.run(debug=True, host='0.0.0.0')
