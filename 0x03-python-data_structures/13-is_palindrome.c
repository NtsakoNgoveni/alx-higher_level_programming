#include "lists.h"
/**
 * is_palindrome - checks whether a linked list is a palindrome
 * @head: pointer to a pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */

listint_t *reverse(listint_t **head)
{
	listint_t *curr = *head, *next = NULL, *prev = NULL;

	while (curr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	*head = prev;
	return (prev);
}

int is_palindrome(listint_t **head)
{
	listint_t *curr = *head, *head2 = *head;
	int len = 0, i;

	if (*head == NULL)
		return (1);
	while (curr)
	{
		len++;
		curr = curr->next;
	}
	curr = *head;
	len = len / 2;
	if (len % 2 != 0)
		len ++;

	for (i = 0; i < len; i++)
		head2 = head2->next;
	head2 = reverse(&head2);

	for (i = 0; i < len; i++)
	{
		if (curr->n != head2->n)
			return (0);
	}
	return (1);
}

