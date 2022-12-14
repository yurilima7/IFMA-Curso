// Generated from taskLang.g4 by ANTLR 4.7.1
package parser;

	import estruturas.taskSimbolo;
	import estruturas.taskTabelaSimbolo;
	import estruturas.taskVariavel;
	import excecoes.ExcecaoSemantica;
	import java.util.ArrayList;

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class taskLangLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, AP=7, FP=8, SC=9, OP=10, 
		ATTR=11, VIR=12, ID=13, NUMBER=14, WS=15;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "AP", "FP", "SC", "OP", 
		"ATTR", "VIR", "ID", "NUMBER", "WS"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'INICIO'", "'FIM$'", "'Numero'", "'Texto'", "'Leia'", "'Escreva'", 
		"'('", "')'", "'$'", null, "'='", "','"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, "AP", "FP", "SC", "OP", "ATTR", 
		"VIR", "ID", "NUMBER", "WS"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


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


	public taskLangLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "taskLang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21k\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b"+
		"\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\7\16V\n\16\f\16\16"+
		"\16Y\13\16\3\17\6\17\\\n\17\r\17\16\17]\3\17\3\17\6\17b\n\17\r\17\16\17"+
		"c\5\17f\n\17\3\20\3\20\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t"+
		"\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21\3\2\7\5\2,-//\61\61\3\2"+
		"c|\5\2\62;C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2n\2\3\3\2\2\2\2\5\3\2\2\2"+
		"\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3"+
		"\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2"+
		"\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2\2\2\5(\3\2\2\2\7-\3\2\2\2\t\64\3\2"+
		"\2\2\13:\3\2\2\2\r?\3\2\2\2\17G\3\2\2\2\21I\3\2\2\2\23K\3\2\2\2\25M\3"+
		"\2\2\2\27O\3\2\2\2\31Q\3\2\2\2\33S\3\2\2\2\35[\3\2\2\2\37g\3\2\2\2!\""+
		"\7K\2\2\"#\7P\2\2#$\7K\2\2$%\7E\2\2%&\7K\2\2&\'\7Q\2\2\'\4\3\2\2\2()\7"+
		"H\2\2)*\7K\2\2*+\7O\2\2+,\7&\2\2,\6\3\2\2\2-.\7P\2\2./\7w\2\2/\60\7o\2"+
		"\2\60\61\7g\2\2\61\62\7t\2\2\62\63\7q\2\2\63\b\3\2\2\2\64\65\7V\2\2\65"+
		"\66\7g\2\2\66\67\7z\2\2\678\7v\2\289\7q\2\29\n\3\2\2\2:;\7N\2\2;<\7g\2"+
		"\2<=\7k\2\2=>\7c\2\2>\f\3\2\2\2?@\7G\2\2@A\7u\2\2AB\7e\2\2BC\7t\2\2CD"+
		"\7g\2\2DE\7x\2\2EF\7c\2\2F\16\3\2\2\2GH\7*\2\2H\20\3\2\2\2IJ\7+\2\2J\22"+
		"\3\2\2\2KL\7&\2\2L\24\3\2\2\2MN\t\2\2\2N\26\3\2\2\2OP\7?\2\2P\30\3\2\2"+
		"\2QR\7.\2\2R\32\3\2\2\2SW\t\3\2\2TV\t\4\2\2UT\3\2\2\2VY\3\2\2\2WU\3\2"+
		"\2\2WX\3\2\2\2X\34\3\2\2\2YW\3\2\2\2Z\\\t\5\2\2[Z\3\2\2\2\\]\3\2\2\2]"+
		"[\3\2\2\2]^\3\2\2\2^e\3\2\2\2_a\7\60\2\2`b\t\5\2\2a`\3\2\2\2bc\3\2\2\2"+
		"ca\3\2\2\2cd\3\2\2\2df\3\2\2\2e_\3\2\2\2ef\3\2\2\2f\36\3\2\2\2gh\t\6\2"+
		"\2hi\3\2\2\2ij\b\20\2\2j \3\2\2\2\b\2UW]ce\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}