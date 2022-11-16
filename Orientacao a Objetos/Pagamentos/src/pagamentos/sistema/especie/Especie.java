package pagamentos.sistema.especie;
import pagamentos.Pagamento;

public class Especie extends Pagamento {

    public Especie(double valorSerPago, double valorPago){
        super(valorSerPago, valorPago);

        if(valorSerPago > 0 && valorPago >= valorSerPago){
            qtdOperacoesDinheiro++;
        }
    }

    @Override
    public void Relatorio(){
        if(this.valorSerPago > 0 && this.valorPago >= this.valorSerPago){
            System.out.println("----------------------------------------------------------------------");
            System.out.printf("TROCO: R$ %.2f\n", this.valorPago - this.valorSerPago);
        }
        super.Relatorio();
    }
}
