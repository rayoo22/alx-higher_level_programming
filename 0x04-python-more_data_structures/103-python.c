#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python - print basic info about python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int size, alloc, i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObjectb *)p;

	size = var->ob_size;
	aloc = list->allocated;

	printf("[*] Pyhton list info\n");
	printf("[*] Size of the python list = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for(i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if(strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]
	}
}
