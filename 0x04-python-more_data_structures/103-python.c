#include <stdio.h>
#include <Python.h>

/**
* print_python_bytes - Prints bytes information
*
* @p: Python Bytes Object
* Return: No return
*/
void print_python_bytes(PyObject *p)
{
char *string;
long int size, i, limit;

printf("[.] bytes object info\n");
if (!PyObject_HasAttrString(p, "decode") || !PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyObject_Size(p);
string = PyUnicode_DecodeUTF8(PyBytes_AsString(p), size, "strict");
if (string == NULL)
{
printf("  [ERROR] Decode failed\n");
return;
}

printf("  size: %ld\n", size);
printf("  trying string: %s\n", string);

limit = (size > 10) ? 10 : size;
printf("  first %ld bytes:", limit);

for (i = 0; i < limit; i++)
printf(" %02x", string[i] & 0xff);

printf("\n");
}

/**
* print_python_list - Prints list information
*
* @p: Python List Object
* Return: No return
*/
void print_python_list(PyObject *p)
{
long int size, i;
PyObject *obj;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", PyObject_Size(p));
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
for (i = 0; i < PyObject_Size(p); i++)
{
obj = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);

if (PyObject_HasAttrString(obj, "decode") && PyBytes_Check(obj))
print_python_bytes(obj);
}
}
