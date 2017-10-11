La orientación de nuestro proyecto consiste en la implementación de un lenguaje amigable, el cual simula la interacción con un perromascota para el usuario, a la cual le "enseñamos" cosas nuevas al trabajar con variables (crearlas, asignarles valor o incluso "hacer trucos con estas" ). Intentamos crear un lenguaje esoterico, de interés no sólo para usuarios experimentados sino también para aquellos que comienzan a adentrarse al mundo de la programación. Su principal ventaja será el tamaño del transpiler.

### EBNF
```
"Start Symbol" = \<START\>

\<START\>         ::= 'hey pupper' {[\<STATEMENT\>]} 'stay safe gud doggo'

\<STATEMENT\>     ::=  \<BARK\>                				#salida
                | \<CONDITIONAL\>
                | \<ROLLOVER\>
	        	| \<ASSIGN\>
	        	| \<ADD\>
	        	| \<DECLARATION\>
            

\<CONDITIONAL\>   ::= 'Come here boi' \<STATEMENT\>     #if, permite 1 STATEMENT, random int 0-1, de ser 1 ejecuta solo la siguiente linea

\<BARK\>          ::= 'Bork! ' \<EXPRESSION\>
                | 'Bark! ' \<EXPRESSION\>
                | 'Woof! ' \<EXPRESSION\>
                | 'imma real pupper i swear! guau guau ' \<EXPRESSION\>


\<ROLLOVER\>      ::= 'roll over!' [\<STATEMENT\>] {['UPDOGO ^_^']} 'gboi'

\<DECLARATION\>   ::= \<ID\> 'is' \<TYPE\>	#Crea un ID y le asigna un tipo(TYPE)

\<ASSIGN\>    ::= 'now' \<ID\> '=' \<EXPRESSION\>

\<ADD\>             ::= 'get together ' \<ID\>|\<EXPRESSION\> ' and ' \<ID\>|\<EXPRESSION\> as \<ID\>      #Concatenacion, si ambos son NUMBA 

\<EXPRESSION\>    ::= \<ID\>
	        	| \<READ\>
	        	
\<READ\>            ::= 'fetch!' \<WURD\>		#READ actua como input. Recibe WURD o NUMBA
                    | 'fetch!' \<NUMBA\>

\<ID\>            ::= \<WURD\>         		#nombres de variables
	        	| \<ID\> \<NUMBA\>
	        	| \<ID\> \<WURD\>			#tambien se podia emplear directamente \<WURD\> 

\<WURD\>          ::= {Letter}          	#Cualquier caracter ascii 65 al 90 y 97 al 122, es decir A a la Z y a a la z

\<NUMBA\>         ::= {Alphanumeric}    	#Cualquier caracter ascii 48 al 57, es decir del 0 al 9

\<TYPE\>          ::= 'numba'           	#usado para declarar tipo de dato
	        	| 'wurd'
```
### Ejemplo:

Input
```
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
play dead gud doggo
```
Output
```
\>\>\>great things come to you but only if you say "be safe good doggo 4 times"
```