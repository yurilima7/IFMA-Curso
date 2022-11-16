package cadastro;

public class Professor extends Pessoa{
    
    private String disciplina;
    private boolean aula;
    private String turno;

    public Professor(String disciplina, String turno, String nome, int idade) {
        super(nome, idade);
        setDisciplina(disciplina);
        setTurno(turno);
    }

    public String getDisciplina() {
        return this.disciplina;
    }

    public void setDisciplina(String disciplina) {
        this.disciplina = disciplina;
    }

    public boolean isAula() {
        return this.aula;
    }

    public void setAula(boolean aula) {
        this.aula = aula;
    }

    public String getTurno() {
        return this.turno;
    }

    public void setTurno(String turno) {
        this.turno = turno;
    }

    public void ministrarAula(boolean aula){
        setAula(aula);
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
        return super.dados() + "\nDISCIPLINA: " + getDisciplina() + 
        " -" + " TURNO: " + getTurno() + "\nEM AULA ? " + isAula() + "\n";
    }
}
