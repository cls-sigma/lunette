from bs4 import BeautifulSoup
import requests
import unidecode
import googlemaps
from googlemaps import convert
import json
from urllib.request import urlopen
from datetime import datetime, timedelta
key="AIzaSyAVr_nuK2dm72cMIgc_ga5yAM1zRYXMnr0"
client=googlemaps.Client(key)
def position2():
    doi_link = 'https://www.google.com/maps'  # https://doi.org/10.1016/j.artint.2018.07.007'
    response = requests.get(url=doi_link, allow_redirects=True)
    # use final response
    # parse html and get final redirect url
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    url = soup.findAll("meta")
    # print("voila url: ", url)
    link = ""
    for i in url:

        if "http" in i['content']:
            # print("lien: ", link)
            link = i['content']
            print(link)
            break
    lien = link
    
    if lien:
        lien = lien.split('?')
        lien = lien[1].split("=")[1].split("%2C")
        lat = lien[0]
        long = lien[1].split("&")[0]
        # print(lat, long)
        reverse_geocode_result = client.reverse_geocode((float(lat), float(long)))
        fin = f"Vous etes actuellement à {reverse_geocode_result[0]['formatted_address']}"  # (float(res['loc'].split(',')[0]), float(res['loc'].split(',')[-1])))
        print(fin)  # , client.geocode(str(reverse_geocode_result)))
        return f'{lien[0]},{lien[1].split("&")[0]}'
    else:
        return ""


def position1():
    url = "http://ipinfo.io/json"
    tes = urlopen(url)
    res = json.load(tes)
    #reverse_geocode_result = client.reverse_geocode((6.1734912,1.1763712))#(float(res['loc'].split(',')[0]), float(res['loc'].split(',')[-1])))
    #print("adresse ip: ", client.geocode(str(reverse_geocode_result)))
    #print("Mon adresse:", reverse_geocode_result[0]["formatted_address"])
    return float(res['loc'].split(',')[0]), float(res['loc'].split(',')[-1])

def position():
    url = "http://ipinfo.io/json"
    tes = urlopen(url)
    res = json.load(tes)
    lat=float(res['loc'].split(',')[0])
    long=float(res['loc'].split(',')[-1])
    reverse_geocode_result = client.reverse_geocode((lat, long))#(float(res['loc'].split(',')[0]), float(res['loc'].split(',')[-1])))
    print("adresse ip: ", client.geocode(str(reverse_geocode_result)))
    t="Votre adresse actuel:"+ reverse_geocode_result[0]["formatted_address"]
    return t

