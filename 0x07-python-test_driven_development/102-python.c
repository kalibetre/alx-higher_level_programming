#include <Python.h>
#include <string.h>
#include <stdio.h>
#include <wchar.h>
#include <unicodeobject.h>

/**
 * print_python_string - prints Python strings
 * @p: PyObject pointer to the object
 */
void print_python_string(PyObject *p)
{
	wprintf(L"[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str"))
	{
		wprintf(L"  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		wprintf(L"  type: compact ascii\n");
	else
		wprintf(L"  type: compact unicode object\n");

	wprintf(L"  length: %lu\n", PyUnicode_GET_LENGTH(p));
	wprintf(L"  value: %ls\n", PyUnicode_AS_UNICODE(p));
}
