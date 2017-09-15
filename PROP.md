La orientación de nuestro proyecto consiste en un enfoque amigable para un lenguaje de programación, que al ser usado simula una interacción con un perro/mascota para el usuario.

El BNF se presenta a continuación:

order		: pee			//pee es declaration
		| assignment
		| write

pee		: 'let' id 'be a' type   // id 'is' thing

assignment	: 'set' id 'to' expression // 'now' id '=' expression

write		: 'write' expression 'to stdout' // 'bark' expression 'loud'

expression	: id
		| numba

id		: char
		| id lil'numba
		| id char

thing		: 'numba' // 
		| 'word'  //nuevo

char		: ['a'-'z']

numb		: numba lil'numba
		| digit

lil'numba	: ['0'-'9']