def text_clean(t):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(t, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.get_text()
    return text
def directions( destination,actuel="non",
                waypoints=None, alternatives=False, avoid=None,
               language=None, units=None, region=None, departure_time=None,
               arrival_time=None, optimize_waypoints=False, transit_mode=None,
               transit_routing_preference=None, traffic_model=None, client=client, mode="walking"):
    
    #origin = "universite de lome"
    destination=unidecode.unidecode(destination)
    destination=destination.title()
    print("destl ", destination)
    #origin = position1()    #origin=convert.latlng(origin)
    #origin=f"{origin[0]},{origin[1]}"
    origin = position2()
    print(origin)
    l11=[ "localisation", "localise", "trouve", "trouve-moi","où",
              "où se trouve","localise-moi", "localises-moi"]
    for i in l11:
        destination=destination.replace(i, "")
    destination=destination.replace('moi', '').replace("é", "e")
    print("dest:", destination)
    params = {
        "origin": origin, # convert.latlng(origin),
        "destination": destination.replace(' ', '+') #convert.latlng(destination)#
    }

    if mode:
        # NOTE(broady): the mode parameter is not validated by the Maps API
        # server. Check here to prevent silent failures.
        if mode not in ["driving", "walking", "bicycling", "transit"]:
            raise ValueError("Invalid travel mode.")
        params["mode"] = mode

    if waypoints:
        waypoints = convert.location_list(waypoints)
        if optimize_waypoints:
            waypoints = "optimize:true|" + waypoints
        params["waypoints"] = waypoints

    if alternatives:
        params["alternatives"] = "true"

    if avoid:
        params["avoid"] = convert.join_list("|", avoid)

    if language:
        params["language"] = language

    if units:
        params["units"] = units

    if region:
        params["region"] = region

    if departure_time:
        params["departure_time"] = convert.time(departure_time)

    if arrival_time:
        params["arrival_time"] = convert.time(arrival_time)

    if departure_time and arrival_time:
        raise ValueError("Should not specify both departure_time and"
                         "arrival_time.")

    if transit_mode:
        params["transit_mode"] = convert.join_list("|", transit_mode)

    if transit_routing_preference:
        params["transit_routing_preference"] = transit_routing_preference

    if traffic_model:
        params["traffic_model"] = traffic_model
    # di=client._request("/maps/api/directions/json", params).get("routes", [])
    import urllib.request
    import json
    complete=""
    print(params)
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    for cle, val in params.items():
        print(cle, val)
        complete+=f"{cle}={val.replace(' ', '+')}&"
    complete+=f"key={key}"
    place_request=endpoint+complete
    print(place_request)
    try:
        response = urllib.request.urlopen(place_request).read()
        chemin = json.loads(response)
        di= chemin["routes"]
        print(di)
        l11=[ "localisation", "localise", "trouve", "trouve-moi","où","localise moi", "moi",
              "où se trouve","localise-moi", "localises-moi"]
        desi=destination.lower()
        for i in l11:
            desi=desi.replace(i, "")
            #print(len(di), type(di), di[0].keys())
        text=f"Informations sur votre trajet de chez vous à {desi}, {di[0]['legs'][0]['end_address']} : "
        text+=f"Distance estimé à {di[0]['legs'][0]['distance']['text']}, Durée du trajet estimé à {di[0]['legs'][0]['duration']['text']}" \
              f" Les differentes tournures: "
        '''print(di[0]["legs"][0]["traffic_speed_entry"])
        print(di[0]["legs"][0]["via_waypoint"])
        print(di[0]["legs"][0]["steps"][0].keys())
        print(di[0]["legs"][0]["steps"][0]["html_instructions"])
        print(di[0]["legs"][0]["steps"][0]["travel_mode"])'''
        j=0
        #print(di[0]["legs"][0]["steps"])
        for i in di[0]["legs"][0]["steps"]:
            #print("voila i: , ", i)
            j+=1
            if actuel=="oui":
                try:
                    text += f"Vous marchez {i['distance']['text']}, estimé à environ {i['duration']['text']},  {text_clean(i['html_instructions'])}, "#, {traduct(i['maneuver'])} "  # , "
                except:
                    text += f"Vous marchez {i['distance']['text']}, estimé à environ {i['duration']['text']},  {text_clean(i['html_instructions'])} "
                break

            if j==1:
                text += f" \n 1ere partie: "
            else:
                text += f" \n {j}eme partie: "

            try:
                text+= f"Vous marchez {i['distance']['text']}, estimé à environ {i['duration']['text']},  {text_clean(i['html_instructions'])}, ",# {traduct(i['maneuver'] )} "#, "
            except:
                text+= f"Vous marchez {i['distance']['text']}, estimé à environ {i['duration']['text']},  {text_clean(i['html_instructions'])} "
        #text=text.replace("onto", "sur la").replace("min", "minutes").replace(" h ", "heures")
        text=text.replace("sortieVotre", "sortie; Votre")
        text=text.replace("onto", "sur la").replace(" min ", " minutes ").replace(' 1 ', ' une ')
    except:
        text=position()+", Je ne trouve pas l'endroit, veuillez reessayer en présisant l'adresse"
    return text




 #print(position2())
#print(position1())
#print(directions(destination="localise moi le Port Autonome de Lome", language="fr"))