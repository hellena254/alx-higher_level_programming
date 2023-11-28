#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: a pointer to the head of the linked list
 * Return: 1 if there's a cycle and 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	tortoise = list;
	hare = list;

	while (tortoise != NULL && hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
			return (1);
	}

	return (0);
}
