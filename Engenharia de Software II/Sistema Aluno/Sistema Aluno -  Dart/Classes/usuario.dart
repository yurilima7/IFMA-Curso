abstract class Usuario {
  String? nome;
  int? idade;
  String? campus;
  String? curso;

  Usuario([this.nome, this.idade, this.campus, this.curso]);

  void template() {
    criarArquivo(armazenar());
  }

  String armazenar();
  void criarArquivo(String armazenamento);

}
