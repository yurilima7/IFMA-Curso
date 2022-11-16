package geometria.figurasplanas.quadrilateros;
import java.lang.Math;

public class Trapezio extends Quadrilatero {

    public Trapezio(int baseMaior, int baseMenor, int lado1, int lado2){
        super(baseMaior, baseMenor, lado1, lado2);
        this.altura(baseMaior, baseMenor, lado1);
    }

    protected void altura(int baseMaior, int baseMenor, int lado1){
        int x = (baseMaior - baseMenor) / 2;
        int h = (int) (Math.pow(lado1, 2) - Math.pow(x, 2));
        this.altura = (int) (Math.sqrt(h));
    }

    @Override
    public int getArea(){
        return ((this.lados[0] + this.lados[1]) * this.altura) / 2;
    }
}
