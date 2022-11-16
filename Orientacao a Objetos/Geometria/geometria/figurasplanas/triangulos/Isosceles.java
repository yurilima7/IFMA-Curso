package geometria.figurasplanas.triangulos;

public class Isosceles extends Triangulo {

    public Isosceles(int ladosAB, int baseC){
        super(ladosAB, ladosAB, baseC);
    }

    protected void calculaAltura(){
        double calculo = Math.pow(this.lados[0], 2) - Math.pow((this.lados[2] / 2), 2);
        double alt = Math.sqrt(calculo);
        this.altura = (int) alt;
    }

    @Override
    public int getArea(){
        this.calculaAltura();
        return this.altura = (this.lados[2] * this.altura) / 2;
    }
}
