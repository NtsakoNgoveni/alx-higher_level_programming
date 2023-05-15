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
	listint_t *ahead = NULL, *head2 = NULL;
	listint_t *slow = NULL;
	int len = 0, len2, i = 0;

	if (*head == NULL)
		return (1);

	while (curr)
	{
		len++;
		curr = curr->next;
	}
	len2 =  len / 2;
	curr = *head;

	if (len % 2 != 0)
		len2 += 1;
	for (i = 0; i < len2; i++)
		curr = curr->next;
	i = 0;
	while (i < len2)
	{
		ahead = curr->next;
		curr->next = slow;
		slow = curr;
		curr = ahead;
		i++;
	}
	head2 = slow;

	/*Compare the first half to second half*/
	for (i = 0; i < len2; i++)
	{
		if ((*head)->n != head2->n)
			return (0);

	}
	return (1);
}
