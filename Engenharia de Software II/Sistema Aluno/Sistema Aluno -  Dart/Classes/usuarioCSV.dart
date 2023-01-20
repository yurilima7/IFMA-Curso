import 'dart:io';
import 'usuario.dart';

class UsuarioCSV extends Usuario {
  UsuarioCSV(String nome, int idade, String campus, String curso)
      : super(nome, idade, campus, curso);

  @override
  String armazenar() {
    return "Nome: $nome\nIdade: $idade\nCampus: $campus\nCurso: $curso";
  }

  @override
  void criarArquivo(String armazenamento) async {
    final filename = 'Alunos.csv';
    await File(filename).writeAsString(armazenamento);
  }
}