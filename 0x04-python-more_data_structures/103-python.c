#include <Python.h>

/**
 * print_python_bytes - prints bytes of python object
 * @p: PyObject pointer to the object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, n, i = 0;
	char *s;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		size = PyBytes_Size(p);
		s = PyBytes_AsString(p);

		printf("  size: %ld\n", size);
		printf("  trying string: %s\n", s);

		n = size < 10 ? size + 1 : 10; 
		printf("  first %ld bytes:", n);
		while (i < n)
		{
			printf(" %02x", s[i]);
			i++;
		}
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

/**
 * print_python_list - prints python list
 * @p: PyObject pointer to the list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i = 0;
	PyObject *ele;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	while (i < size)
	{
		ele = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((ele)->ob_type)->tp_name);
		if (PyBytes_Check(ele))
			print_python_bytes(ele);
		i++;
	}
}
