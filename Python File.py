import random 

daniil = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

number = int( input( 'Кол-во паролей: ' ) )
lenght = int( input( 'Длина строки: ' ) )

for x in range( number ):
	password = ''

	for i in range( lenght ):
		password += random.choice( daniil )

	print( password )
