grammar taskLang;

@header{
	import estruturas.taskSimbolo;
	import estruturas.taskTabelaSimbolo;
	import estruturas.taskVariavel;
	import excecoes.ExcecaoSemantica;
	import java.util.ArrayList;
}

@members{
	private int _tipo;
	private String _varName;
	private String _varValue;
	private taskTabelaSimbolo tabelaSimbolo = new taskTabelaSimbolo();
	private taskSimbolo simbolo;
	
	public void verificaID(String id){
		if (!tabelaSimbolo.exists(id)){
			throw new ExcecaoSemantica("Simbolo " + id + " nao declarado");
		}
	}
}

prog    : 'INICIO' decl bloco  'FIM$'
        ;

decl	: (declaravar)+
		;
		
declaravar : tipo ID {
				_varName = _input.LT(-1).getText();
				_varValue = null;
				simbolo = new taskVariavel(_varName, _tipo, _varValue);
				
					if (!tabelaSimbolo.exists(_varName)){
						tabelaSimbolo.add(simbolo);
					}else{
						throw new ExcecaoSemantica("Simbolo " + _varName + " ja foi declarado");
					}
				
				}
				
			 ( VIR 
			   ID  {
				_varName = _input.LT(-1).getText();
				_varValue = null;
				simbolo = new taskVariavel(_varName, _tipo, _varValue);
				
					if (!tabelaSimbolo.exists(_varName)){
						tabelaSimbolo.add(simbolo);
					}else{
						throw new ExcecaoSemantica("Simbolo " + _varName + " ja foi declarado");
					}
				
				}
				
			 )* SC
		   ;
		   
tipo	: 'Numero' {_tipo = taskVariavel.NUMBER; }
		| 'Texto'	{_tipo = taskVariavel.TEXT; }
		;

bloco   : (cmd)+
        ;

cmd     : cmdleitura 
		| cmdescrita 
		| cmdattrib 
        ;

cmdleitura  : 'Leia' AP 
					 ID { verificaID(_input.LT(-1).getText());}
					 FP 
					 SC
        ;

cmdescrita  : 'Escreva' AP 
						ID { verificaID(_input.LT(-1).getText());}
						FP 
						SC
        ;

cmdattrib   : ID { verificaID(_input.LT(-1).getText());}
			  ATTR 
			  expr 
			  SC
        ;

expr    : termo (OP termo)*
        ;

termo : ID { verificaID(_input.LT(-1).getText());}
	  | NUMBER
        ;

AP  : '('
    ;

FP  : ')'
    ;

SC  : '$'
    ;

OP  : '+' | '-' | '*' | '/'
    ;

ATTR    : '='
    ;
    
VIR	: ','
	;

ID  : [a-z] ([a-z] | ([A-Z]) | [0-9])*
    ;

NUMBER  : [0-9]+ ('.' [0-9]+)?
    ;
    
WS : (' ' | '\t' | '\n' | '\r') -> skip;