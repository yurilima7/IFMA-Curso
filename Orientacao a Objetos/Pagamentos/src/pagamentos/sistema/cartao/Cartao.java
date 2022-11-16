package pagamentos.sistema.cartao;
import pagamentos.Pagamento;

public class Cartao extends Pagamento {
    protected double qtdParcelas;
    
    public Cartao(double valorSerPago, int qtdParcelas){
        super(valorSerPago, valorSerPago);

        if(qtdParcelas > 1 && valorSerPago > 0){
            this.qtdParcelas = qtdParcelas; 
            qtdOperacoesParceladas++;       
        }
        else{
            if(qtdParcelas <= 0){
                System.out.println("Parcelamento inválido!");
                totalOperacoes = totalOperacoes - 1;
                valorTotal = valorTotal - valorSerPago;    
            }
        }
    }

    public Cartao(double valorSerPago){
        this(valorSerPago, 1);

        if(valorSerPago > 0){
            qtdOperacoesCartaoAVista++;
        }
    }

    @Override
    public void Relatorio(){
        if(this.valorSerPago > 0 && this.qtdParcelas > 1){
            System.out.println("----------------------------------------------------------------------");
            System.out.printf("VALOR DAS PARCELAS: R$ %.2f\n", this.valorSerPago / this.qtdParcelas);
        }
        super.Relatorio();
    }
}
