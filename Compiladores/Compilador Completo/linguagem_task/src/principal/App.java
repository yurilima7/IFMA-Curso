package principal;

import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;

import excecoes.ExcecaoSemantica;
import parser.taskLangLexer;
import parser.taskLangParser;

public class App {
	public static void main(String[] args) throws Exception {
        try {
        	taskLangLexer lexer;
        	taskLangParser parser;
        	
        	//ler o arquivo input.task que é a entrada para o Analisador lexico
        	lexer = new taskLangLexer(CharStreams.fromFileName("Input.task"));
        	
        	// cria um fluxo de tokens para passar para o PARSER
        	CommonTokenStream tokenStream = new CommonTokenStream(lexer);
        	
        	// cria meu parser a partir desse tokenStream
        	parser = new taskLangParser(tokenStream);
        	
        	parser.prog();
        	System.out.println("Compilado com sucesso!");
        }
        catch(ExcecaoSemantica t) {
        	System.err.println("Erro semantico " + t.getMessage());
        }
        catch(Exception ex) {
        	System.err.println("ERROR " + ex.getMessage());
        }
    }
}
