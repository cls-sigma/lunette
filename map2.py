import json
from urllib.request import urlopen
from datetime import datetime, timedelta

import wolframalpha
from googlesearch import search
import googlemaps
import requests
from bs4 import BeautifulSoup
from googlemaps import convert
from googletrans import Translator

from googleapiclient.discovery import build
#Printable pour telecharger les fichers dejà existants

trans=Translator()

def traduct(text):
    return trans.translate(text, dest="fr").text
import os
key="AIzaSyAVr_nuK2dm72cMIgc_ga5yAM1zRYXMnr0"

client=googlemaps.Client(key)

#print(dir(client))

my_api_key = "AIzaSyA5B_zTVX7ktACpwWf5dN9BkPW1bk161P0"
my_cse_id = "47d81914f1b5b4b02"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def gsearch(p):
    # to search
    e = ""
    text=''
    se=search(p)
    print("reponse", se)
    r=0
    for j in se: #,  stop=10, pause=2):
        try:
            print(j)
            response = requests.get(j)
            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find('body').find_all('p')
            #print(headlines)
            for x in headlines:
                e += x.text.strip() + ". \n "
            if e:
                r+=1
                print("voila e: ",e.split('.'))
                text+=" ".join(e.split('.')[:5])
                
            #e=e.splitlines()
            text=traduct(text)
            
            ''' 
            e=traduct(e)
            print("debut e:", e, "fin e" '''
        except:
            pass
        if r==1:
            #if e:
            break
    if not text:
        text="Je n'ai pas pu trouvé d'information à propos de votre requète. Vous pouvez réessayer tout en assurant que les informations de votre demande sont correctes. Merci"
    
    print("Le texte:  ",text)
    return text

import vlc
from talk import talk
def radio(command):
    url="http://vis.media-ice.musicradio.com/Capital"
    if "londre" in command:
        url="http://vis.media-ice.musicradio.com/Capital"
    
    if globals().get('player'):
        instance = globals()['instance']
        player = globals()['player']
    else:
        instance = globals()['instance'] = vlc.Instance("--no-video")
        player = globals()['player'] = instance.media_player_new()    

    
    lr=["arrête-moi", "arrête", "stop"]
    instance = vlc.get_default_instance()
    
    for j in lr:
        if j in command:
            print("yes")
            print('1')
            player.stop()
            print('2')
            # and possibly garbage collect the player
            del globals()['player']
            del globals()['instance']
            return
    if command:
        talk("Recherche de la radio en cours")
        #url="http://vis.media-ice.musicradio.com/Capital"
        media = instance.media_new(url)
        media.get_mrl()
        player.set_media(media)

        player.play()
        return

#radio("radio lome")
#gsearch("Qui est SEKPONA Kokou Sitsopé ?")
def myadress():
    url = "http://ipinfo.io/json"
    tes = urlopen(url)
    res = json.load(tes)

    return float(res['loc'].split(',')[0]), float(res['loc'].split(',')[-1])

def myadress():
    doi_link  = 'https://www.google.com/maps'#https://doi.org/10.1016/j.artint.2018.07.007'
    response = requests.get(url= doi_link ,allow_redirects=True )
    
    # use final response
    # parse html and get final redirect url
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)
    url = soup.findAll("meta")
    #print("voila url: ", url)
    link=""
    for i in url:
    
        if "http" in i['content']:
            #print("lien: ", link)
            link=i['content']
            break
    lien=link
    if lien:
        lien=lien.split('?')
        lien=lien[1].split("=")[1].split("%2C")
        lat=lien[0]
        long=lien[1].split("&")[0]
        print(lat, long)
        #reverse_geocode_result = client.reverse_geocode((float(lat),float(long)))#(float(res['loc'].split(',')[0]), float(res['loc'].split(',')[-1])))
        #print("adresse ip: ",reverse_geocode_result[0]["formatted_address"])#, client.geocode(str(reverse_geocode_result)))
        return lat, long
    else:
        return "Je n'ai pas pu vous localiser"

