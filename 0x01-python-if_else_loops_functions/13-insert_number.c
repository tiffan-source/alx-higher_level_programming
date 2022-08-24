#include "lists.h"

/**
 * create_node - create a node
 * @number: number to insert to node
 *
 * Return: node create
 */

listint_t *create_node(int number)
{
	listint_t *new_node = NULL;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	return (new_node);
}

/**
 * insert_node - insert node in order list
 * @head: adress of list head
 * @number: number to insert
 *
 * Return: new node add or NULL if fail to create node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *save;

	if (head == NULL)
		return (NULL);

	save = *head;

	if (save == NULL)
		return (add_nodeint_end(head, number));

	if (save->n >= number)
	{
		new_node = create_node(number);

		if (new_node == NULL)
			return (NULL);

		new_node->next = save;
		*head = new_node;

		return (new_node);
	}

	while (save->next != NULL)
	{
		if (number <= save->next->n)
		{
			new_node = create_node(number);

			if (new_node == NULL)
				return (NULL);

			new_node->next = save->next;
			save->next = new_node;
			return (new_node);
		}
		save = save->next;
	}

	return (add_nodeint_end(head, number));
}
