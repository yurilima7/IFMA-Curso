#include <stdlib.h>
#include <GL/glut.h>

static int ano = 0, dia = 0, diaV = 0, anoV = 0;
static int ano3 = 0, dia3 = 0;

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    glPushMatrix(); // Empilhando Matriz
    {
      glColor3f(0.5, 0.5, 0.0); // definindo a cor da estrela
      glutWireSphere(1.0, 20, 16); // tamanho da estrela e seu desenho na tela

      glTranslatef(1.5, 0.0, 0.0); // translação dos pontos para o próximo desenho

      glTranslatef(-1.5, 0.0, 0.0); // voltando em 2 no x os pontos do planeta
      glRotatef(ano, 0.0, 0.0, 1.0); // rotacionando o planeta em relação a estrela
      glTranslatef(1.5, 0.0, 0.0); // caminhando em 2 no x para desenhar o planeta

      glRotatef(dia, 0.0, 1.0, 0.0); // rotação do planeta em relação ao seu eixo

      glColor3f(0.0, 0.0, 0.5); // coloração do planeta
      glutWireSphere(0.2, 10, 8); // tamanho do planeta e seu desenho na tela
        
    }
    glPopMatrix(); // Desempilando a Matriz

    glPushMatrix();{
      glTranslatef(2, 0.0, 0.0); // translação dos pontos para o próximo desenho

      glTranslatef(-2, 0.0, 0.0); // voltando 2 no eixo x 
      glRotatef(anoV, 0.0, 0.0, 1.0); // rotação do planeta 02
      glTranslatef(2, 0.0, 0.0); // caminhando em 2 no eixo x

      glRotatef(diaV, 0.0, 1.0, 0.0); // rotação do planeta 02 em relação ao seu eixo

      glColor3f(0.0, 1.0, 0.5);
      glutWireSphere(0.2, 10, 8);
    }
    glPopMatrix();

    glPushMatrix(); // Empilhando Matriz
    {
      glTranslatef(0.0, 2.6, 0.0); // translação dos pontos para o próximo desenho

      glTranslatef(0.0, -2.6, 0.0);
      glRotatef(ano3, 0.0, 0.0, 1.0);
      glTranslatef(0.0, 2.6, 0.0);

      glRotatef(dia3, 0.0, 1.0, 0.0);

      glColor3f(0.5, 0.5, 0.5);
      glutWireSphere(0.3, 20, 16);  
    }
    glPopMatrix(); // Desempilando a Matriz

   glutSwapBuffers(); 
}

void reshape (int w, int h)
{
   glMatrixMode(GL_PROJECTION); // Especificando que as operações serão feitas na matrix projection
   glLoadIdentity(); // Carregando a matrix identidade

   // Mexendo com a perspectiva
   gluPerspective(60.0, w/(h*1.0), 1.0, 20.0);
   gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);

   glMatrixMode(GL_MODELVIEW); // Especificando que as operações serão feitas na matrix modelview
   glLoadIdentity(); // Carregando a matrix identidade
}

void keyboard (unsigned char key, int x, int y)
{
   switch (key) {
      case 'a':
        dia = (dia + 10) % 360;
        diaV = (diaV + 11) % 360;
        dia3 = (dia3 + 9) % 360;
        glutPostRedisplay(); // Informa que a janela atual deve ser redesenhada
        break;
      case 'd':
        dia = (dia - 10) % 360;
        diaV = (diaV - 11) % 360;
        dia3 = (dia3 - 9) % 360;
        glutPostRedisplay(); // Informa que a janela atual deve ser redesenhada 
        break;
      case 's':
        ano = (ano + 5) % 360;
        anoV = (anoV + 6) % 360;
        ano3 = (ano3 + 4) % 360;
        glutPostRedisplay(); // Informa que a janela atual deve ser redesenhada
        break;
      case 'w':
        ano = (ano - 5) % 360;
        anoV = (anoV - 6) % 360;
        ano3 = (ano3 - 4) % 360;
        glutPostRedisplay(); // Informa que a janela atual deve ser redesenhada
        break;

      case 27:
        exit(0);
        break;

      default:
         break;
   }
}

int main(int argc, char** argv)
{
   glutInit(&argc, argv); // Inicializando a OpenGl
   glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB); // Configurando os modos de exibição
   glutInitWindowSize(500, 500); // Definindo o tamanho da janela em pixels
   glutCreateWindow("Sistema"); // Definindo o nome da janela
   glutDisplayFunc(display); // Especificando a função de rendering (exibe a cena no loop)
   glutReshapeFunc(reshape); // Especificando a função a ser executada quando a janela é redimensionada
   glutKeyboardFunc(keyboard); // Escificando a função que deve ser executada quando a tela for pressionada
   glClearColor(0,0,0,0);
   glutMainLoop();  // Executando o loop de renderização
   return 0;
}