# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     print(b,a)
# else:
#     print(a,b)
#

is_rain = input("Is rain? ")
is_rain_lower = is_rain.lower()
if is_rain_lower == 'yes':
    is_wind = input("wind?").lower()
    if is_wind == 'yes':
        print('bla-bla-bla')
    else:
        print('Take an umbprella')
else:
    print("enjoy your day")