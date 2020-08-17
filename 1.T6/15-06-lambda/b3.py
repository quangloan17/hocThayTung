def getAddress(street,city,country = 'Việt Nam'):
    return f'{street}, {city}, {country}'
print(getAddress('Cầu Giấy', 'Hà Nội'))
