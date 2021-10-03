import phonenumbers
# importing number from the main file
from main import number

# Get the  country name
from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_nmber,"en"))

# Get the service provider name
from phonenumbers import carrier
service_number = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))