def position():
    doi_link  = 'https://www.google.com/maps'#https://doi.org/10.1016/j.artint.2018.07.007'
    response = requests.get(url= doi_link ,allow_redirects=True )
    
    # use final response
    # parse html and get final redirect url
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)
    url = soup.findAll("meta")
    #print("voila url: ", url)
    link=""
    for i in url:
    
        if "http" in i['content']:
            #print("lien: ", link)
            link=i['content']
            break
    lien=link
    if lien:
        lien=lien.split('?')
        lien=lien[1].split("=")[1].split("%2C")
        lat=lien[0]
        long=lien[1].split("&")[0]
        #print(lat, long)
        reverse_geocode_result = client.reverse_geocode((float(lat),float(long)))
        fin=f"Vous etes actuellement à {reverse_geocode_result[0]['formatted_address']}"#(float(res['loc'].split(',')[0]), float(res['loc'].split(',')[-1])))
        print(fin)#, client.geocode(str(reverse_geocode_result)))
        return fin
    else:
        return "Je n'ai pas pu vous localiser"

'''from selenium import webdriver
driver=webdriver.Firefox()
def position():
    driver.get("https://www.google.com/maps")
    get_url = driver.current_url
    print("The current url is:" + str(get_url))
    driver.quit()
    reverse_geocode_result = client.reverse_geocode((6.1734912, 1.1763712))  # (float(res['loc'].split(',')[0]), float(res['loc'].split(',')[-1])))
    print("adresse ip: ", client.geocode(str(reverse_geocode_result)))
    print("Mon adresse:", reverse_geocode_result[0]["formatted_address"])
    return'''


'''def map(lieu):
    a=client.geocode(lieu)
    try:
        a=a[0]
        localisation=''
        for i in a['address_components']:
            localisation+=i['long_name']+ ' '
        localisation+=a['formatted_address']
        localisation+=f" latitude:  {a['geometry']['location']['lat']}, longitude: {a['geometry']['location']['lat']}, {traduct(a['types'][-1])}"
        return traduct(localisation)
    except:
        return "Ce lieu ne semble pas etre sur la carte, veuillez donner plus de précision svp"
def direction(place):
    import urllib.request
    import json
    endpoint='https://maps.googlemapi.com/maps/api/directions/json?'

    origin="Universite de lome".replace(' ', '+')#myadress().encode('utf-8').strip().replace(' ', '+')
    destination=place.replace(' ', '+')
    place_request=f'origin={origin}&destination={destination}&key={key}'
    place_request=endpoint+place_request
    print(place_request)
    response=urllib.request.urlopen(place_request).read()
    chemin=json.loads(response)
    print(chemin)'''

def distance(destination):

    response=client.distance_matrix(origins=myadress(),
                          destinations=destination,
                          departure_time=datetime.now() + timedelta(minutes=10))
    t=f"Disance: {response['rows'][0]['elements'][0]['distance']['text']}, temps approximative: {response['rows'][0]['elements'][0]['duration']['text']}"
    return t
'''
def direction(destination, ad):
    result = client.directions(origin=ad,#myadress(),
                                         destination=destination,
                                         mode="transit",)
                                         #arrival_time=datetime.now() + timedelta(minutes=0.5))
    return result'''

