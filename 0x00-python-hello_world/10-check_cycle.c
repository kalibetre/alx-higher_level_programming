#include "lists.h"

/**
 * check_cycle - checks a list for a cycle
 * @list: the list
 *
 * Return: returns 0 if there is no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *node = list, *prev = list;

	while (node != NULL && node->next != NULL)
	{
		node = node->next;
		prev = list;

		if (node->next == node)
			return (1);

		while (prev != NULL && prev != node && node != NULL)
		{
			if (node->next == prev)
				return (1);
			prev = prev->next;
		}
	}
	return (0);
}
