package geometria.figurasplanas;

public abstract class Poligono implements Interface{

	protected int[] lados;
	protected int raio;

	@Override
	public int getPerimetro() {	
		int soma = 0;
		
		for(int i = 0; i < this.lados.length; i++) {
			soma += this.lados[i];
		}
		
		return soma;		
	}
	
	@Override
	public abstract int getArea();
	
	@Override
	public void apresentaDados(){
		System.out.println("Area: " + this.getArea());
        System.out.println("Perimetro: " + this.getPerimetro());
        System.out.println("----------------------------------------");
	}
}
