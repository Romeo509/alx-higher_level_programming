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
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
string = PyBytes_AsString(p);

printf("  size: %ld\n", size);
printf("  trying string: %s\n", string);

limit = (size > 10) ? 10 : size;

printf("  first %ld bytes:", limit);

for (i = 0; i < limit; i++)
printf(" %02x", string[i]);

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

size = PyList_Size(p);

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
for (i = 0; i < size; i++)
{
obj = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);

if (PyBytes_Check(obj))
print_python_bytes(obj);
}
}

