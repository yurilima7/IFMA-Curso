package xopay;

public class App {
    public static void main(String[] args){

        Banco c1 = null, c2 = null;

        try {
            c1 = new Especial("Arnaldo", 2, 1000);
            c2 = new Especial("Janaina", 4, 1500);
        } catch (Exception e) {
            System.out.println("Nao é possivel abrir conta especial com valor abaixo de R$ 1000");
        }

        c1.rendimento();
        c1.deposito(200);

        c1.rendimento();
        c2.rendimento();

        Classica c3 = new Classica("Jake", 6);
        Classica c4 = new Classica("Laura", 6);

        c3.deposito(100);
        c4.deposito(2100);
        c4.rendimento();
        c3.rendimento();
        c1.rendimento();
        c2.rendimento();

        c1.Saque(200);
        c4.Saque(100);
        c3.tempodeExistenciaConta();

        Banco.dia(7);

        c1.rendimento();
        c2.rendimento();
        c3.rendimento();
        c4.rendimento();

        System.out.println(c1.DadosConta());
        System.out.println(c2.DadosConta());
        System.out.println(c3.DadosConta());
        System.out.println(c4.DadosConta());
    }
}
