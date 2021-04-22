#Define a lista:
alien_0 = {'x_position': 0, 'y_position': 25, 'speedy': 'medium'}
print(f"Original x-position: {str(alien_0['x_position'])}")

#Move o alienígena para a direita
#Determina a distância que o alienígena deve se deslocar de acordo com a sua velocidade atual

if alien_0['speedy'] == 'slow':
    x_increment = 1
elif alien_0['speedy'] == 'medium':
    x_increment = 2
#Este deve ser um alienígena rápido:
else: x_increment = 3

#A nova posição é a posição antiga somada ao incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New x-position {str(alien_0['x_position'])}")
