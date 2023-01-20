package geometria.figurasplanas.quadrilateros;
import geometria.figurasplanas.Poligono;

public abstract class Quadrilatero extends Poligono{
	protected int base;
	protected int altura;

	public Quadrilatero(int lado1, int lado2, int lado3, int lado4) {
		
		this.lados = new int[4];
		this.lados[0] = lado1;
		this.lados[1] = lado2;
		this.lados[2] = lado3;
		this.lados[3] = lado4;
	}	
}
