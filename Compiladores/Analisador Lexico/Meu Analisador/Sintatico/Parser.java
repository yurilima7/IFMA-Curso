package Sintatico;

import Excecoes.ErroSintatico;
import Lexico.Analisador;
import Lexico.Token;

public class Parser {
    private Analisador scanner;
    private Token token;

    public Parser(Analisador scanner){
        this.scanner = scanner;
    }
    
    public void S(){
        token = scanner.percorreToken();
        
        if(token != null){P(); S(); }
       
    }

    public void P(){

        if(token.getTipo() != Token.CADEIA){
            throw new ErroSintatico("Erro sintático encontrado");
        }
    }

    
}
