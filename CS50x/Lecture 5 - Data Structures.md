- Adding a new value to a array of int
	- Static array allocations - created under stack
		- Need to create a new stack with +1 size to fit new value
	- Dynamic array allocations -  created under heap
		-  realloc allocates new size for the array
		- It also checks if adjacent memory is free - else returns a new address
- Linked Lists
- Initialization
```C
typedef struct node // temp name
{  
	int number;  
	struct node *next; // initialized with temp name, struct node as compiler will not know "node" after 2 lines
}  
node;
```
- Trees
- Hash Table
- Tries
- Abstract Data structures
	- Queues - fifo - enqueue and dequeue
	- Stacks  - lifo - push and pop
	- Dictionaries 