import Lexico.Analisador;
import Lexico.Token;

public class Main {
    public static void main(String args[]) {
        Analisador anaCad = new Analisador("teste.txt");

        Token token = null;

        do {
            token = anaCad.percorreToken();

            if(token != null){
                System.out.println(token);
            }
            
        } while (token != null);
    }
}
