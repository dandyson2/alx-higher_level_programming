#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
* print_python_string - Function that prints python strings
* @p: The object
* Return: None return
*/

void print_python_string(PyObject *p)
{
PyObject *str, *repr;

printf("[.] string object info\n");

if (!PyUnicode_Check(p))
{
printf("  [ERROR] Invalid String Object\n");
return;
}

if (PyUnicode_IS_COMPACT_ASCII(p))
printf("  type: compact ascii\n");
else
printf("  type: compact unicode object\n");

repr = PyObject_Repr(p);
if (repr == NULL)
{
printf("  [ERROR] Failed to get string representation\n");
return;
}

str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
if (str == NULL)
{
Py_XDECREF(repr);
printf("  [ERROR] Failed to encode string to UTF-8\n");
return;
}

printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
printf("  value: %s\n", PyBytes_AsString(str));

Py_XDECREF(repr);
Py_XDECREF(str);
}
