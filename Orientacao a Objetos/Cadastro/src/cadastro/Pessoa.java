package cadastro;

public abstract class Pessoa {
    
    protected String nome;
    protected int idade;

    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public abstract String getNome();

    public abstract void setNome(String nome);

    public abstract int getIdade();

    public abstract void setIdade(int idade);

    public abstract void fazerAniversario();

    public String dados(){
        return "---DADOS CADASTRADOS---\n" + 
        "NOME: " + getNome() + "\nIDADE: " + 
        getIdade();
    }
}
