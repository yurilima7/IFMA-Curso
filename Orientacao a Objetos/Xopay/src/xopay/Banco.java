package xopay;

public abstract class Banco {
    
    protected static int existenciaBanco = 0;
    protected static int controladorDias;

    private String nome;
    private double saldo;

    public Banco(String nome) {
        this.setNome(nome);
    }

    public String getNome() {
        return this.nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getSaldo() {
        return this.saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }    

    public void Saque(double saque){
        this.setSaldo(this.getSaldo() - saque);
    }

    public static void setControladorDias(int aberturaConta){
        if(controladorDias < aberturaConta)
        {
            Banco.controladorDias = aberturaConta;
        }  
    }

    public static int getControladorDias(){
        return Banco.controladorDias;
    }

    public void deposito(double valor){
        this.setSaldo(getSaldo() + valor);
    }

    public static void dia(int novoDia){
        Banco.setControladorDias(novoDia);;
    }

    public abstract void rendimento();
    public abstract double taxadeJuros();
    public abstract void tempodeExistenciaConta();
    public abstract int tempo();
    public abstract String DadosConta();
}
