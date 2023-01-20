import 'dart:io';
import 'usuario.dart';

class UsuarioBIN extends Usuario {
  UsuarioBIN(String nome, int idade, String campus, String curso)
      : super(nome, idade, campus, curso);

  @override
  String armazenar() {
    return "Nome: $nome\nIdade: $idade\nCampus: $campus\nCurso: $curso";
  }

  @override
  void criarArquivo(String armazenamento) async {
    final filename = 'Alunos.bin';
    await File(filename).writeAsString(armazenamento);
  }
}
