#include <GL/glut.h>

static int rot_terra = 0, rot_lua = 0, rot_marte = 0;

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glPushMatrix();{
         glColor3f(1.0, 1.0, 0.0);
         glutSolidSphere(30.0, 32, 32); /* Estrela */

         glPushMatrix();{
            glRotatef(rot_terra, 0, 1, 0);
            glTranslatef(75, 0, 0);
            glColor3f(0.0, 0.0, 0.5);
            glutSolidSphere(3, 16, 16); /* Terra */

            glRotatef(rot_lua, 0, 1, 0);
            glTranslatef(10, 0, 0);
            glColor3f(0.7, 0.7, 0.7);
            glutSolidSphere(1, 16, 16); /* Lua */
         }
         glPopMatrix();

         glPushMatrix();{
            glRotatef(rot_marte, 0, 1, 0);
            glTranslatef(100, 0, 0);
            glColor3f(0.7, 0.2, 0.3);
            glutSolidSphere(2, 16, 16); /* Marte */
         }
         glPopMatrix();
    }
    glPopMatrix();

    glutSwapBuffers();
}

void reshape(GLsizei w, GLsizei h)
{
   if (h == 0)
      h = 1;

   glViewport(0, 0, w, h);

   GLfloat fAspect = (GLfloat)w / (GLfloat)h;

   glMatrixMode(GL_PROJECTION);
   glLoadIdentity();
   gluPerspective(90, fAspect, 0.1, 500);
   gluLookAt(0.0, 50.0, 125.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
   glMatrixMode(GL_MODELVIEW);
   glLoadIdentity();
}

void keyboard(unsigned char key, int x, int y)
{
   switch (key)
   {
      case 32:
         rot_lua = (rot_lua + 20) % 360;
         rot_terra = (rot_terra + 2) % 360;
         rot_marte = (rot_marte + 1) % 360;
         break;

      case 27:
        exit(0);
        break;

      default:
         break;
   }
   glutPostRedisplay();
}

void init()
{
   glClearColor(0, 0, 0, 0);
   glEnable(GL_DEPTH_TEST);
}

int main(int argc, char **argv)
{
   glutInit(&argc, argv);
   glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
   glutInitWindowSize(800, 600);
   glutCreateWindow(argv[0]);
   glutDisplayFunc(display);
   glutReshapeFunc(reshape);
   glutKeyboardFunc(keyboard);
   init();
   glutMainLoop();
   return 0;
}