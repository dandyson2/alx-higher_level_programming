#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Function that prints python bytes objects
 * @p: Object of python
 * Return: No return
 */

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    char *string = bytes->ob_sval;
    long int size = ((PyVarObject *)p)->ob_size;
    long int limit;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n")
		;
        return;
    }

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    limit = (size >= 10) ? 10 : size + 1;
    printf("  first %ld bytes:", limit);

    for (long int i = 0; i < limit; i++)
    {
        unsigned char byte = (unsigned char)string[i];
        printf(" %02x", byte);
    }

    printf("\n");
}

/**
 * print_python_list - Function that prints some python list objects
 * @p: Object of python
 * Return: No return
 */

void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    long int size = PyList_Size(p);
    PyObject *obj;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (long int i = 0; i < size; i++)
    {
        obj = list->ob_item[i];
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
        if (PyBytes_Check(obj))
            print_python_bytes(obj);
    }
}
