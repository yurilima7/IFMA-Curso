// Generated from taskLang.g4 by ANTLR 4.7.1
package parser;

	import estruturas.taskSimbolo;
	import estruturas.taskTabelaSimbolo;
	import estruturas.taskVariavel;
	import excecoes.ExcecaoSemantica;
	import java.util.ArrayList;

import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link taskLangParser}.
 */
public interface taskLangListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link taskLangParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(taskLangParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link taskLangParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(taskLangParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link taskLangParser#decl}.
	 * @param ctx the parse tree
	 */
	void enterDecl(taskLangParser.DeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link taskLangParser#decl}.
	 * @param ctx the parse tree
	 */
	void exitDecl(taskLangParser.DeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link taskLangParser#declaravar}.
	 * @param ctx the parse tree
	 */
	void enterDeclaravar(taskLangParser.DeclaravarContext ctx);
	/**
	 * Exit a parse tree produced by {@link taskLangParser#declaravar}.
	 * @param ctx the parse tree
	 */
	void exitDeclaravar(taskLangParser.DeclaravarContext ctx);
	/**
	 * Enter a parse tree produced by {@link taskLangParser#tipo}.
	 * @param ctx the parse tree
	 */
	void enterTipo(taskLangParser.TipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link taskLangParser#tipo}.
	 * @param ctx the parse tree
	 */
	void exitTipo(taskLangParser.TipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link taskLangParser#bloco}.
	 * @param ctx the parse tree
	 */
	void enterBloco(taskLangParser.BlocoContext ctx);
	/**
	 * Exit a parse tree produced by {@link taskLangParser#bloco}.
	 * @param ctx the parse tree
	 */
	void exitBloco(taskLangParser.BlocoContext ctx);
	/**
	 * Enter a parse tree produced by {@link taskLangParser#cmd}.
	 * @param ctx the parse tree
	 */
	void enterCmd(taskLangParser.CmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link taskLangParser#cmd}.
	 * @param ctx the parse tree
	 */
	void exitCmd(taskLangParser.CmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link taskLangParser#cmdleitura}.
	 * @param ctx the parse tree
	 */
	void enterCmdleitura(taskLangParser.CmdleituraContext ctx);
	/**
	 * Exit a parse tree produced by {@link taskLangParser#cmdleitura}.
	 * @param ctx the parse tree
	 */
	void exitCmdleitura(taskLangParser.CmdleituraContext ctx);
	/**
	 * Enter a parse tree produced by {@link taskLangParser#cmdescrita}.
	 * @param ctx the parse tree
	 */
	void enterCmdescrita(taskLangParser.CmdescritaContext ctx);
	/**
	 * Exit a parse tree produced by {@link taskLangParser#cmdescrita}.
	 * @param ctx the parse tree
	 */
	void exitCmdescrita(taskLangParser.CmdescritaContext ctx);
	/**
	 * Enter a parse tree produced by {@link taskLangParser#cmdattrib}.
	 * @param ctx the parse tree
	 */
	void enterCmdattrib(taskLangParser.CmdattribContext ctx);
	/**
	 * Exit a parse tree produced by {@link taskLangParser#cmdattrib}.
	 * @param ctx the parse tree
	 */
	void exitCmdattrib(taskLangParser.CmdattribContext ctx);
	/**
	 * Enter a parse tree produced by {@link taskLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(taskLangParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link taskLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(taskLangParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link taskLangParser#termo}.
	 * @param ctx the parse tree
	 */
	void enterTermo(taskLangParser.TermoContext ctx);
	/**
	 * Exit a parse tree produced by {@link taskLangParser#termo}.
	 * @param ctx the parse tree
	 */
	void exitTermo(taskLangParser.TermoContext ctx);
}