package banco;

public interface AcoesBanco {
    
    public void abrirConta(int num, int dig);
    public void fecharConta();
    public void sacar(float valor);
    public void depositar(float valor);
    public void saldo();
}
