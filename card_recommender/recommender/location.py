import requests
import numpy as np

app_id = "EPimKPfenNGqsgGCr01O"
app_code  = "n6V78llT2352UUagDt295g"

def get_geo_code(area,city):
    """ Gets the geocode for the area given by user input.
        Geocode is the latitude and longitude from the 
        text input by user.
        Uses the geocoding api by HERE technologies. """
    searchtext=area + "+"+city
    geo_code = requests.get("https://geocoder.api.here.com/6.2/geocode.json",
                             params={"app_id":app_id,
                                     "app_code":app_code,
                                     "searchtext":searchtext})
    if geo_code.status_code==200:
        latitude= geo_code.json()['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
        longitude = geo_code.json()['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
        return (latitude,longitude)
    else:
        return "Failed to enable location features"
    
    
    
def make_browse_request(latitude,longitude):
    """Make the API request to search for nearby banks based on latitude and longitude"""
    browse_request = f"""https://places.cit.api.here.com/places/v1/browse?app_id={app_id}&app_code={app_code}&in={latitude},{longitude};r=5000&cat=atm-bank-exchange&pretty"""
    return browse_request

def get_browse_response(browse_request):
    """ Get the distances for all nearby banks"""
    response = requests.get(browse_request)
    bank_names_distance = {}
    if response.status_code==200:
        json_result = response.json()
        for result in json_result["results"]["items"]:
            bank_name = result["title"].lower().replace("-",' ')
            distance = result["distance"]
            bank_names_distance[bank_name] = distance
    return bank_names_distance

def process_bank_names(bank_names):
    return [name.replace("Limited",'').lower().strip() for name in bank_names]

def location_scoring_banks(card_preference_banks, geo_results):
    """Assign location scores to banks that scored high in preference"""
    card_bank_score = {}
    # Traverse through each of the banks that ranked high in the preferences
    for card_bank in card_preference_banks:
        current_bank_scores = []
        # if any of those banks area nearby, then get a location score for those banks
        for result in geo_results.keys():
            result = result
            if card_bank in result:
                current_bank_scores.append(geo_results[result])
        # each bank may have multiple locations, so the location score for a bank is the minimum of all the location scores.
        try:
            current_bank_score_avg = np.array(current_bank_scores).min()
        except:
            current_bank_score_avg = np.inf
        # assign the location score to each of the banks from the card preference
        card_bank_score[card_bank] = current_bank_score_avg
        
    return card_bank_score




def location_scoring_cards(user_location,card_preference_banks):
    # clean up data 
    card_preference_banks = process_bank_names(card_preference_banks)

    # First find the geocoes from user input
    area = user_location["area"]
    city = user_location["city"]
    geo_codes = get_geo_code(area,city)
    if type(geo_codes) == type((1,1)):
    # if successfully geocodes are found, then find nearby banks
        browse_request  = make_browse_request(latitude=geo_codes[0],longitude=geo_codes[1])
    # location score the banks which scored high on card preference based on the distance
        geo_results = get_browse_response(browse_request)
        bank_location_scores = location_scoring_banks(card_preference_banks,geo_results)
        return bank_location_scores
    else:
        return "Fail"
    

