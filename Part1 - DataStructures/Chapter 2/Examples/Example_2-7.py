#Example 2-7. Tuples used as records

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

# '%s%s' -> i expect two elements inside passport i.e. USA and 31195855
for passport in sorted(traveler_ids):
    print('%s%s' % passport) #The % formatting operator understands tuples and treats each item as a separate field



for country, _ in traveler_ids: # i use _ to discard the second item of the tuple
    print(country)