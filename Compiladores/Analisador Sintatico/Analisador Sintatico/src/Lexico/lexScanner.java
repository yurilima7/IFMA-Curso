package Lexico;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

import Erros.*;

public class lexScanner {
    private char[] conteudo;
    private int estado;
    private int posicao;
    private int line;
    private int column;

    public lexScanner(String fileName){
        try {
            line = 1;
            column = 0;
            String txtConteudo;
            posicao = 0;
            txtConteudo = new String(Files.readAllBytes(Paths.get(fileName)),StandardCharsets.UTF_8);
            System.out.println("......Analisando......");
            System.out.println(txtConteudo);
            System.out.println("...............................");
            conteudo = (txtConteudo + "\0").toCharArray();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public Token proximoToken(){
        
        
        if(isEOF()){
            return null;
        }
        char atualChar;
        Token token;
        String term = "";
        
        estado = 0;

        while(true){
            atualChar = nextChar();
            column++;
            
            switch(estado){
                
                case 0:
                
                    if(isChar(atualChar)){
                        term += atualChar;
                        estado = 1;
                    }
                    else if(isDigit(atualChar)){
                        estado = 0;
                    }
                    else if(isSpace(atualChar)){
                        estado = 0;
                    }
                    else if(isOperador(atualChar)){
                        estado = 0;
                    }
                    else if(isPontuacao(atualChar) || isEOF(atualChar)){
                       
                        term += atualChar;
                        token = new Token();
                        token.setType(Token.PONTUACAO);
                        token.setTeste(term);
                        token.setLine(line);
                        token.setColumn(column - term.length());
                        return token;
                    }
                    else{
                        throw new LexicalException("Caracter nao reconhecido");
                    }
                    break;

                case 1:
                    if(isChar(atualChar)){
                        estado = 1;
                        term += atualChar;
                    }
                    else if(isSpace(atualChar) || isPontuacao(atualChar) || isEOF(atualChar)){
                        if(!isEOF(atualChar)){back();}

                        token = new Token();
                        token.setType(Token.IDENTIFICADOR);
                        token.setTeste(term);
                        token.setLine(line);
                        token.setColumn(column - term.length());
                        return token;
                    }
                    else {
                        throw new LexicalException("Identificador mal formado");
                    }
                    break;
            }
        }
    }

    private char nextChar(){
        if (isEOF()) {
			return '\0';
		}
        return conteudo[posicao++];
    }

    private boolean isChar(char c){
        return (c >= 'a' && c <= 'z')|| (c >= 'A' && c <= 'Z'); 
    }

    private boolean isDigit(char c){
        return (c >= '0' && c <= '9'); 
    }

    private boolean isSpace(char c){
        if(c == '\n' || c == '\r'){line++; column = 0;}

        return (c == ' ' || c == '\n' || c == '\t' || c == '\r'); 
    }

    private boolean isOperador(char c){
        return (c == '>' || c == '<' || c == '+' || c == '-' || c == '*' || c == '/' || c == '=' ); 
    }

    private boolean isPontuacao(char c){
        return (c == '.' || c == ',' );
    }

    private boolean isEOF(char c){
        return (c == '\0') ;
    }

    private boolean isEOF(){
        return posicao >= (conteudo.length);
    }

    private void back(){
        posicao -= 1;
        column -= 1;
    }
}
