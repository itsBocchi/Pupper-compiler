La orientación de nuestro proyecto consiste en un enfoque amigable para un lenguaje de programación, que al ser usado simula una interacción con un perro/mascota para el usuario.

El BNF se presenta a continuación:

order		: declaration
		| assignment
		| write

declaration	: 'let' id 'be a' type   // id 'is' thing

<Program> ::= 'hey pupper' <nl> <gudboi?><nl><Statements> 'gud boi!'

<Statements>    ::= <Statements>::= <Statement><nl><gudboi?><nl><Statements>

<Statement>    ::= <Read>  //entrada
            | <Bark>                //salida
            | <PlayDeadForReal>         
            | <PlayDead>
            | <Conditional>
            | <RollOver>
            | <Stop!>
            
<gudboi?>   ::= badboi
        |guuuudboi
        
<Bark>        ::= 'Bork!'
    | 'Bark!'
    | 'Woof!'
    | 'imma real pupper i swear! guau guau'
    
<Read> ::= 'GIMMEH' <ReadOp> Identifier
            
<nl>         ::= '\n' <nl>
            | '\n'

assignment	: 'set' id 'to' expression // 'now' id '=' expression

write		: 'write' expression 'to stdout' // 'bark' expression 

expression	: id
		| numba
		| word

id		: char
		| id lil'numba
		| id char

thing		: 'numba' // 
		| 'word'  //nuevo

word ::= char
        |charword

char		: ['a'-'z']

numb		: numba lil'numba
		| digit

lil'numba	: ['0'-'9']





