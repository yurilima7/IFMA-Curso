import '../Classes/usuarioBIN.dart';
import '../Classes/usuarioCSV.dart';
import '../Classes/usuarioDOC.dart';
import '../Classes/usuarioTXT.dart';

void main(List<String> args) {
  UsuarioTXT a1 = new UsuarioTXT("François", 25, "IFMA - CAXIAS", "CC");
  a1.template();

  UsuarioCSV a2 = new UsuarioCSV("Santana", 22, "IFMA - CAXIAS", "CC");
  a2.template();

  UsuarioDOC a3 = new UsuarioDOC("Santos", 20, "IFMA - CAXIAS", "CC");
  a3.template();

  UsuarioBIN a4 = new UsuarioBIN("Luiza", 20, "IFMA - CAXIAS", "CC");
  a4.template();
}
