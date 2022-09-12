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
		s = ((PyBytesObject *)p)->ob_sval;

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
 * print_python_float - prints python float
 * @p: PyObject pointer to the float
 */
void print_python_float(PyObject *p)
{
	char *value_str;
	printf("[.] float object info\n");

	if (PyFloat_Check(p))
	{
		value_str = PyOS_double_to_string(PyFloat_AsDouble(p), 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);
		printf("  value: %s\n", value_str);
	}
	else
		printf("  [ERROR] Invalid Float Object\n");
}

/**
 * print_python_list - prints python list
 * @p: PyObject pointer to the list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i = 0;
	PyObject *ele;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_Check(p))
	{
		size = ((PyVarObject *)p)->ob_size;
		allocated = ((PyListObject *)p)->allocated;
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", allocated);

		while (i < size)
		{
			ele = ((PyListObject *)p)->ob_item[i];
			printf("Element %ld: %s\n", i, ((ele)->ob_type)->tp_name);
			if (PyBytes_Check(ele))
				print_python_bytes(ele);
			else if (PyFloat_Check(ele))
				print_python_float(ele);
			i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
