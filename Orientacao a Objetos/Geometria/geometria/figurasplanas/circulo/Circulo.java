package geometria.figurasplanas.circulo;

import geometria.figurasplanas.Poligono;

public class Circulo extends Poligono{
    public Circulo(int raio){
        this.raio = raio;
    }

    @Override
    public int getPerimetro(){
        double p = 2 * Math.PI * this.raio;
        return (int) p;
    }

    public int getDiametro(){
        return 2 * this.raio;
    }

    @Override
    public int getArea(){
        double a = Math.PI * Math.pow((double) this.raio, 2);
        return (int) a;
    }

    @Override
    public void apresentaDados(){
        System.out.println("Diametro: " + this.getDiametro());
        super.apresentaDados();
    }
}
