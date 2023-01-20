package cadastro;

public class Vigilante extends Pessoa{
    
    private float altura;
    private boolean trabalhar;
    private String turno;

    public Vigilante(float altura, String turno, String nome, int idade) {
        super(nome, idade);
        setAltura(altura);
        setTurno(turno);
    }

    public float getAltura() {
        return this.altura;
    }

    public void setAltura(float altura) {
        this.altura = altura;
    }

    public boolean isTrabalhar() {
        return this.trabalhar;
    }

    public void setTrabalhar(boolean trabalhar) {
        this.trabalhar = trabalhar;
    }

    public void trabalhando(boolean trabalhar){
        setTrabalhar(trabalhar);
    }

    public String getTurno() {
        return this.turno;
    }

    public void setTurno(String turno) {
        this.turno = turno;
    }

    @Override
    public void fazerAniversario() {
        setIdade(getIdade() + 1);
    }

    @Override
    public String getNome() {
        return this.nome;
    }

    @Override
    public void setNome(String nome) {
        this.nome = nome;
    }

    @Override
    public int getIdade() {
        return this.idade;
    }

    @Override
    public void setIdade(int idade) {
        this.idade = idade;
    }

    public String dados(){
        return super.dados() + "\nALTURA: " + getAltura() + 
        "\nTURNO: " + getTurno() + " -" + " TRABALHANDO ? " + isTrabalhar() + "\n";
    }
}
