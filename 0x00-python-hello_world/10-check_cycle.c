#include "lists.h"

/**
* check_cycle - Checks if a singly linked list has a cycle.
* @list: Pointer to the head of the linked list.
* Return: 1 if there is a cycle, 0 if not.
*/
int check_cycle(listint_t *list)
{
listint_t *tortoise, *hare;

if (!list || !list->next)
return (0);

tortoise = list;
hare = list;

while (tortoise && hare && hare->next)
{
tortoise = tortoise->next; /* Move one step */
hare = hare->next->next;   /* Move two steps */

if (tortoise == hare)
return (1); /* Cycle detected */
}

return (0); /* No cycle found */
}

