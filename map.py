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
import os
key="AIzaSyAVr_nuK2dm72cMIgc_ga5yAM1zRYXMnr0"
client=googlemaps.Client(key)
trans=Translator()

def traduct(text):
    return trans.translate(text, dest="fr").text


def gsearch(p):
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
                text+=" ".join(e.split('.')[:10])
                
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
    '''if "bbc" in command:
        url="http://stream.live.vc.bbcmedia.co.uk/bbc_radio_one" '''
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



#gsearch("Qui est SEKPONA Kokou Sitsopé ?")
def myadress():
    url = "http://ipinfo.io/json"
    tes = urlopen(url)
    res = json.load(tes)
    #reverse_geocode_result = client.reverse_geocode((float(res['loc'].split(',')[0]),float(res['loc'].split(',')[-1])))#(float(res['loc'].split(',')[0]), float(res['loc'].split(',')[-1])))
    lat, long=float(res['loc'].split(',')[0]),float(res['loc'].split(',')[-1])
    print(lat, long)
    doi_link  = 'https://www.google.com/maps'#https://doi.org/10.1016/j.artint.2018.07.007'
    response = requests.get(url= doi_link ,allow_redirects=True )
    
    # use final response
    # parse html and get final redirect url
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)
    url = soup.findAll("meta")
    #print("voila url: ", url)d
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
        long=lien[1].split("&")[0]#print("adresse ip: ", client.geocode(str(reverse_geocode_result)))
        lat=6.206263
        long=1.202593
        reverse_geocode_result = client.reverse_geocode((round(float(lat), 6), round(float(long), 6)))#(float(res['loc'].split(',')[0]), float(res['loc'].split(',')[-1])))
        print(round(float(lat), 6), long)
        t=reverse_geocode_result[0]["formatted_address"]
        print("Mon adresse:", reverse_geocode_result[0]["formatted_address"])
        for i in reverse_geocode_result:
            try:
                for j in i["formatted_address"].lower().split(','):
                   if "region" in j:
                       t+=" "+j
            except:
                pass
        print(t)
        return t
    #return float(res['loc'].split(',')[0]),float(res['loc'].split(',')[-1])
#myadress()
def myadress():
    doi_link  = 'https://www.google.com/maps'
    #https://doi.org/10.1016/j.artint.2018.07.007'
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
    fin=""
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
        print(reverse_geocode_result)
        fin=f"Vous etes actuellement à {reverse_geocode_result[0]['formatted_address']}"#(float(res['loc'].split(',')[0]), float(res['loc'].split(',')[-1])))
        print(fin)#, client.geocode(str(reverse_geocode_result)))
        for i in reverse_geocode_result:
            try:
               print(i[0]["formatted_address"])
            except:
                pass
        fin=fin
    else:
        fin= "Je n'ai pas pu vous localiser"
    
    url = "http://ipinfo.io/json"
    tes = urlopen(url)
    res = json.load(tes)
    reverse_geocode_result = client.reverse_geocode((float(res['loc'].split(',')[0]),float(res['loc'].split(',')[-1])))
    #(float(res['loc'].split(',')[0]), float(res['loc'].split(',')[-1])))
    fin+=" "+reverse_geocode_result[0]['formatted_address']
    return fin
#print(position())


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
            break
    lien = link
    print(lien)
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
    reverse_geocode_result = client.reverse_geocode((6.1734912,1.1763712))#(float(res['loc'].split(',')[0]), float(res['loc'].split(',')[-1])))
    print("adresse ip: ", client.geocode(str(reverse_geocode_result)))
    print("Mon adresse:", reverse_geocode_result[0]["formatted_address"])
    return float(res['loc'].split(',')[0]), float(res['loc'].split(',')[-1])

def distance(destination):

    response=client.distance_matrix(origins=myadress(),
                          destinations=destination,
                          departure_time=datetime.now() + timedelta(minutes=10))
    t=f"Disance: {response['rows'][0]['elements'][0]['distance']['text']}, temps approximative: {response['rows'][0]['elements'][0]['duration']['text']}"
    return t

#from googlemaps import convert


def text_clean(t):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(t, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.get_text()
    return text

''' def directions( destination,actuel="non",
                waypoints=None, alternatives=False, avoid=None,
               language=None, units=None, region=None, departure_time=None,
               arrival_time=None, optimize_waypoints=False, transit_mode=None,
               transit_routing_preference=None, traffic_model=None, client=client,  mode="walking"):
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
    return text '''



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
    l11=[ "localisation", "localise", "trouve", "trouve-moi","où",
              "où se trouve","localise-moi", "localises-moi"]
    for i in l11:
        destination=destination.replace(i, "")
    destination=destination.replace('moi', '')
    print("dest:", destination)
    #origin = "universite de lome"
    origin = position1()
    #origin=convert.latlng(origin)
    print(origin)

    params = {
        "origin": origin, # convert.latlng(origin),
        "destination": convert.latlng(destination)#destination.replace(' ', '+') #
    }
    print(convert.latlng(destination))
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
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    for cle, val in params.items():
        complete+=f"{cle}={val.replace(' ', '+')}&"
    complete+=f"key={key}"
    place_request=endpoint+complete
    
    
    try:
        response = urllib.request.urlopen(place_request).read()
        chemin = json.loads(response)
        di= chemin["routes"]

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
    except:
        text=position()+", Je ne trouve pas l'endroit, veuillez reessayer en présisant l'adresse"
    return text







'''
from youtube_search import YoutubeSearch
results = YoutubeSearch('Je benirai le seigneur en chantant', max_results=2)
a=results.to_dict()[0]
url=a["thumbnails"]#['url']
print(url, a)'''

# returns a json string

########################################
'''
results = YoutubeSearch('search terms', max_results=10).to_dict()

print(results)'''
# returns a dictionary
'''import yt_dlp as youtube_dl
#from youtubesearchpython import VideosSearch
from youtube_search import YoutubeSearch
videosSearch = VideosSearch("Je benirai le seigneur en chantant", limit = 2)
print(videosSearch.result())'''



#youtube("Jeurlopen benirai le seigneur en chantant")
'''
import vlc

instance = vlc.Instance()
player = instance.media_player_new()
player.set_media(instance.media_new(streaming_url))
player.set_playback_mode(0) # 0 for automatic playback
player.play()'''

#print(directions(destination="localise moi le Port Autonome de Lome", language="fr"))
