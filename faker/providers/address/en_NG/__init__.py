from __future__ import unicode_literals
from .. import Provider as AddressProvider


class Provider(AddressProvider):
    building_number_formats = ('#', '##', '###')
    street_suffixes = ('Avenue', 'Road', 'Street')
    states = (
        'Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 
        'Benue', 'Borno', 'Cross-River', 'Delta', 'Edo', 'Ekiti', 'Enugu', 
        'Gombe', 'Imo', 'Jigawa', 'Kaduna', 'Kano', 'Katsina', 'Kebbi', 
        'Kogi', 'Kwara', 'Lagos', 'Nassarawa', 'Niger', 'Ogun', 'Ondo', 
        'Osun', 'Oyo', 'Plateau', 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 
        'Zamfara', 'FCT',
    )
    
    states_abbr = (
        'AB', 'AD', 'AK', 'AN', 'BA', 'BY', 'BE', 'BO', 'CR', 'DE', 'EB', 'ED',
        'EK', 'EN', 'GO', 'IM', 'JI', 'KD', 'KN', 'KT', 'KE', 'KO', 'KW', 'LA',
        'NA', 'NI', 'OG', 'ON', 'OS', 'OY', 'PL', 'RI', 'SO', 'TA', 'YO', 'ZA'
    )
    
    city_names = (
        'Aba', 'Abeokuta', 'Abuja', 'Akure', 'Asaba', 'Awka', 'Bauchi', 
        'Benin-City', 'Birnin Kebbi', 'Calaba', 'Damaturu', 'Dambatta', 
        'Dutse', 'Enugu', 'Funtua', 'Gaya', 'Gumel', 'Gusau', 'Hadejia', 
        'Ibadan', 'Ikeja', 'Ilorin', 'Jalingo', 'Jos', 'Kaduna', 'Kafanchan', 
        'Kano', 'Katsina', 'Kazaure', 'Lafia', 'Lokoja', 'Maiduguri', 
        'Malumfashi', 'Markurdi', 'Minna', 'Okigwe', 'Onisha', 'Orlu', 'Oshogbo', 
        'Owerri', 'Port Harcourt', 'Potiskum', 'Sokoto', 'Umahia', 'Uyo', 
        'Vandekia', 'Wudil', 'Yenagoa', 'Yola', 'Zaria', 
    )
    
    city_formats = (
        '{{cities}}',
    )
    
    street_name_formats = (
        '{{first_name}} {{street_suffix}}',
        '{{last_name}} {{street_suffix}}',
    )
    
    street_address_formats = (
        '{{building_number}} {{street_name}}',
        '{{secondary_address}}\n{{street_name}}',
    )
    
    address_formats = (
        '{{street_address}}\n{{city}}, {{state}}',
    )
    
    secondary_address_formats = ('Flat #', 'Flat ##', 'Flat ##?')
    
    @classmethod
    def cities(cls):
        return cls.random_element(cls.city_names)
    
    @classmethod
    def state(cls):
        return cls.random_element(cls.states)
    
    @classmethod
    def state_abbr(cls):
        return cls.random_element(cls.states_abbr)
    
    @classmethod
    def secondary_address(cls):
        return cls.bothify(cls.random_element(cls.secondary_address_formats))
    