from googlemaps import convert


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
    """Get directions between an origin point and a destination point.
    :param origin: The address or latitude/longitude value from which you wish
        to calculate directions.
    :type origin: string, dict, list, or tuple
    :param destination: The address or latitude/longitude value from which
        you wish to calculate directions. You can use a place_id as destination
        by putting 'place_id:' as a prefix in the passing parameter.
    :type destination: string, dict, list, or tuple
    :param mode: Specifies the mode of transport to use when calculating
        directions. One of "driving", "walking", "bicycling" or "transit"
    :type mode: string
    :param waypoints: Specifies an array of waypoints. Waypoints alter a
        route by routing it through the specified location(s). To influence
        route without adding stop prefix the waypoint with `via`, similar to
        `waypoints = ["via:San Francisco", "via:Mountain View"]`.
    :type waypoints: a single location, or a list of locations, where a
        location is a string, dict, list, or tuple
    :param alternatives: If True, more than one route may be returned in the
        response.
    :type alternatives: bool
    :param avoid: Indicates that the calculated route(s) should avoid the
        indicated features.
    :type avoid: list or string
    :param language: The language in which to return results.
    :type language: string
    :param units: Specifies the unit system to use when displaying results.
        "metric" or "imperial"
    :type units: string
    :param region: The region code, specified as a ccTLD ("top-level domain"
        two-character value.
    :type region: string
    :param departure_time: Specifies the desired time of departure.
    :type departure_time: int or datetime.datetime
    :param arrival_time: Specifies the desired time of arrival for transit
        directions. Note: you can't specify both departure_time and
        arrival_time.
    :type arrival_time: int or datetime.datetime
    :param optimize_waypoints: Optimize the provided route by rearranging the
        waypoints in a more efficient order.
    :type optimize_waypoints: bool
    :param transit_mode: Specifies one or more preferred modes of transit.
        This parameter may only be specified for requests where the mode is
        transit. Valid values are "bus", "subway", "train", "tram", "rail".
        "rail" is equivalent to ["train", "tram", "subway"].
    :type transit_mode: string or list of strings
    :param transit_routing_preference: Specifies preferences for transit
        requests. Valid values are "less_walking" or "fewer_transfers"
    :type transit_routing_preference: string
    :param traffic_model: Specifies the predictive travel time model to use.
        Valid values are "best_guess" or "optimistic" or "pessimistic".
        The traffic_model parameter may only be specified for requests where
        the travel mode is driving, and where the request includes a
        departure_time.
    :type units: string
    :rtype: list of routes
    """
    origin=myadress()
    params = {
        "origin": convert.latlng(origin),
        "destination": convert.latlng(destination)
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

    di=client._request("/maps/api/directions/json", params).get("routes", [])
    #print(len(di), type(di), di[0].keys())
    text=f"Informations sur votre trajet de chez vous à {destination}, {di[0]['legs'][0]['end_address']} : "
    text+=f"Distance estimé à {di[0]['legs'][0]['distance']['text']}, Durée du trajet estimé à {di[0]['legs'][0]['duration']['text']}" \
          f" Les differentes tournures: "
    '''print(di[0]["legs"][0]["traffic_speed_entry"])
    print(di[0]["legs"][0]["via_waypoint"])
    print(di[0]["legs"][0]["steps"][0].keys())
    print(di[0]["legs"][0]["steps"][0]["html_instructions"])
    print(di[0]["legs"][0]["steps"][0]["travel_mode"])'''
    j=0
    for i in di[0]["legs"][0]["steps"]:
        j+=1
        if actuel=="oui":
            try:
                text += f"Vous marchez {i['distance']['text']}, estimé à environ {i['duration']['text']},  {traduct(text_clean(i['html_instructions']))}, {traduct(i['maneuver'])} "  # , "
            except:
                text += f"Vous marchez {i['distance']['text']}, estimé à environ {i['duration']['text']},  {traduct(text_clean(i['html_instructions']))} "
            break

        if j==1:
            text += f" \n 1ere partie: "
        else:
            text += f" \n {j}eme partie: "

        try:
            text+= f"Vous marchez {i['distance']['text']}, estimé à environ {i['duration']['text']},  {traduct(text_clean(i['html_instructions']))}, {traduct(i['maneuver'] )} "#, "
        except:
            text+= f"Vous marchez {i['distance']['text']}, estimé à environ {i['duration']['text']},  {traduct(text_clean(i['html_instructions']))} "
    text=text.replace("onto", "sur la").replace("min", "minutes").replace(" h ", "heures")
    return text

    #print(text)


