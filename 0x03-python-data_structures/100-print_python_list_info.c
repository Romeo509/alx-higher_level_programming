#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic information about a Python list
 * @p: Pointer to a Python list object
 */
void print_python_list_info(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size, allocated, i;
    PyListObject *listobj;

    size = PyList_Size(p);
    allocated = list->allocated;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (i = 0; i < size; i++)
    {
        listobj = (PyListObject *)PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(listobj)->tp_name);
    }
}

