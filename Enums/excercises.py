from enum import Enum

class Country(Enum):
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

#Write a Python program to create an Enum object and display a member name and value.
print('\nMember name: {}'.format(Country.Algeria.name))
print('Member value: {}'.format(Country.Algeria.value))

# Write a Python program that iterates over an enum class and displays each member and their value.
for e in Country:
    print('\nMember name: {}'.format(e.name))
    print('Member value: {}'.format(e.value))

#Write a Python program to display all the member names of an enum class ordered by their values.

print('Country Name ordered by Country Code:')
# print('\n'.join('  ' + c.name for c in sorted(Country)))