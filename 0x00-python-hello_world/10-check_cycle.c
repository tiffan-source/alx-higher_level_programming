#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list to check
 *
 * Return: 1 if detect cycle 0 else
 */

int check_cycle(listint_t *list)
{
	listint_t *save, *i_save;
	int i = 0, j;

	if (list == NULL)
		return (0);

	save = list->next;

	while (save)
	{
		i++;
		for (i_save = list, j = 0; j < i; i_save = i_save->next, j++)
			if (i_save == save)
				return (1);
		save = save->next;
	}

	return (0);
}
