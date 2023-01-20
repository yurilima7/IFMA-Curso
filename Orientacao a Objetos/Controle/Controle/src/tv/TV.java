package tv;

public class TV implements Controle{
    protected String cor;
    protected String marca;
    protected String modelo;
    protected int polegadas;
    protected static int volume = 30;
    protected int canal;

    public TV(String cor, String marca, String modelo, int polegadas){
        this.cor = cor;
        this.marca = marca;
        this.modelo = modelo;
        this.polegadas = polegadas;
    }

    @Override
    public void estadoTV(boolean e) {
        if(e == false){
            System.out.println("Delisgando TV...");
         }
         else if(e == true){
             System.out.println("Ligando TV...");
         }
    }


    protected void volume(boolean a) {
        if(volume >= 0 && volume <= 30){
            if(a == true && volume == 30){
                System.out.println("Volume------30");
            }
            else if(a == false && volume <= 30 && volume > 0 ){
                volume = volume - 1; 
                System.out.println("Volume------" + volume);
            }
            else if(a == true && volume < 30 && volume >= 0){
                volume = volume + 1;
                System.out.println("Volume------" + volume);
            }
        }
    }

    @Override
    public void mudo(boolean s) {
        int vA = volume; 
        if(s == true){
            volume = 0;
            System.out.println("Volume------" + volume);
        }
        else if(s == false){
            volume = vA;
            System.out.println("Volume------" + volume);
        }
    }

    @Override
    public void sintonizarCanal(int canal) {
        if(canal > 0){
            System.out.println("Canal " + canal + " Sintonizado");
        }
    }

    @Override
    public void aumentarVolume() {
        volume(true);
    }

    @Override
    public void diminuirVolume() {
        volume(false);       
    }
}
