filter = input('Enter your request (Home,Specific): ')
if filter == 'Home':
    Home = input('Home clothes (sweater, t-shirt, shorts): ')
    if Home == 'sweater':
        color = input('Enter the color you want (grey, red, blue): ')
        print('You ordered ' + color + ' ' + Home + ' everyday type')
    elif Home == 't-shirt':
        color = input('Enter the color you want (black, white, grey, purple): ')
        print('You ordered ' + color + ' ' + Home + ' everyday type')
    elif Home == 'shorts':
        color = input('Enter the color you want (black, blue, grey): ')
        print('You ordered ' + color + ' ' + Home + ' everyday type')
    else:
        print('Our online store does not have such home clothes!')
elif filter == 'Specific':
    Specific = input('Specific clothes (shirt, jacket, tie): ')
    if Specific == 'shirt':
        color = input('Enter the color you want (white, blue): ')
        print('You ordered ' + color + ' ' + Specific + ' specific type')
    elif Specific == 'jacket':
        color = input('Enter the color you want (black, red, purple): ')
        print('You ordered ' + color + ' ' + Specific + ' specific type')
    elif Specific == 'tie':
        color = input('Enter the color you want (black, red, white): ')
        print('You ordered ' + color + ' ' + Specific + ' specific type')
    else:
        print('Our online store does not have such specific clothes!')
else:
    print('Our online store does not have such type of clothes!')

