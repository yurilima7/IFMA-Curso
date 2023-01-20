package estruturas;

public class taskVariavel extends taskSimbolo {
	public static final int NUMBER = 0;
	public static final int TEXT = 1;
	
	private int tipo;
	private String valor;
	
	public taskVariavel(String name, int tipo, String valor) {
		super(name);
		this.tipo = tipo;
		this.valor = valor;
	}

	public int getTipo() {
		return tipo;
	}

	public void setTipo(int tipo) {
		this.tipo = tipo;
	}

	public String getValor() {
		return valor;
	}

	public void setValor(String valor) {
		this.valor = valor;
	}

	@Override
	public String toString() {
		return "taskVariavel [name=" + name + ", tipo=" + tipo + ", valor=" + valor + "]";
	}

	
}
