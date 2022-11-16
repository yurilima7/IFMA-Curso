package Sintatico;
import Erros.SintaxeException;
import Lexico.Token;
import Lexico.lexScanner;

public class Parser {
    private lexScanner scanner;
    private Token token;

    public Parser(lexScanner scanner){
        this.scanner = scanner;
    }

    public void S(){
        P();
        S1();
    }

    public void S1(){
        token = scanner.proximoToken();
       
        if(token != null){
            Q();
            P();
            S1();
        }
    }

    public void P(){
        token = scanner.proximoToken();
    
        if(token.getType()!=Token.IDENTIFICADOR){
            throw new SintaxeException("Esperava-se ID, foi encontrado "  + Token.Tk_Text[token.getType()] + " (" + token.getTeste() + ") na linha " + token.getLine() + " e coluna " + token.getColumn());
        }
    }

    public void Q(){
    
        if(token.getType() != Token.PONTUACAO){
            throw new SintaxeException("Esperava-se PONTUACAO, foi encontrado " + Token.Tk_Text[token.getType()] + " (" + token.getTeste() + ") na linha " + token.getLine() + " e coluna " + token.getColumn());
        }
    }
}

// S -> SQP | P => S -> PS', S' -> QPS' | Vazio
// P -> id
// Q -> ,|.
