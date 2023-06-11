#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - function that prints some basic
 * info about python list
 * @p: Object of python
 */

void print_python_list_info(PyObject *p)
{
    Py_ssize_t size = PyList_Size(p);
    PyListObject *listObj = (PyListObject *)p;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", listObj->allocated);

    for (Py_ssize_t i = 0; i < size; i++)
	{
        PyObject *item = listObj->ob_item[i];
        const char *typeName = Py_TYPE(item)->tp_name;
        printf("Element %zd: %s\n", i, typeName);
	}
}
