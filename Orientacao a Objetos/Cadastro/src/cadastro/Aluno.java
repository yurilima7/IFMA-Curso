package cadastro;

public class Aluno extends Pessoa{
    
    private int matricula;
    private int turma;
    private String turno;

    public Aluno(String nome, int idade) {
        super(nome, idade);
    }

    public int getMatricula() {
        return this.matricula;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }

    public int getTurma() {
        return this.turma;
    }

    public void setTurma(int turma) {
        this.turma = turma;
    }

    public String getTurno() {
        return this.turno;
    }

    public void setTurno(String turno) {
        this.turno = turno;
    }

    public void fazerMatricula(int matricula, int turma, String turno){
        setMatricula(matricula);
        setTurma(turma);
        setTurno(turno);
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
        return super.dados() + "\nMATRICULA: " + getMatricula() + 
        "\nTURMA: " + getTurma() + " -" + " TURNO: " + getTurno() + "\n";
    }
}
