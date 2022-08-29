#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i = 0;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);

	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %ld\n", allocated);

	while (i < size)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		i++;
	}
}
