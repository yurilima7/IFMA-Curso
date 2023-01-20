import tv.TV;

public class App {
    public static void main(String[] args) throws Exception {
        TV a = new TV("Azul", "Samsung", "SM23", 40);
        a.estadoTV(true);
        a.aumentarVolume();
        a.sintonizarCanal(10);
        a.diminuirVolume();
        a.diminuirVolume();
        a.aumentarVolume();
        a.mudo(true);
        a.mudo(false);
        a.aumentarVolume();
        a.aumentarVolume();
        a.aumentarVolume();
        a.aumentarVolume();
        a.aumentarVolume();
        a.estadoTV(false);
    }
}
