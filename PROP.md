La orientación de nuestro proyecto consiste en la implementación de un lenguaje amigable, el cual simula la interacción con un perro/mascota para el usuario, a la cual le "enseñamos" cosas nuevas al trabajar con variables (crearlas, asignarles valor o incluso "hacer trucos con estas" ). Intentamos crear un lenguaje esoterico, de interés no sólo para usuarios experimentados sino también para aquellos que comienzan a adentrarse al mundo de la programación. Su principal ventaja será el tamaño del transpiler.

### EBNF
```
/<Program/>       ::= 'hey pupper' {[/<Statement/>]} /<PlayDead4Real/>

/<Statement/>	::=  /<Bark/>                //salida
                | /<Conditional/>
                | /<RollOver/>
	        	| /<assignment/>
	        	| /<declaration/>
	        	          //"relleno" (abre paso para llenar el programa) 
	        	
            
/<PlayDead4Real/> ::='stay safe gud doggo'//elemento terminal para finalizar el programa

/<Conditional/>   ::= 'Come here boi' /<statement/>     //if, permite 1 statement, random int 0-1, de ser 1 ejecuta solo la siguiente linea

/<Bark/>          ::= 'Bork! ' /<expression/>
                | 'Bark! ' /<expression/>
                | 'Woof! ' /<expression/>
                | 'imma real pupper i swear! guau guau ' /<expression/>


/<RollOver/>      ::= 'roll over!' [/<statement/>] {['again']} 'gboi'

/<declaration/>   ::= /<id/> 'is' /<type/>

/<assignment/>    ::= 'now' /<id/> '=' /<expression/>

/<add/>             ::= 'get together ' /<id/> ' and ' /<id/>|/<expression/> as /<id/>      //suma expresiones o id. tambien concatena wurd, wurd con numba son compatibles (se le asigna valor al ultimo id)

/<expression/>    ::= /<id/>        //valores de las variables
	        	| /<numba/>
	        	| /<wurd/>
	        	| /<Read/>  //entrada
	        	
/<Read/>            ::= 'look at this' /<wurd/>
                    | 'look at this' /<numba/>

/<id/>            ::= /<char/>          //nombres de variables
	        	| /<id/> /<lilnumba/>
	        	| /<id/> /<char/>		//tambien se podia emplear directamente /<wurd/> 

/<type/>          ::= 'numba'           //al nombrar tipos, puede ser <numba>
	        	| 'wurd'

/<wurd/>          ::= {Letter}

/<numba/>         ::= {Alphanumeric}

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
/>/>/>great things come to you but only if you say "be safe good doggo 4 times"
```