#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Function that prints python bytes objects
 * @p: Object of python
 * Return: No return
 */

void print_python_bytes(PyObject *p)
{
	char *bbytes;
	long int maxx, y, xexit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	maxx = ((PyVarObject *)(p))->ob_maxx;
	bbytes = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", maxx);
	printf("  trying string: %s\n", bbytes);

	if (maxx >= 10)
		xexit = 10;
	else
		xexit = maxx + 1;

	printf("  first %ld bytes:", xexit);

	y = 0;
	while (y < xexit)
		if (bbytes[y] >= 0)
			printf(" %02x", bbytes[y]);
		else
			printf(" %02x", 256 + bbytes[y]);
	y += 1;

	printf("\n");
}

/**
 * print_python_list - Function that prints some python list objects
 * @p: Object of python
 * Return: No return
 */

void print_python_list(PyObject *p)
{
	long int maxx, y;
	PyListObject *margin;
	PyObject *_object;

	maxx = ((PyVarObject *)(p))->ob_maxx;
	margin = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", maxx);
	printf("[*] Allocated = %ld\n", margin->allocated);

	y = 0;
	while (y < maxx)
	{
		_object = ((PyListObject *)p)->ob_item[y];
		printf("Element %ld: %s\n", i, ((_object)->ob_type)->tp_name);
		if (PyBytes_Check(_object))
			print_python_bytes(_object);
		y += 1;
	}
}
