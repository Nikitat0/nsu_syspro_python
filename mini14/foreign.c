#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>

PyObject *foreign_matrix_power(PyObject *self, PyObject *args) {
    return NULL;
}

static PyMethodDef FputsMethods[] = {
    {"foreign_matrix_power", foreign_matrix_power, METH_VARARGS,
     "Python interface for fputs C library function"},
    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef foreignmodule = {PyModuleDef_HEAD_INIT, "foreign",
                                           NULL, -1, FputsMethods};

PyMODINIT_FUNC PyInit_foreign(void) {
    return PyModule_Create(&foreignmodule);
};
