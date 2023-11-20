#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <floatobject.h>
#include <string.h>

void print_python_float_info(PyObject *obj) {
    double value;

    setbuf(stdout, NULL);
    printf("[.] float object information\n");

    if (strcmp(obj->ob_type->tp_name, "float") != 0) {
        printf(" [ERROR] Invalid Float Object\n");
        return;
    }

    value = ((PyFloatObject *)obj)->ob_fval;
    printf(" value: %s\n", PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}

void print_python_bytes_info(PyObject *obj) {
    size_t i, size, max_display;
    char *data;

    setbuf(stdout, NULL);
    printf("[.] bytes object information\n");

    if (strcmp(obj->ob_type->tp_name, "bytes") != 0) {
        printf(" [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)obj)->ob_size;
    data = ((PyBytesObject *)obj)->ob_sval;
    max_display = size < 10 ? size : 10;

    printf(" size: %lu\n", size);
    printf(" trying string: %s\n", data);
    printf(" first %lu bytes: ", max_display);

    for (i = 0; i < max_display; i++) {
        printf("%02hhx%s", data[i], i + 1 < max_display ? " " : "");
    }
    printf("\n");
}

void print_python_list_info(PyObject *obj) {
    int i;

    setbuf(stdout, NULL);
    printf("[*] Python list information\n");

    if (strcmp(obj->ob_type->tp_name, "list") != 0) {
        printf(" [ERROR] Invalid List Object\n");
        return;
    }

    printf("[*] Size of the Python List = %lu\n", ((PyVarObject *)obj)->ob_size);
    printf("[*] Allocated = %lu\n", ((PyListObject *)obj)->allocated);

    for (i = 0; i < ((PyVarObject *)obj)->ob_size; i++) {
        PyObject *item = ((PyListObject *)obj)->ob_item[i];

        printf("Element %d: %s\n", i, item->ob_type->tp_name);

        if (strcmp(item->ob_type->tp_name, "bytes") == 0) {
            print_python_bytes_info(item);
        } else if (strcmp(item->ob_type->tp_name, "float") == 0) {
            print_python_float_info(item);
        }
    }
}

int main(void) {
    PyObject *list, *bytes, *float_obj;

    Py_Initialize();

    bytes = PyBytes_FromString("Hello");
    float_obj = PyFloat_FromDouble(3.14);

    list = PyList_New(3);
    PyList_SetItem(list, 0, bytes);
    PyList_SetItem(list, 1, float_obj);
    PyList_SetItem(list, 2, PyLong_FromLong(42));

    print_python_bytes_info(bytes);
    print_python_float_info(float_obj);
    print_python_list_info(list);

    Py_DECREF(bytes);
    Py_DECREF(float_obj);
    Py_DECREF(list);

    Py_Finalize();

    return (0);
}

