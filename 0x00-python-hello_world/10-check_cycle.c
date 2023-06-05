#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - Function that checks if a singly
 * linked list has a cycle in it
 * @list: Linked list to check
 * Return: 0 if there is no cycle, 1 if there is
 */

int check_cycle(listint_t *list)
{
	listint_t *deffi = list;
	listint_t *effi = list;

	if (list == NULL)
	{
		return (0);
	}

	while (deffi && effi && effi->next)
	{
		deffi = deffi->next;
		effi = effi->next->next;
		if (deffi == effi)
			return (1);
	}
	return (0);
}

