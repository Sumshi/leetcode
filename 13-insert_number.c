#include "lists.h"
#include<stdlib.h>
#include<stdio.h>
#include <stddef.h>
/**
 * listint_t *insert_node - inserts a number in list
 * @number: number to insert
 * @head: pointer to the head of linked list
 * Return: address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;/*stores new created node*/
	listint_t *current;/*for traversing the list*/

	new = malloc(sizeof(listint_t));/*allocates memory for new node*/
	if (new == NULL)
		return (NULL);/*memory allocation failed*/
	new->n = number;/*stores the number*/
	new->next = NULL;/*there is no node after it*/
	/*linked list is empty or number to insert is less than num current node*/
	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;/*next pointer is set to current head*/
		*head = new;
		return (new);
	}
	current = *head;/*traverses linked list till position to insert*/
	while (current->next != NULL && current->next->n < number)
		current = current->next;

	new->next = current->next;/*new node is inserted*/
	current->next = new;

	return (new);
}
