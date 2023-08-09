#include "lists.h"

/**
* check_cycle - checks if a linked list contains cycle
* @list: linked list to check
* Made by MEGA
* Return: one if the list has a cycle, zero if it doesn't
*/

int check_cycle(listint_t *list)
{
	listint_t *slw = list;
	listint_t *fst = list;

	if(!list)
		return (0);

	while (slw && fst && fst->next)
	{
		slw = slw->next;
		fst = fst->next->next;
		if (slw == fst)
			return (1);
	}
	return (0);
}
