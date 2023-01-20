package xopay;

public class Especial extends Banco{

    private static int diasRendimento = 30;
    private static double rendimentoEspecialMensal = 0.3;
    private static double valorInicial = 1000;

    private int aberturaConta;

    public Especial(String nome, int aberturaConta, double deposito) throws Exception{
        super(nome);
        if(deposito < valorInicial){
            throw new Exception();
        } else
        {
            this.aberturaConta = aberturaConta;
            this.deposito(deposito);
            Banco.setControladorDias(aberturaConta);
        }
    }

    public int getAberturaConta() {
        return this.aberturaConta;
    }

    public void setAberturaConta(int aberturaConta) {
        this.aberturaConta = aberturaConta;
    }

    @Override
    public double taxadeJuros() {
        double taxaJuros = rendimentoEspecialMensal / (double)diasRendimento;
        return taxaJuros;
    }

    @Override
    public void tempodeExistenciaConta(){
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
    public void rendimento() {
        double rendimento = this.getSaldo() * Math.pow(1 + this.taxadeJuros(), this.tempo()) - this.getSaldo();
        this.setSaldo(this.getSaldo() + rendimento);
    }

    @Override
    public String DadosConta() {
        return "\nDados da Conta: \n" + 
        "Cliente: " + this.getNome() + 
        "\nSaldo: " + this.getSaldo() + 
        "\nDia de abertura da Conta: " + this.aberturaConta;
    }
}
