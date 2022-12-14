#include "lists.h"

/**
 * fill_revert_list - fill a list with another in reverse
 * @dst: destination list
 * @src: source list
 *
 */

void fill_revert_list(listint_t **dst, listint_t *src)
{
	if (src->next != NULL)
		fill_revert_list(dst, src->next);

	add_nodeint_end(dst, src->n);
}

/**
 * is_palindrome - check if list is a palindrome
 * @head: list to check
 *
 * Return: 1 if is a palindrome 0 else
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp_lst = NULL, *save, *sav1;

	if (head == NULL || *head == NULL)
		return (0);

	fill_revert_list(&tmp_lst, *head);

	save = *head;
	sav1 = tmp_lst;

	while (save != NULL)
	{
		if (save->n != sav1->n)
		{
			free_listint(tmp_lst);
			return (0);
		}
		save = save->next;
		sav1 = sav1->next;
	}

	free_listint(tmp_lst);

	return (1);
}
