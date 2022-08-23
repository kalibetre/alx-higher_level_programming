#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a node in to a sorted list
 * @head: the list
 * @number: the number to be inserted
 *
 * Return: the address of the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *temp = *head, *prev = *head;

	if (head == NULL)
		return (NULL);

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = number;
	node->next = NULL;

	if (*head == NULL)
		*head = node;

	while (temp != NULL && temp->n < number)
	{
		prev = temp;
		temp = temp->next;
	}

	if (prev == temp)
	{
		node->next = temp;
		*head = node;
	}
	else if (temp == NULL)
		prev->next = node;
	else
	{
		prev->next = node;
		node->next = temp;
	}

	return (node);
}
