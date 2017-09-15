La orientación de nuestro proyecto consiste en un enfoque amigable para un lenguaje de programación, que al ser usado simula una interacción con un perro/mascota para el usuario.

El BNF se presenta a continuación:

statement	: declaration
		| assignment
		| write

declaration	: 'let' id 'be a' type   // id 'is' type

assignment	: 'set' id 'to' expression // 'now' id '=' expression

write		: 'write' expression 'to stdout' // 'bay' expression 'loud'

expression	: id
		| number

id		: char
		| id digit
		| id char

type		: 'number'
		| 'word'  //nuevo

char		: 'a'
		| ...
		| 'z'

number		: number digit
		| digit

digit		: '0'
		| ...
		| '9'





