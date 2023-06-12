#include "lists.h"

/**
 * reverse_listint - Function that reverses a linked list
 * @head: Ptr to first node in list
 * Return: Ptr to first node in new line
 */

void reverse_listint(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;

for (; current; current = next)
{
	next = current->next;
	current->next = prev;
	prev = current;
}

*head = prev;
}

/**
 * is_palindrome - Function that checks if a singly linked
 * list is a palindrome
 * @head: Ptr to linked list
 * Return: 0 if it is a palindrome, 1 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

while (1)
{
	fast = fast->next->next;

    switch (fast)
    {
	    case NULL:
		dup = slow->next;
	    break;

	case NULL:
	    dup = slow->next->next;
	    break;

	default:

	    slow = slow->next;
	    break;
    }

    if (dup != NULL)
	    break;
}

reverse_listint(&dup);

while (dup && temp)
{
	if (temp->n == dup->n)
    {
	    dup = dup->next;
	temp = temp->next;
    }
    else
	    return (0);
}

if (!dup)
	return (1);

return (0);
}
