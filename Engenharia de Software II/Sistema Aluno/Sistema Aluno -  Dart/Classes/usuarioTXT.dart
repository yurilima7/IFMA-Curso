import 'dart:io';
import 'usuario.dart';

class UsuarioTXT extends Usuario {
  UsuarioTXT(String nome, int idade, String campus, String curso)
      : super(nome, idade, campus, curso);

  @override
  String armazenar() {
    return "Nome: $nome\nIdade: $idade\nCampus: $campus\nCurso: $curso";
  }

  @override
  void criarArquivo(String armazenamento) async {
    final filename = 'Alunos.txt';
    await File(filename).writeAsString(armazenamento);
  }
}
