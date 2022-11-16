// implementação que apresentam dados de algumas figuras geométricas
import geometria.figurasplanas.circulo.Circulo;
import geometria.figurasplanas.quadrilateros.Losango;
import geometria.figurasplanas.quadrilateros.Paralelogramo;
import geometria.figurasplanas.quadrilateros.Quadrado;
import geometria.figurasplanas.quadrilateros.Retangulo;
import geometria.figurasplanas.quadrilateros.Trapezio;
import geometria.figurasplanas.triangulos.Equilatero;
import geometria.figurasplanas.triangulos.Escaleno;
import geometria.figurasplanas.triangulos.Isosceles;

public class Main {

	public static void main(String[] args) {
		
		Quadrado q1 = new Quadrado(5);		
		Retangulo r1 = new Retangulo(5, 3);
		Trapezio t1 = new Trapezio(28, 12, 10, 10);
		Paralelogramo p1 = new Paralelogramo(8, 12);
		Losango l1 = new Losango(3, 3);
		Escaleno te1 = new Escaleno(11, 4, 8, 17);
		Equilatero teq1 = new Equilatero(10);
		Isosceles tiso1 = new Isosceles(10, 12);
		Circulo c1 = new Circulo(3);

		System.out.println("Quadrado");
		q1.apresentaDados();
		System.out.println("Retangulo");
		r1.apresentaDados();
		System.out.println("Trapezio");
		t1.apresentaDados();
		System.out.println("Paralelogramo");
		p1.apresentaDados();
		System.out.println("Losango");
		l1.apresentaDados();
		System.out.println("Triangulo Esccaleno");
		te1.apresentaDados();
		System.out.println("Triangulo Equilatero");
		teq1.apresentaDados();
		System.out.println("Triangulo Isosceles");
		tiso1.apresentaDados();
		System.out.println("Circulo");
		c1.apresentaDados();

	}

}
