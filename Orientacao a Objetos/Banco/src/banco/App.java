package banco;

public class App {
    public static void main(String[] args) {
        Conta c = new Conta("Inter", "Anderson", 20, "Masculino");
        c.abrirConta(1343, 2);
        c.depositar(500f);
        c.sacar(560f);
        System.out.println(c.toString());
        c.depositar(2.55f);
        c.saldo();
        c.sacar(233.50f);
        c.saldo();
        c.fecharConta();
    }
}
