 # exceptions.py
    class CityNotAllowedException(Exception):
    		message = 'The city {city} is not allowed'
    		
    		def __init__(self, city: str) -> None:
    				self.city = city
    				super().__init__(self.message.format(city=city))
    
    # service.py
    from .exceptions import CityNotAllowedException
    
    # ...
    	
    if user.city not in allowed_cities:
    		raise CityNotAllowedException(user.city)