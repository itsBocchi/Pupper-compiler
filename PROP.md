La orientación de nuestro proyecto consiste en un enfoque amigable para un lenguaje de programación, que al ser usado simula una interacción con un perro/mascota para el usuario, a la cual le "enseñamos" cosas nuevas al trabajar con variables (crearlas, renombrarlas o asignarles valor).

### BNF
```
<Program>       ::= 'hey pupper' [<nl><Statements>] <PlayDead4Real>

<Statements>    ::= <nl><gudboi?><Statement><nl><Statements>
                | !Empty

<Statement>	::= <Read>  //entrada
                | <Bark>                //salida (mostrar por consola)
                | <PlayDead>
                | <Conditional>
                | <RollOver>
	        	| <assignment>
	        	| <declaration>
	        	| <Statements>          //"relleno" (abre paso para llenar el programa) 
            
<gudboi?>       ::= 'badboi'
                |'gudboi!'
                |'nice dogger'
            
<PlayDead4Real> ::='Play Dead gud doggo'//elemento terminal para finalizar el programa

<Bark>          ::= <id>                //id para imprimir el valor de una variable
	        	| <wurd>
	        	| <numba>
	        	|'Bork!'<s><Bark>
                | 'Bark!'<s><Bark>
                | 'Woof!'<s><Bark>
                | 'imma real pupper i swear! guau guau'<s><Bark>

            
<nl>            ::= '\n' <nl>
                | '\n'

<s>		::= ' '
            
<PlayDead>      ::= 'Play Dead' (<char>|<lilnumba>)*  //elemento no terminal para "pausar el programa"

<RollOver>      ::= 'Roll Over!' [<nl><statement>] {[<nl>'again']} <nl>'gboi'

<declaration>   ::= <id> 'is' <type>

<assignment>    ::= 'now' <id> '=' <expression>

<add>			::= 'get together ' <id> ' and ' <id>|<expression> as <id>

<write>         ::= 'bark' <expression>

<expression>    ::= <id>        //valores de las variables
	        	| <numba>
	        	| <wurd>

<id>            ::= <char>          //nombres de variables
	        	| <id> <lilnumba>
	        	| <id> <char>		//tambien se podia emplear directamente <wurd> 

<type>          ::= 'numba'
	        	| 'wurd'

<wurd>          ::= [<wurd>]<char>

<char>          ::= ['a'-'z']|<s>

<numba>         ::= <numba><lilnumba>
	        	| <lilnumba>

<lilnumba>	    ::= ['0'-'9']
```
### Ejemplo:

Input

hey pupper
x is numba
now x = 4
w is wurd
newwurd is wurd
anotherwurd is wurd
now anotherwurd =  times
now w is great things come to you but only if you say be safe good doggo 
get together w and x as newwurd
get together newwurd and anotherwurd as newwurd
bark newwurd


Output

great things come to you but only if you say "be safe good doggo 4 times"