#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is palindrome
 * @head: the list
 *
 * Return: 0 if it is not a palindrome else 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *rev_list = NULL, *temp, *temp_rev, *node;
	size_t list_size = 0, i = 0;

	if (head == NULL || *head == NULL)
		return (1);

	temp = *head;
	while (temp != NULL)
	{
		node = malloc(sizeof(listint_t));
		if (node == NULL)
			return (1);
		node->n = temp->n;
		if (rev_list == NULL)
			node->next = NULL;
		else
			node->next = rev_list;
		rev_list = node;
		list_size++;
		temp = temp->next;
	}
	temp = *head;
	temp_rev = rev_list;
	while (i < list_size / 2)
	{
		if (temp_rev->n != temp->n)
			return (0);
		temp_rev = temp_rev->next;
		temp = temp->next;
		i++;
	}
	free_listint(rev_list);
	return (1);
}
