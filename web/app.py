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

@app.route('/')
def index():
	return(render_template('output.html'))

@app.route('/redo')
def redo():
    response = requests.get('https://monolithtracker.com/json-export')
    data = response.json()

    shortener = Cuttpy("18bd1d3e0bbe131f91f5c5e1d38cb47927ba5")

    f = open("templates/output.html","w", encoding="utf8")

    initialisationhtml = """<!DOCTYPE html>
                            <head>
                            <!-- Boostrap CDN -->
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
                            <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
                            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>


                            <style>
                                    html,body{
                                        width:210mm;
                                    }
                                    .main {
                                        margin-left:10mm;
                                        margin-right:10mm;
                                        padding-top:5mm;
                                    }
                            </style>

                            </head>

                            <body>
                                <div class="main">
                                    <br>
                                    <h1 style="text-align: center;"><img src="https://monolithtracker.com/sites/default/files/favicon-32x32.png"> &nbsp Monolith Tracker Export PDF &nbsp <img src="https://monolithtracker.com/sites/default/files/favicon-32x32.png"></h1>
                                    <hr>

                                    <h5>Note</h5>
                                    <p>
                                        <b>
                                            
                                            This export was written using Python and the MonolithTracker.com API.
                                        </b>
                                    </p>

                                    <br>

                                    <div class="row">
                                        <div class="col-sm-6">
                                        <div class="card">
                                            <div class="card-body">
                                            <h5 class="card-title">Currently</h5>
                                            <p class="card-text"><b>This document contains """+str(len(data))+""" Monoliths!</b></p>
                                            </div>
                                        </div>
                                        </div>
                                    </div>

                                    <br>

                                    <h5>Welcome</h5>
                                    <p><i>Welcome to Monolith Tracker, a site where we are trying to track and categorize all of the monoliths. Anyone can contribute and update or add monoliths. This website and it's dataset is user contributed, by users like yourself. We encourage you to edit any of the existing monoliths, adding new sources, new details, sources, or notes. Additionally, we encourage you to help us find these monoliths, by reporting any monoliths not on the map. Thank you!

                                        We have just launched a discord server. If you want to help us with this project, joining the Monolith Tracker Discord is a great place to start.</i></p>
                                    
                                    <br>
                                    
                                    <h5>An Introduction</h5><h6>By u/Walkyou</h6>
                                    <p><i>On November 18th 2020, a group of Utah DWR Biologists were flying in Southwest Utah on an assignment to count Bighorn Sheep in the area. What they saw next kickstarted possibly the most ‘2020’ news story the world has ever seen. A large metal monolith, approximately 9.8 feet tall, was standing in the middle of the desert, miles from the nearest town of Moab, Utah.
                                    </i></p><p><i>
                                        The Biologists published a video of the monolith on November 23rd, and the story instantly went viral. National news companies caught wind of it and the monolith became somewhat of a meme, but also a hell of a mystery.
                                    </i></p><p><i>
                                        Within days, the location of the monolith was discovered by Reddit users, and Google Earth imagery had determined that it was placed sometime in 2016. People naturally flocked to the site over the course of the next few days, taking pictures, videos, investigating, or just marveling and the mystery of the monolith. Who put it there? Why? Was it the government, or even aliens? The world was captivated, and the investigation had no sign of stopping. Until, of course, it vanished.
                                    </i></p><p><i>
                                        On November 27th, a group of 4 slackliners removed the monolith. They took responsibility for the removal a few days later, resulting in mixed reactions from the public. On the one hand, the land would not be ravaged by tourists who were making a mess of it. On the other, the monolith would not be able to be studied or investigated any further. Regardless of what anyone thought though, the mystery came to an unsatisfying close.
                                    </i></p><p><i>
                                        Until there was another. The same day that the Utah Monolith was removed, a second monolith was discovered in eastern Romania. This monolith had odd squiggles on one side, and was generally much less well-made than the Utah Monolith. Some believed that it was made as a knockoff, others believed that it was the second clue in the larger Monolith mystery. But then, on December 1st, this monolith vanished just like its predecessor. Maybe this was truly the end.
                                    </i></p><p><i> 
                                        The next day there was a third. This time in California. The day after that, it too was destroyed. This time, it was a group of a far right “activists”, who forcefully removed it ‘in the name of christ’. Everyone knew what was coming though. A 4th monolith appeared in Las Vegas, in the middle of the extremely popular and crowded Fremont Street. Then, a 5th in Joshua Tree National Park, California. They kept appearing. There have been 19 total monoliths, plus an additional 5 confirmed fakes, and they are seemingly growing exponentially. Are they all connected? Which ones are real, which are simply knockoffs? This mystery is far from over. With the way that 2020 has been going, it is likely just beginning.</i></p>
                                    </i></p>

                                    <h5>Links</h5>
                                    <div class="container">
                                        <div class="row">
                                        <div class="col">
                                            <img style="float: right;" src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://cutt.ly/nh7n6jZ">
                                        </div>
                                        <div class="col">
                                            Main Page. <br>
                                            Also Avaliable at: <br>
                                            <b>https://cutt.ly/nh7n6jZ </b>
                                        </div>
                                        </div>
                                        </div>
                                    
                                    <hr>
                                    <img src="https://licensebuttons.net/l/by/4.0/80x15.png">
                                    <p>Written work is licensed under a Creative Commons Attribution 4.0 International License.<br>"""+('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))+"""GMT</p>
                                </div>
                                <p style="page-break-before: always">
                                """

    f.write(initialisationhtml)

    for number in range(0,len(data)):
        name = data[number]["title"][0]["value"]
        #print("["+str(number)+"/"+str(len(data))+"]"+"-"+str(name))
        image = data[number]["field_monolith_image"][0]["url"]
        monolithurl = "https://monolithtracker.com/node/"+str(data[number]["nid"][0]["value"])+"?mtm_campaign=exportpdf"
        monolithshorturl = str(shortener.shorten(monolithurl+"&mtm_kwd=short-url").shortened_url)
        monolithshorturlqr = str(shortener.shorten(monolithurl+"&mtm_kwd=qr").shortened_url)

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

        if len(data[number]["field_texture"]) > 1:
            textures=[]
            for texture in data[number]["field_texture"]:
                textures.append(texture["value"])
            textures = " / ".join(textures)
        else:
            texture = ("No Data")

        if len(data[number]["field_top_geometry"]) > 1:
            top_geometry=[]
            for geometry in data[number]["field_top_geometry"]:
                top_geometry.append(geometry["value"])
            top_geometry = " / ".join(top_geometry)
        else:
            top_geometry = ("No Data")

        if len(data[number]["field_construction"]) > 1:
            constructions=[]
            for construction in data[number]["field_construction"]:
                constructions.append(construction["value"])
                construction = " / ".join(constructions)
        else:
            construction = ("No Data")

        if len(data[number]["field_notes"]) == 1:
            notes = (data[number]["field_notes"][0]["value"])
        else:
            notes = ("No Notes have been written.")

        if len(data[number]["field_text_symbols"]) == 1:
            text_symbols = (data[number]["field_text_symbols"][0]["value"])

        if len(data[number]["field_text_symbols"]) > 1:
            symbols=[]
            for symbol in data[number]["field_text_symbols"]:
                symbols.append(symbol["value"])
                text_symbols = " / ".join(symbols)
        else:
            text_symbols = ("No Data")

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
                articles.append(str(article["title"])+" - "+str(("Error ",response.code," : This URL Wouldn't Shorten :",url)))       

        geohack = ("""https://geohack.toolforge.org/geohack.php?params="""+decdeg2dms(lattitude)[0]+"""_"""+decdeg2dms(lattitude)[1]+"""_"""+decdeg2dms(lattitude)[2]+"""_N_"""+decdeg2dms(longitude)[0]+"""_"""+decdeg2dms(longitude)[1]+"""_"""+decdeg2dms(longitude)[2]+"""_E""")
        shortgeohack = shortener.shorten(geohack).shortened_url

        content =           """
                                    <div class="main">
                                        <hr>
                                        <h2>"""+str(name)+"""</h2>

                                        <br>

                                        <div class="container">
                                            <div class="row">
                                                <div class="col-8">
                                                    <img src=\""""+str(image)+"""\" style="object-fit:cover;width:100%;height:470px">
                                                </div>
                                                <div class="col-4">
                                                    <h6><b>Spotted</b>&nbsp """+str(spotteddate)+"""</h6>
                                                    <h6><b>Disappeared</b>&nbsp """+str(gonedate)+""" </h6>
                                                    <hr>
                                                    <h6><b>Classification</b>&nbsp """+str(classification)+"""</h6>
                                                    <hr>
                                                    <h6><b>Material</b>&nbsp """+str(material)+"""</h6>
                                                    <h6><b>Height</b>&nbsp """+str(height)+"""</h6>
                                                    <h6><b>Texture</b>&nbsp """+str(texture)+"""</h6>
                                                    <h6><b>Top Geometry</b>&nbsp """+str(top_geometry)+"""</h6>
                                                    <h6><b>Construction</b>&nbsp """+str(construction)+"""</h6>
                                                    <h6><b>Text Symbols</b>&nbsp """+str(text_symbols)+"""</h6>
                                                    <hr>
                                                    <h6><b>Lattitude</b>&nbsp """+str(lattitude)+"""</h6>
                                                    <h6><b>Longitude</b>&nbsp """+str(longitude)+"""</h6>
                                                    <h6><b>Accuracy</b>&nbsp """+str(accuracy)+"""</h6>
                                                    <hr>
                                                    <h6><b>URL</b>&nbsp """+str(monolithshorturl)+"""</h6>

                                                </div>
                                            </div>
                                        </div>

                                        <br>
                                        
                                        <h5>Body</h5>
                                        <p>"""+str(body)+"""</p>


                                        <h5>Notes</h5>
                                        <p><i>"""+str(notes)+"""</i></p>


                                        <h5>Articles</h5>
                                        <p>
                                            """+str(' <br> '.join(articles))+"""
                                        </p>

                                        <h5>Map</h5>
                                        <br>
                                        
                                        
                                        <div class="container">
                                            <div class="row">
                                                <div class="col-8">
                                                    <img width=100% style="object-fit:contain;margin-bottom: 10px;" src="https://api.mapbox.com/styles/v1/mapbox/light-v10/static/pin-s-l+000("""+str(longitude)+""","""+str(lattitude)+""")/"""+str(longitude)+""","""+str(lattitude)+""",3/1000x600?access_token=pk.eyJ1IjoiZHlsYW5rMTIzIiwiYSI6ImNrajUwMm55NzV0NWwyc2xiNzk0OHFjdXoifQ.cIzWvi9HlI1YfhpY24KbTA" >
                                                </div>
                                                <div class="col-4">
                                                    <p>Geohack:</p>
                                                    <img width="90px" src="http://api.qrserver.com/v1/create-qr-code/?data="""+shortgeohack+"""&size=200x200">
                                                    <hr>
                                                    <p>Monolith Tracker:</p>
                                                    <img width="90px" src="http://api.qrserver.com/v1/create-qr-code/?data="""+monolithshorturlqr+"""&size=200x200">
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                <p style="page-break-before: always">
                                    """

        f.write(content)

    finishhtml = """</body>"""   
    f.write(finishhtml)    
    f.close()
    return("200")


app.run(debug=True, host='0.0.0.0')
