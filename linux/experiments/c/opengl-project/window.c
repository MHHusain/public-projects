#include <stdio.h>
#include <GL/glut.h>

void myInit();
void myDraw();

int main(int argc, char *argv[])
{

	/* Initialize window system */
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(250, 250);
	glutCreateWindow("Hello World");

	/* Initialize graphics */
	myInit();

	/* Display callback and enter event loop */
	glutDisplayFunc(myDraw);
	glutMainLoop();
	return 0;
}

/*set up viewing*/
void myInit()
{
	/* Background color */
	glClearColor(255.0, 255.0, 255.0, 0.5);

	/* Projection */
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-2.0, 2.0, -2.0, 2.0, -2.0, 2.0);
}

void myDraw()
{
	/* Clear the screen */
	glClearColor(0.0, 0.0, 0.0, 1.0);
	glClear(GL_COLOR_BUFFER_BIT);

	/* Example code to draw 3 white points /
	/* Draw your points here **/
	glColor3f(1.0, 1.0, 1.0);
	glBegin(GL_POLYGON);
	glVertex3f(0.25, 0.25, 0.0);
	glVertex3f(0.75, 0.25, 0.0);
	glVertex3f(0.75, 0.75, 0.0);

	glEnd();

	/* Execute draw commands */
	glFlush();
}
