La orientación de nuestro proyecto consiste en un enfoque amigable para un lenguaje de programación, que al ser usado simula una interacción con un perro/mascota para el usuario, a la cual le "enseñamos" cosas nuevas al trabajar con variables (crearlas, renombrarlas o asignarles valor). La idea no es que sea facil de codificar.

El BNF se presenta a continuación:

\<Program\>       ::= 'hey pupper' [\<nl\>\<Statements\>] \<PlayDead4Real\>

\<Statements\>    ::= \<nl\>\<gudboi?\>\<Statement\>\<nl\>\<Statements\>
                | !Empty

\<Statement\>	::= \<Read\>  //entrada
                | \<Bark\>                //salida (mostrar por consola)
                | \<PlayDead\>
                | \<Conditional\>
                | \<RollOver\>
	        	| \<assignment\>
	        	| \<declaration\>
	        	| \<Statements\>          //"relleno" (abre paso para llenar el programa) 
            
\<gudboi?\>       ::= 'badboi'
                |'gudboi!'
                |'nice dogger'
            
\<PlayDead4Real\> ::='Play Dead gud doggo'//elemento terminal para finalizar el programa

\<Bark\>          ::= \<id\>                //id para imprimir el valor de una variable
	        	| \<word\>
	        	| \<numba\>
	        	|'Bork!'\<s\>\<Bark\>
                | 'Bark!'\<s\>\<Bark\>
                | 'Woof!'\<s\>\<Bark\>
                | 'imma real pupper i swear! guau guau'\<s\>\<Bark\>

            
\<nl\>            ::= '\n' \<nl\>
                | '\n'

\<s\>		::= ' '
            
\<PlayDead\>      ::= 'Play Dead' (\<char\>|\<lilnumba\>)*  //elemento no terminal para "pausar el programa"

\<RollOver\>      ::= 'Roll Over!' [\<nl\>\<statement\>] {[\<nl\>'again']} \<nl\>'gboi'

\<declaration\>   ::= \<id\> 'is' \<type\>

\<assignment\>    ::= 'now' \<id\> '=' \<expression\>

\<write\>         ::= 'bark' \<expression\>

\<expression\>    ::= \<id\>        //valores de las variables
	        	| \<numba\>
	        	| \<word\>

\<id\>            ::= \<char\>          //nombres de variables
	        	| \<id\> \<lilnumba\>
	        	| \<id\> \<char\>		//tambien se podia emplear directamente \<word\> 

\<type\>          ::= 'numba'
	        	| 'word'

\<word\>          ::= \<char\>
                |\<word\>\<char\>

\<char\>          ::= ['a'-'z']

\<numba\>         ::= \<numba\>\<lilnumba\>
	        	| \<lilnumba\>

\<lilnumba\>	    ::= ['0'-'9']

## Ejemplos:

La derivación para that is numba :

	\<Statement\>
	\<declaration\>
	\<id\> 'is' \<type\>
	\<id\> 'is' 'numba'
	\<word\> 'is' 'numba'
	\<word\>\<char\> 'is' 'numba'
	\<word\>'t' 'is' 'numba'
	\<word\>\<char\>'t' 'is' 'numba'
	\<word\>'a''t' 'is' 'numba'
	\<word\>\<char\>'a''t' 'is' 'numba'
	\<word\>'h''a''t' 'is' 'numba'
	\<char\>'h''a''t' 'is' 'numba'
	't''h''a''t' 'is' 'numba'
	'that' 'is' 'numba'

La derivación para now t = 23 :

	\<Statement\>
	\<assignment\>
	'now' \<id\> '=' \<expression\>
	'now' \<id\> '=' \<numba\>
	'now' \<id\> '=' \<numba\>\<lilnumba\>
	'now' \<id\> '=' \<numba\>'3'
	'now' \<id\> '=' \<lilnumba\>'3'
	'now' \<id\> '=' '2''3'
	'now' \<char\> '=' '23'
	'now' 't' '=' '23'	

La derivación para 'imma real pupper i swear! guau guau lol' :

	\<Statement\>
	\<Bark\>
	'imma real pupper i swear! guau guau'\<s\>\<Bark\>
	'imma real pupper i swear! guau guau'\<s\>\<word\>
	'imma real pupper i swear! guau guau'\<s\>\<word\>\<char\>
	'imma real pupper i swear! guau guau'\<s\>\<word\>'l'
	'imma real pupper i swear! guau guau'\<s\>\<word\>\<char\>'l'
	'imma real pupper i swear! guau guau'\<s\>\<word\>'o''l'
	'imma real pupper i swear! guau guau'\<s\>\<char\>'o''l'
	'imma real pupper i swear! guau guau'\<s\>'l''o''l'
	'imma real pupper i swear! guau guau'' ''l''o''l'
	'imma real pupper i swear! guau guau lol'
