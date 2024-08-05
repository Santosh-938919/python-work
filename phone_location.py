import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+919939062057")
print("\n\nPhone location")
print(geocoder.description_for_number(phone_number1, "en"))