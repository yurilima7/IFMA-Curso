package tv;

public interface Controle {
    void estadoTV(boolean e);
    void aumentarVolume();
    void diminuirVolume();
    void mudo(boolean s);
    void sintonizarCanal(int canal);
}
