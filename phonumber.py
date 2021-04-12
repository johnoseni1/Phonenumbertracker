import phonenumbers
from testy import number

from phonenumbers import geocoder
numbers = phonenumbers.parse(number, "NH")
print(geocoder.description_for_number(numbers, "en"))

from phonenumbers import carrier
network = phonenumbers.parse(number, "GH")
print(carrier.name_for_number(network, "en"))

