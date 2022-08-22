#include "lists.h"

/**
 * check_cycle - checks a list for a cycle
 * using the floyd's cycle finding algorithm
 * @list: the list
 *
 * Return: returns 0 if there is no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *fast_p = list, *slow_p = list;

	while (fast_p != NULL && fast_p->next != NULL)
	{
		fast_p = fast_p->next->next;
		slow_p = slow_p->next;

		if (fast_p == slow_p)
			return (1);
	}
	return (0);
}
