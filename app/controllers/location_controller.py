class LocationController:
    @staticmethod
    def search(repository, value):
        fields = ["country"]
        country = repository.search(fields, value)
        country = [location.country for location in country]
        country = list(dict.fromkeys(country))
        fields = ["city"]
        cities = repository.search(fields, value)
        cities = [f"{location.city}, {location.country}" for location in cities]

        return country + cities
