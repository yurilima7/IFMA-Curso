package Excecoes;

public class ErroSintatico extends RuntimeException{
    public ErroSintatico(String msg){
        super(msg);
    }
}
