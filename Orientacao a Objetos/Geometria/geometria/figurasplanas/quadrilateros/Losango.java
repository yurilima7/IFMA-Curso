package geometria.figurasplanas.quadrilateros;
import java.lang.Math;

public class Losango extends Paralelogramo {
    protected int diagonalMaior;
    protected int diagonalMenor;

    public Losango(int ladosAC, int ladosBD){
        super(ladosAC, ladosBD);
        this.calculaDiagonalMaior(ladosBD);
        this.calculaDiagonalMenor(ladosAC);
    }

    protected void calculaDiagonalMaior(int ladosBD){
        int BDq = (int) (Math.pow(ladosBD, 2) + Math.pow(ladosBD, 2)) - (2 * ladosBD * ladosBD * (int) Math.cos(120));
        this.diagonalMaior = (int) (Math.sqrt(BDq));
    }

    protected void calculaDiagonalMenor(int ladosAC){
        int ACq = (int) (Math.pow(ladosAC, 2) + Math.pow(ladosAC, 2)) - (2 * ladosAC * ladosAC * (int) Math.cos(60));
        this.diagonalMenor = (int) (Math.sqrt(ACq));
    }

    @Override
    public int getArea(){
        return (this.diagonalMaior * this.diagonalMenor) / 2;
    }

}
