from countryinfo import CountryInfo


country = CountryInfo(input("Enter Country Name: "))

print(f"Country Name: {country.name()}")
print(f"Country Capital: {country.capital()}")
print(f"Country Population: {country.population()}")
print(f"Country Area In Km: {country.area()}")
print(f"Country Region: {country.region()}")
print(f"Country SubRegion: {country.subregion()}")
print(f"Country Demonym: {country.demonym()}")
print(f"Country Currency: {country.currencies()}")
print(f"Country Languages: {country.languages()}")
print(f"Country Borders: {country.borders()}")

