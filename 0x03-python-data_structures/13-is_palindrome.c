#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome_rec - check for palindrome recursively
 * @left: left node
 * @right: right node
 *
 * Return: 0 if it is not a palindrome else 1
 */
int is_palindrome_rec(listint_t **left, listint_t *right)
{
	int is_pal;

	if (right == NULL)
		return (1);

	is_pal = is_palindrome_rec(left, right->next);
	if (is_pal == 0)
		return (0);

	is_pal = (*left)->n == right->n;
	*left = (*left)->next;
	return (is_pal);
}

/**
 * is_palindrome - checks if a singly linked list is palindrome
 * @head: the list
 *
 * Return: 0 if it is not a palindrome else 1
 */
int is_palindrome(listint_t **head)
{
	return (is_palindrome_rec(head, *head));
}
