package xopay;

public class Classica extends Banco{

    private static int diasRendimento = 30;
    private static double rendimentoClassico = 0.1;
    private static double rendimentoClassicoSuperior = 0.2;

    private int aberturaConta;

    public Classica(String nome, int aberturaConta) {
        super(nome);
        this.aberturaConta = aberturaConta;
        Banco.setControladorDias(aberturaConta);
    }

    public int getAberturaConta() {
        return this.aberturaConta;
    }

    public void setAberturaConta(int aberturaConta) {
        this.aberturaConta = aberturaConta;
    }

    @Override
    public void tempodeExistenciaConta() {
        int existencia = Banco.controladorDias - this.getAberturaConta();
        if(existencia == 0){
            System.out.println("\nConta aberta hoje \n");
        } else
        {
            System.out.println("\nConta existe ha: " + existencia + " dias\n");
        }
    }

    @Override
    public int tempo(){
        int diasParaRendimento = Banco.controladorDias - this.getAberturaConta();
        return diasParaRendimento;
    }

    @Override
    public double taxadeJuros() {

        double taxadeJuros;
        if(this.getSaldo() <= 2000){
            taxadeJuros = rendimentoClassico / (double)diasRendimento;
        } else
        {
            taxadeJuros = rendimentoClassicoSuperior / (double)diasRendimento;
        }
        return taxadeJuros;
    }

    @Override
    public void rendimento() {

        double rendimento;
        if(this.getSaldo() <= 2000){
            rendimento = this.getSaldo() * Math.pow(1 + this.taxadeJuros(), this.tempo()) - this.getSaldo();
            this.setSaldo(this.getSaldo() + rendimento);        
        } else
        {
            double diferenca = this.getSaldo() - 2000;
            rendimento = diferenca * Math.pow(1 + this.taxadeJuros(), this.tempo()) - diferenca;
            this.setSaldo(this.getSaldo() + rendimento);
        }
    }

    @Override
    public String DadosConta(){
        return "\nDados da Conta: \n" + 
        "Cliente: " + this.getNome() + 
        "\nSaldo: " + this.getSaldo() + 
        "\nDia de abertura da Conta: " + this.aberturaConta;
    }
}
