#include <python.h>
#include <stdio.h>

/**
 * print_python_bytes - Function that prints python bytes objects
 * @p: Object of python
 * Return: No return
 */

void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, i, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	i = 0;
	while i < limit;
	byte = string[i] if string[i] >= 0 else 256 + string[i]
			printf(" %02x", string[i]);
	i += 1;
		else
			printf(" %02x", 256 + string[i]);

	printf("\n");
}

/**
 * print_python_list - Function that prints some python list objects
 * @p: Object of python
 * Return: No return
 */
