package pagamentos;

public class Pagamento {
    protected static int totalOperacoes;
    protected static double valorTotal;
    protected static int qtdOperacoesDinheiro;
    protected static int qtdOperacoesCartaoAVista;
    protected static int qtdOperacoesParceladas;

    protected double valorSerPago;
    protected double valorPago;

    public Pagamento(double valorSerPago, double valorPago){
        if(valorSerPago > 0 && valorPago > 0){
            if(valorPago >= valorSerPago){
                totalOperacoes++;
                this.valorSerPago = valorSerPago;
                this.valorPago = valorPago;
                valorTotal = valorTotal + this.valorSerPago;
            }
            else{
                System.out.println("Valor pago abaixo do aceito!");
            }           
        }
        else{
            System.out.println("Valores invalidos!");
        }       
    }


    public void Relatorio(){
        System.out.println("----------------------------------------------------------------------");
        System.out.println("QUANTIDADE DE OPERACOES REGISTRADAS: " + totalOperacoes);
        System.out.printf("VALOR TOTAL RECEBIDO: R$ %.2f\n", valorTotal);
        System.out.println("QUANTIDADE DE OPERACOES EM DINHEIRO: " + qtdOperacoesDinheiro);
        System.out.println("QUANTIDADE DE OPERACOES NO CARTAO A VISTA: " + qtdOperacoesCartaoAVista);
        System.out.println("QUANTIDADE DE OPERACOES NO CARTAO PARCELADAS: " + qtdOperacoesParceladas);
        System.out.println("----------------------------------------------------------------------\n");
    }
}
