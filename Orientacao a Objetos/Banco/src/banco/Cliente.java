package banco;

public abstract class Cliente {
    
    private String nomeCliente;
    private int idade;
    private String sexo;

    public Cliente(String nomeCliente, int idade, String sexo) {
        this.nomeCliente = nomeCliente;
        this.idade = idade;
        this.sexo = sexo;
    }

    public String getNomeCliente() {
        return this.nomeCliente;
    }

    public void setNomeCliente(String nomeCliente) {
        this.nomeCliente = nomeCliente;
    }

    public int getIdade() {
        return this.idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public String getSexo() {
        return this.sexo;
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }

    @Override
    public String toString() {
        return "\nnome do cliente: " + getNomeCliente() +
            "\nidade: " + getIdade()+
            "\nsexo: " + getSexo() + "\n";
    }

}
