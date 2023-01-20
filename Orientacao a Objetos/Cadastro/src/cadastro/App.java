package cadastro;

public class App {
    public static void main(String[] args) {
        
        Aluno alu = new Aluno("Sara", 19);
        alu.fazerMatricula(001, 01, "vespertino");
        System.out.println(alu.dados());


        Professor pro = new Professor("POO", "Matutino", "Francisco", 34);
        pro.ministrarAula(true);
        System.out.println(pro.dados());


        Vigilante vig = new Vigilante(1.76f, "Tarde", "Sandro", 30);
        vig.trabalhando(false);
        System.out.println(vig.dados());

        alu.fazerAniversario();
        pro.fazerAniversario();

        System.out.println(alu.dados());
        System.out.println(pro.dados());

    }
}
