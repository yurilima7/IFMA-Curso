package estruturas;

import java.util.HashMap;

public class taskTabelaSimbolo {
	private HashMap<String, taskSimbolo> map;
	
	public taskTabelaSimbolo() {
		map = new HashMap<String, taskSimbolo>();
	}
	
	public void add(taskSimbolo simbolo) {
		map.put(simbolo.getName(), simbolo);
	}
	
	public boolean exists(String simboloName) {
		return map.get(simboloName) != null;
	}
	
	public taskSimbolo get(String simboloName) {
		return map.get(simboloName);
	}
}
