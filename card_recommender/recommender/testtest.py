import requests
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
    
    
print(get_geo_code("Random","Random"))