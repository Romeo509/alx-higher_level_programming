#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <string.h>

/**
 * print_python_bytes - Prints info about a Python bytes object
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)(p))->ob_size;
    str = ((PyBytesObject *)(p))->ob_sval;

    if (size >= 10)
        size = 10;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %ld bytes: ", size + 1);
    for (i = 0; i <= size; i++)
    {
        printf("%02x", str[i] & 0xff);
        if (i == size)
            printf("\n");
        else
            printf(" ");
    }
}

/**
 * print_python_list - Prints info about a Python list
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *element;

    printf("[*] Python list info\n");

    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = ((PyVarObject *)(p))->ob_size;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        element = ((PyListObject *)p)->ob_item[i];
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
        if (PyBytes_Check(element))
            print_python_bytes(element);
    }
}


