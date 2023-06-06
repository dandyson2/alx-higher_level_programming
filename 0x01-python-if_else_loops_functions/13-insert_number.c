#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Function that insert a number
 * into a sorted singly linked list
 * @head: Ptr to the head of the linked lists
 * @number: Number for insertion
 * Return: The address of the new node, NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *node = *head;
listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));

if (new_node == NULL)
return (NULL);

new_node->n = number;

if (node == NULL || node->n >= number)
{
new_node->next = node;
*head = new_node;

return (new_node);
}

while (node && node->next && node->next->n < number)

node = node->next;

new_node->next = node->next;
node->next = new_node;

return (new_node);
}
