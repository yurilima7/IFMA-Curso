package geometria.figurasplanas.triangulos;
import geometria.figurasplanas.Poligono;

public abstract class Triangulo extends Poligono{
    protected int altura;
    protected int area;

    public Triangulo(int lado1, int lado2, int lado3){
        this.lados =  new int[3];
        this.lados[0] = lado1;
        this.lados[1] = lado2;
        this.lados[2] = lado3;
    }
}
