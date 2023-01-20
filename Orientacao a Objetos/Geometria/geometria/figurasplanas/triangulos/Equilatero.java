package geometria.figurasplanas.triangulos;
import java.lang.Math;

public class Equilatero extends Triangulo {

    public Equilatero(int lado){
        super(lado, lado, lado);
    }

    protected void calculaAltura(int lado){
        this.altura = (lado * (int) (Math.sqrt(3))) / 2;
    }

   @Override
    public int getArea(){
        double rq = (Math.sqrt(3));
        double pt = Math.pow(this.lados[0], 2);
        double resultado = (pt * rq) / 4;
        return this.area = (int) resultado;
    }

}
