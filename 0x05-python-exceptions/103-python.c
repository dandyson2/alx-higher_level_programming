#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
* print_python_list - Function that prints some
* basic info about python list
* @p: A PyListObject
*/

void print_python_list(PyObject *p)
{
Py_ssize_t size, alloc, i;
const char *type;
PyListObject *list = (PyListObject *)p;
PyVarObject *var = (PyVarObject *)p;

size = var->ob_size;
alloc = list->allocated;

fflush(stdout);

printf("[*] Python list info\n");
if (strcmp(p->ob_type->tp_name, "list") != 0)
{
printf("  [ERROR] Invalid List Object\n");
return;
}

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", alloc);

i = 0;
while (i < size)
{
type = list->ob_item[i]->ob_type->tp_name;
printf("Element %ld: %s\n", i, type);
if (strcmp(type, "bytes") == 0)
print_python_bytes(list->ob_item[i]);
else if (strcmp(type, "float") == 0)
print_python_float(list->ob_item[i]);

i++;
}
}

/**
* print_python_bytes - Function that prints some
* basic info about python bytes
* @p: A PyBytesObject
*/

void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
PyBytesObject *bytes = (PyBytesObject *)p;

fflush(stdout);

printf("[.] bytes object info\n");
if (strcmp(p->ob_type->tp_name, "bytes") != 0)
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
printf("  trying string: %s\n", bytes->ob_sval);

if (((PyVarObject *)p)->ob_size >= 10)
size = 10;
else
size = ((PyVarObject *)p)->ob_size + 1;

printf("  first %ld bytes: ", size);

i = 0;
while (i < size)
{
printf("%02hhx", bytes->ob_sval[i]);
if (i == (size - 1))
printf("\n");
else
printf(" ");

i++;
}
}

/**
* print_python_float - Function that print some
* basic info about python float
* @p: A PyFloatObject
*/

void print_python_float(PyObject *p)
{
PyFloatObject *float_obj = (PyFloatObject *)p;

fflush(stdout);

printf("[.] float object info\n");
if (strcmp(p->ob_type->tp_name, "float") != 0)
{
printf("  [ERROR] Invalid Float Object\n");
return;
}

printf("  value: %s\n", PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL));
}
