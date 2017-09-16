La orientación de nuestro proyecto consiste en un enfoque amigable para un lenguaje de programación, que al ser usado simula una interacción con un perro/mascota para el usuario.

El BNF se presenta a continuación:

<Program> ::= 'hey pupper' <nl><Statements>'PlayDead4Real'

<Statements>::= <nl><gudboi?><Statement><nl><Statements>
            |!Empty

<Statement>    ::= <Read>  //entrada
            | <Bark>                //salida
            | <PlayDead>
            | <Conditional>
            | <RollOver>
            
<gudboi?>   ::= 'badboi'
            |'gudboi!'
            
<PlayDeadForReal>

<Bark>      ::= 'Bork!'
            | 'Bark!'
            | 'Woof!'
            | 'imma real pupper i swear! guau guau'
            
<nl>        ::= '\n' <nl>
            | '\n'
<PlayDead>  ::= 'Play Dead' (<char>|<lilnumba>)

<assignment>::= 'now' <id> '=' <expression>

<declaration>::= <id> 'is' <type>

<write>   ::= 'bark' <expression>

<expression>	: <id>
		| <numba>
		| <word>

<id>	   ::= <char>
		| <id> <lilnumba>
		| <id> <char>

<type> ::= <numba>
		| <word>

<word> ::= <char>
        |<char> <word>

<char> ::= ['a'-'z']

<numba> ::= <numba> <lilnumba>
		| <lilnumba>

<lilnumba>	::= ['0'-'9']





