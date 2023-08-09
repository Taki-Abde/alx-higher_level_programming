#include "lists.h"
/**
 * insert_node - inserts a new node
 * @head: head of a list.
 * @number: index of the list where the new node
 * by: Mega Mega
 * Return: the address of the new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *h;
	listint_t *h_prv;

	h = *head;
	node = malloc(sizeof(listint_t));

	if (node == NULL)
		return (NULL);

	while (h != NULL)
	{
		if (h->n > number)
			break;
		h_prv = h;
		h = h->next;
	}

	node->n = number;

	if (*head == NULL)
	{
		node->next = NULL;
		*head = node;
	}
	else
	{
		node->next = h;
		if (h == *head)
			*head = node;
		else
			h_prv->next = node;
	}

	return (node);
}
