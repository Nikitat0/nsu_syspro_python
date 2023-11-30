#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>
#define ull unsigned long long

typedef struct {
    double **ptr;
    size_t size;
} Matrix;

Matrix newMatrix(size_t n) {
    Matrix matrix;
    matrix.ptr = calloc(n, sizeof(double *));
    matrix.size = n;
    for (size_t i = 0; i < n; i++)
        matrix.ptr[i] = calloc(n, sizeof(double));
    return matrix;
}

Matrix newIdentityMatrix(size_t n) {
    Matrix matrix = newMatrix(n);
    for (size_t i = 0; i < n; i++)
        matrix.ptr[i][i] = 1;
    return matrix;
}

void freeMatrix(Matrix *matrix) {
    for (size_t i = 0; i < matrix->size; i++)
        free(matrix->ptr[i]);
    free(matrix->ptr);
}

Matrix pow_matrix(Matrix *matrix, size_t pow) {
    Matrix result;
    size_t n = matrix->size;
    result = newIdentityMatrix(n);
    for (size_t h = 0; h < pow; h++) {
        Matrix temp = newMatrix(n);
        for (size_t i = 0; i < n; i++) {
            for (size_t j = 0; j < n; j++) {
                double v = 0;
                for (size_t k = 0; k < n; k++) {
                    v += matrix->ptr[i][k] * result.ptr[k][j];
                }
                temp.ptr[i][j] = v;
            }
        }
        freeMatrix(&result);
        result = temp;
    }
    return result;
}

int convert_matrix(PyObject *obj, void *addr) {
    Matrix *matrix = addr;
    size_t n = PyList_Size(obj);

    *matrix = newMatrix(n);
    for (size_t i = 0; i < n; i++) {
        PyObject *row = PyList_GetItem(obj, i);
        for (size_t j = 0; j < matrix->size; j++)
            matrix->ptr[i][j] = PyFloat_AsDouble(PyList_GetItem(row, j));
    }

    return 1;
}

PyObject *pythonizeMatrix(Matrix *src) {
    size_t n = src->size;
    PyObject *matrix = PyList_New(n);
    for (size_t i = 0; i < n; i++) {
        PyObject *row = PyList_New(n);
        for (size_t j = 0; j < n; j++)
            PyList_SetItem(row, j, PyFloat_FromDouble(src->ptr[i][j]));
        PyList_SetItem(matrix, i, row);
    }
    return matrix;
}

PyObject *foreign_matrix_power(PyObject *self, PyObject *args) {
    Matrix matrix;
    size_t pow;
    if (!PyArg_ParseTuple(args, "O&n", convert_matrix, &matrix, &pow))
        return NULL;
    Matrix result = pow_matrix(&matrix, pow);
    PyObject *python_result = pythonizeMatrix(&result);
    freeMatrix(&matrix);
    freeMatrix(&result);
    return python_result;
}

static PyMethodDef FputsMethods[] = {
    {"foreign_matrix_power", foreign_matrix_power, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef foreignmodule = {PyModuleDef_HEAD_INIT, "foreign",
                                           NULL, -1, FputsMethods};

PyMODINIT_FUNC PyInit_foreign(void) {
    return PyModule_Create(&foreignmodule);
};
