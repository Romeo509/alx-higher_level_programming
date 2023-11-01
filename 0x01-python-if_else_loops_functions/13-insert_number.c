#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
listint_t *current = *head;
    listint_t *new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return NULL;

    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL || number < (*head)->n)
    {
        new_node->next = *head;
        *head = new_node;
        return new_node;
    }

    while (current->next != NULL && current->next->n <= number)
    {
        current = current->next;
    }

    new_node->next = current->next;
    current->next = new_node;

    return new_node;
}

