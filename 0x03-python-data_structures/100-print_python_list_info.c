#include "lists.h"

void print_python_list_info(PyObject *p)
{
	Py_ssize_t len;

	len = PyList_Size(p);

	printf("[*]Size of Python List = %d", len);
}
