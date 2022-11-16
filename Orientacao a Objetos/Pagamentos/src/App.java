// implementação que simula situações de pagamentos

import pagamentos.sistema.cartao.Cartao;
import pagamentos.sistema.especie.Especie;

public class App {
    public static void main(String[] args) throws Exception {
        Especie p1 = new Especie(100, 130.5);
        System.out.println("Pagamento 1:");
        p1.Relatorio();

        System.out.println("Pagamento 2:");
        Especie p2 = new Especie(50.5, 51);
        p2.Relatorio();

        System.out.println("Pagamento 3:");
        Cartao p3 = new Cartao(250);
        p3.Relatorio();

        System.out.println("Pagamento 4:");
        Cartao p4 = new Cartao(100, 2);
        p4.Relatorio();

        System.out.println("Pagamento 5:");
        Cartao p5 = new Cartao(-250);
        p5.Relatorio();

        System.out.println("Pagamento 6:");
        Cartao p6 = new Cartao(-100, 2);
        p6.Relatorio();

        System.out.println("Pagamento 7:");
        Cartao p7 = new Cartao(100, -2);
        p7.Relatorio();

        Especie p8 = new Especie(-100, 130.5);
        System.out.println("Pagamento 8:");
        p8.Relatorio();

        Especie p9 = new Especie(100, 30.5);
        System.out.println("Pagamento 9:");
        p9.Relatorio();
        
        Cartao p10 = new Cartao(145, 200);
        System.out.println("Pagamento 10:");
        p10.Relatorio();
    }
}
