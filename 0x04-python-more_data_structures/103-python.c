#include <python.h>
#include <stdio.h>

/**
 * print_python_bytes - Function that prints python bytes objects
 * @p: Object of python
 * Return: Nothing
 */

void print_python_bytes(PyObject *p)
{
    char *string;
    long int size, i, limit;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("\t[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)(p))->ob_size;
    string = ((PyBytesObject *)p)->ob_sval;

    printf("\tsize: %ld\n", size);
    printf("\ttrying string: %s\n", string);

    if (size >= 10)
        limit = 10;
    else
        limit = size + 1;

    printf("\tfirst %ld bytes:", limit);

    i = 0;
    while (i < limit)
    {
        if (string[i] >= 0)
            printf(" %02x", string[i]);
        else
            printf(" %02x", 256 + string[i]);

        i++;
    }

    printf("\n");
}

/**
 * print_python_list - Function that prints some python list objects
 * @p: Object of python7
 * Return: Nothing
 */

void print_python_list(PyObject *p)
{
    long int size, i;
    PyListObject *list;
    PyObject *obj;

    size = ((PyVarObject *)(p))->ob_size;
    list = (PyListObject *)p;

    printf("[*] Python list info\n");
    printf("\t[*] Size of the Python List = %ld\n", size);
    printf("\t[*] Allocated = %ld\n", list->allocated);

    i = 0;
    while (i < size)
    {
        obj = ((PyListObject *)p)->ob_item[i];
        printf("\tElement %ld: %s\n", i, ((obj)->ob_type)->tp_name);
        if (PyBytes_Check(obj))
            print_python_bytes(obj);

        i++;
    }
}
