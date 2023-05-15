#include "lists.h"
/**
 * is_palindrome - checks whether a linked list is a palindrome
 * @head: pointer to a pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr = *head;
	listint_t *next = NULL;
	listint_t *prev = NULL, *rev = NULL;

	if (!*head || !((*head)->next))
		return (1);
	while (curr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	rev = prev;
	curr = *head;
	while (rev)
	{
		if (rev->n != curr->n)
			return (0);
		rev = rev->next;
		curr = curr->next;
	}
	return (1);
}
