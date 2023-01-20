package geometria.figurasplanas.quadrilateros;

public class Retangulo extends Quadrilatero {
		
	public Retangulo(int base, int altura) {
		// construtor da superclasse (classe pai)		
		super(base, altura, base, altura);
		
		this.base = base;
		this.altura = altura;
		
	}
	
	@Override
	public int getArea() {
		return this.base * this.altura; 		
	}
}
