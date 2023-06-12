#include "lists.h"

/**
 * reverse_listint - Function to linked list
 * @head: Ptr to first node
 * Return: Ptr to 1st node
 */

void reverse_listint(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*head = prev;
}

/**
 * is_palindrome - Function that checks if a singly linked
 * list is a palindrome
 * @head: Ptr to linked list
 * Return: 0 if not a palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
int is_palindrome(listint_t **head)
{
listint_t *slow = *head;
listint_t *fast = *head;
listint_t *temp = *head;
listint_t *dup = NULL;

if (*head == NULL || (*head)->next == NULL)
return (1);

while (fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
}

dup = reverse_listint(slow->next);

while (dup && temp)
{
if (temp->n != dup->n)
return (0);

temp = temp->next;
dup = dup->next;
}

return (1);
}
