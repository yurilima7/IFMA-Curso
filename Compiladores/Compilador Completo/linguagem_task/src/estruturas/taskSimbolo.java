package estruturas;

public abstract class taskSimbolo {
	protected String name;
	
	public taskSimbolo(String name) {
		this.name = name;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	@Override
	public String toString() {
		return "taskSimbolo [name=" + name + "]";
	}
}
