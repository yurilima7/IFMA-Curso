package banco;

public class Conta extends Cliente implements AcoesBanco{
    
    private int conta;
    private int digito;
    private String nomeBanco;
    private float saldo;
    private boolean aberta;

    public Conta(String nomeBanco, String nomeCliente, int idade, String sexo) {
        super(nomeCliente, idade, sexo);
        this.nomeBanco = nomeBanco;
        this.aberta = false;
    }

    private int getConta() {
        return this.conta;
    }

    private void setConta(int conta) {
        this.conta = conta;
    }

    private int getDigito() {
        return this.digito;
    }

    private void setDigito(int digito) {
        this.digito = digito;
    }

    private String getNomeBanco() {
        return this.nomeBanco;
    }

    protected void setNomeBanco(String nomeBanco) {
        this.nomeBanco = nomeBanco;
    }

    private float getSaldo() {
        return this.saldo;
    }

    private void setSaldo(float saldo) {
        this.saldo = saldo;
    }

    private boolean isAberta() {
        return this.aberta;
    }

    private void setAberta(boolean aberta) {
        this.aberta = aberta;
    }

    @Override
    public void abrirConta(int num, int dig) {
        if (isAberta()) {
            System.out.println("Conta ja esta aberta!");
        } 
        else {
            setAberta(true);
            setConta(num);
            setDigito(dig);
            System.out.println("Conta aberta com sucesso!");
            setSaldo(0f);
        }
    }

    @Override
    public void fecharConta() {
        if (isAberta() == false) {
            System.out.println("Impossivel encerrar conta que nao esta aberta!");
        } 
        else {
            if (getSaldo() == 0f) {
                setAberta(false);
                System.out.println("Conta encerrada com sucesso!");
            } 
            else if(getSaldo() < 0f) {
                System.out.println("Impossivel encerrar conta, pois cliente esta em debito com o banco!");
            } 
            else {
                System.out.println("Impossivel encerrar conta, pois ha saldo na mesma!");
            }
        }
    }

    @Override
    public void sacar(float valor) {
        if (isAberta() == false) {
            System.out.println("Impossivel sacar pois conta nao existe!");
        } 
        else {
            if (getSaldo() > 0f && getSaldo() >= valor) {
                setSaldo(getSaldo() -  valor);
                System.out.println("Saque feito com sucesso!");
            } 
            else if (getSaldo() > 0f && getSaldo() <= valor) {
                System.out.println("Impossivel sacar! Saldo insuficiente!");
            }
            else{
                System.out.println("Impossivel sacar!");
            }
        }
    }

    @Override
    public void depositar(float valor) {
        if (isAberta() == false) {
            System.out.println("Impossivel sacar pois conta nao existe!");
        } 
        else {
            setSaldo(getSaldo() + valor);
            System.out.println("Deposito feito com sucesso!");
        }
    }

    @Override
    public void saldo() {
        if (isAberta()) {
            System.out.println("Saldo da conta = " + getSaldo());
        } 
        else {
            System.out.println("Erro! Conta nao existe!");
        }
    }

    @Override
    public String toString() {
        return "\nSOBRE A CONTA: " +
            "\nnumero da conta com digito: " + getConta() + "-" + getDigito() +
            "\nnome do banco: " + getNomeBanco() + super.toString();
    }

}
