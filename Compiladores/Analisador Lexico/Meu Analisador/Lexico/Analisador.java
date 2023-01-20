package Lexico;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

import Excecoes.ErroLexico;

public class Analisador{
    char[] conteudo;
    private int estado;
    private int posicao;
    private String text = "";
   
    public Analisador(String fileName){
        try {
            String txtConteudo;
            posicao = 0;
            txtConteudo = new String(Files.readAllBytes(Paths.get(fileName)),StandardCharsets.UTF_8);
            // System.out.println("......Analisando a cadeia......");
            // System.out.println(txtConteudo);
            // System.out.println("...............................");
            this.conteudo = (txtConteudo + "\0").toCharArray();
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public Token percorreToken(){

        if(seEOF()){
            return null;
        }

        char caracterAtual;
        this.text = "";
        this.estado = 0;

        while(true){
            caracterAtual = nextChar();
            // System.out.println("caracter " + caracterAtual);
            // System.out.println("estado " + estado);
            // System.out.println("posicao " + posicao);
            // System.out.println("-----------------");

            switch(estado){
    
                case 0:
                    text += caracterAtual;
                    if(seCharABC(caracterAtual)){
                        if(caracterAtual == 'a'){
                            estado = 1;
                        }
                    }
                    else if(seChar(caracterAtual)){
                        throw new ErroLexico("Simbolo nao reconhecido");
                    }
                    else if(seNumero(caracterAtual)){
                        throw new ErroLexico("Simbolo nao reconhecido");
                    }
                    else if(seEspaco(caracterAtual)){
                        text = "";
                        break;
                    }
                    else if(seEOF(caracterAtual)){
                       
                        //System.out.println("caracter eof " + caracterAtual);
                        text = "";
                        throw new ErroLexico("Simbolo nao reconhecido");          
                      
                    }
                    else{
                        throw new ErroLexico("Simbolo nao reconhecido");
                    }
                    break;

                case 1:
                    if(seCharABC(caracterAtual)){
                        text += caracterAtual;
                        if(caracterAtual == 'a'){
                            estado = 2;
                        }
                        else if(caracterAtual == 'b'){
                            estado = 3;
                        }
                        else{
                            throw new ErroLexico("Simbolo nao reconhecido");
                        }
                    }
                    else{
                        throw new ErroLexico("Simbolo nao reconhecido");
                    }
                    break;

                case 2: // estado de salvação
                    if(seEspaco(caracterAtual) || seEOF(caracterAtual)){
                        Token token = new Token();
                        token.setTipo(Token.CADEIA);
                        token.setValor(text);
                        return token;
                    }
                

                case 3:
                    if(seCharABC(caracterAtual)){
                        text += caracterAtual;
                        if(caracterAtual == 'c'){
                            estado = 4;
                        }
                        else{
                            throw new ErroLexico("Simbolo nao reconhecido");
                        }
                    }
                    else{
                        throw new ErroLexico("Simbolo nao reconhecido");
                    }
                    break;

                case 4:
                    if(seCharABC(caracterAtual)){
                        text += caracterAtual;
                        if(caracterAtual == 'b'){
                            estado = 3;
                        }
                        else if(caracterAtual == 'a'){
                            estado = 2;
                        }
                        else{
                            throw new ErroLexico("Simbolo nao reconhecido");
                        }
                    }
                    else{
                        throw new ErroLexico("Simbolo nao reconhecido");
                    }
                    break;
            }
        }
    }

    private char nextChar(){
        if(seEOF()){
            return '\0';
        }
        return conteudo[posicao++];
    }

    private boolean seEOF(){
        return posicao >= conteudo.length;
    }

    private boolean seCharABC(char c){
        return (c == 'a' || c == 'b' || c == 'c');
    }

    private boolean seChar(char c){
        return ((c >= 'd' && c <= 'z') || (c >= 'A' && c <= 'Z'));
    }

    // private void voltar(){
    //     posicao--;
    // }

    private boolean seNumero(char c){
        return (c >= '0' && c <= '9');
    }

    private boolean seEspaco(char c){
        return (c == ' ' || c == '\n' || c == '\t' || c == '\r'); 
    }

    private boolean seEOF(char c){
        return (c == '\0') ;
    }
}