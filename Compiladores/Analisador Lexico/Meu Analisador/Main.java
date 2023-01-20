import Excecoes.ErroLexico;
import Excecoes.ErroSintatico;
import Lexico.Analisador;
import Lexico.Token;
import Sintatico.Parser;

public class Main {
    // public static void main(String args[]) {
    //     Analisador anaCad = new Analisador("teste.txt");

    //     Token token = null;

    //     do {
    //         token = anaCad.percorreToken();

    //         if(token != null){
    //             System.out.println(token);
    //         }
            
    //     } while (token != null);
    // }

    public static void main(String args[]) {
        try { 
            Analisador s = new Analisador("teste.txt");
            Parser p = new Parser(s);
            
            p.S();
            System.out.println("Compilado com sucesso!");
        } catch (ErroLexico e ) {
            System.out.println("Erro lexico " + e.getMessage());
        } catch (ErroSintatico t) {
            System.out.println("Erro sintatico ");
        } catch ( Exception f){
            System.out.println("Erro! " + f);
        }
    }
}
//throw new ErroLexico("Caracter não reconecido");