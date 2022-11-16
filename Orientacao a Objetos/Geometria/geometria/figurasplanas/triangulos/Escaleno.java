package geometria.figurasplanas.triangulos;
import java.lang.Math;

public class Escaleno extends Triangulo {

    public Escaleno(int ladoA, int ladoB, int ladoC, double anguloC) {
        super(ladoA, ladoB, ladoC);
        this.calculaAltura(anguloC);
    }
    
    protected void calculaAltura(double anguloC){
        double calculo = lados[0] * (Math.sin(anguloC));
        this.altura = (int) calculo;
    }

    @Override
    public int getArea(){
        return this.area = (this.lados[2] * (int) Math.abs(this.altura)) / 2;
    }
}
