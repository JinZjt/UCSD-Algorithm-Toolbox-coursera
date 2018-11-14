#include "bstdb.h"
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define N 100
// Write your submission in this file
//
// A main function and some profiling tools have already been set up to test
// your code in the task2.c file. All you need to do is fill out this file
// with an appropriate Binary Search Tree implementation.
//
// The input data will be books. A book is comprised of a title and a word
// count. You should store both these values in the tree along with a unique
// integer ID which you will generate.
//
// We are aiming for speed here. A BST based database should be orders of
// magnitude faster than a linked list implementation if the BST is written
// correctly.
//
// We have provided an example implementation of what a linked list based
// solution to this problem might look like in the db/listdb.c file. If you
// are struggling to understand the problem or what one of the functions
// below ought to do, consider looking at that file to see if it helps your
// understanding.
//
// There are 6 functions you need to look at. Each is provided with a comment
// which explains how it should behave. The functions are:
//
//  + bstdb_init
//  + bstdb_add
//  + bstdb_get_word_count
//  + bstdb_get_name
//  + bstdb_stat
//  + bstdb_quit
//
// Do not rename these functions or change their arguments/return types.
// Otherwise the profiler will not be able to find them. If you think you
// need more functionality than what is provided by these 6 functions, you
// may write additional functions in this file.

typedef struct node{
	int doc_id;
	char* name;
	int word_count;
	struct node* left;
	struct node* right;
}tree_node;

typedef struct node{
	int a[N];
	int stack_top;
}stack;

stack* initialization(){
	stack* ret;
	ret = (stack*)malloc(sizeof(stack));
	if(ret){
		ret->stack_top = 0;
	}
	return ret;
}

void createstack(stack* s, int id){
	int num = id;
	s->a[s->stack_top] = num;
	s->stack_top++;
	while(num>=0){
		if(s->stack_top>=N) {printf("stack overflow\n"); return;}
		else if((num-1)%2==0) {
			num = (num-1)/2;
			s->a[s->stack_top] = num;
			s->stack_top++;
		}
		else if((num-1)%2!=0){
			num = (num-2)/2;
			s->a[s->stack_top] = num;
			s->stack_top++;
		}
	}
	return;
}

int               g_next_id;     // ID of the next document to be added
tree_node* g_linked_list; 		 // database storage
int g_num_comps;
int g_num_searches;
bstdb_init ( void ) {
	// This function will run once (and only once) when the database first
	// starts. Use it to allocate any memory you want to use or initialize 
	// some globals if you need to. Function should return 1 if initialization
	// was successful and 0 if something went wrong.
	g_linked_list = NULL;
	g_next_id = 0;
	g_num_comps = 0;
	g_num_searches = 0;
	return 1;
}

void tree_delete(tree_node* root){
    if(root!=NULL){
        tree_delete(root->left);
        tree_delete(root->right);
        free(root);
    }
    else return;
}

int
bstdb_add ( char *name, int word_count ) {
	// This function should create a new node in the binary search tree, 
	// populate it with the name and word_count of the arguments and store
	// the result in the tree.
	//
	// This function should also generate and return an identifier that is
	// unique to this document. A user can find the stored data by passing
	// this ID to one of the two search functions below.
	//
	// How you generate this ID is up to you, but it must be an integer. Note
	// that this ID should also form the keys of the nodes in your BST, so
	// try to generate them in a way that will result in a balanced tree.
	//
	// If something goes wrong and the data cannot be stored, this function
	// should return -1. Otherwise it should return the ID of the new node
	tree_node* p;
	tree_node* parent;
	int length = 0, index = 0;
	length = strlen(name);
	p = (tree_node*)malloc(sizeof(tree_node));
	parent = (tree_node*)malloc(sizeof(tree_node));
	if(!g_linked_list){
		g_linked_list->doc_id = 0;
		g_linked_list->name = (char*)malloc(sizeof(char)*length);
		strcpy(g_linked_list->name, name);
		g_linked_list->word_count = word_count;
		g_linked_list->left = NULL;
		g_linked_list->right = NULL;
		return 0;
	}
	else{
		parent = g_linked_list;
		p->name = (char*)malloc(sizeof(char));// store new node information
		strcpy(p->name, name);
		p->word_count = word_count;
		p->left = NULL;
		p->right = NULL;
		while(1){
			if(p->word_count>=parent->word_count && parent->right!=NULL) {
				index = 2*index+2;
				parent = parent->right;
			}
			else if(p->word_count<parent->word_count && parent->left!=NULL){
				index = 2*index+1;
				parent = parent->left;
			}
			else if(p->word_count>=parent->word_count && parent->right==NULL){
				index = 2*index+2;
				p->doc_id = index;
				parent->right = p;
				return index; // index is the new ID
			}
			else if(p->word_count<parent->word_count && parent->left==NULL){
				index = 2*index+1;
				p->doc_id = index;
				parent->left = p;
				return index; //index is the new ID
			}
		}
	}
	return -1;
}

int
bstdb_get_word_count ( int doc_id ) {
	// This is a search function. It should traverse the binary search tree
	// and return the word_count of the node with the corresponding doc_id.
	//
	// If the required node is not found, this function should return -1
	stack* s;
	int temp_id;
	tree_node* p;
	s = initialization();
	p = (tree_node*)malloc(sizeof(tree_node));
	p = g_linked_list;
	createstack(s, doc_id);
	s->stack_top = s->stack_top-1;
	while(s->stack_top>0){
		s->stack_top--;
		temp_id = s->a[s->stack_top];
		if(temp_id%2!=0&&p->left!=NULL) p=p->left;
		else if(temp_id%2==0&&p->right!=NULL) p = p->right;
		else if(temp_id%2!=0&&p->left==NULL) {printf("not found"); return -1;}
		else if(temp_id%2==0&&p->right==NULL) {printf("not found"); return -1;}
	}
	if(p->doc_id==doc_id) return p->word_count;
	else return -1;
}

char*
bstdb_get_name ( int doc_id ) {
	// This is a search function. It should traverse the binary search tree
	// and return the name of the node with the corresponding doc_id.
	//
	// If the required node is not found, this function should return NULL or 0
	stack* s;
	int temp_id;
	tree_node* p;
	s = initialization();
	p = (tree_node*)malloc(sizeof(tree_node));
	p = g_linked_list;
	createstack(s, doc_id);
	s->stack_top = s->stack_top-1;
	while(s->stack_top>0){
		s->stack_top--;
		temp_id = s->a[s->stack_top];
		if(temp_id%2!=0&&p->left!=NULL) p=p->left;
		else if(temp_id%2==0&&p->right!=NULL) p = p->right;
		else if(temp_id%2!=0&&p->left==NULL) {printf("not found"); return 0;}
		else if(temp_id%2==0&&p->right==NULL) {printf("not found"); return 0;}
	}
	if(p->doc_id==doc_id) return p->name;
	else return NULL;
}

void
bstdb_stat ( void ) {
	// Use this function to show off! It will be called once after the 
	// profiler ends. The profiler checks for execution time and simple errors,
	// but you should use this function to demonstrate your own innovation.
	//
	// Suggestions for things you might want to demonstrate are given below,
	// but in general what you choose to show here is up to you. This function
	// counts for marks so make sure it does something interesting or useful.
	//
	//  + Check if your tree is balanced and print the result
	//
	//  + Does the number of nodes in the tree match the number you expect
	//    based on the number of insertions you performed?
	//
	//  + How many nodes on average did you need to traverse in order to find
	//    a search result? 
	//
	//  + Can you prove that there are no accidental duplicate document IDs
	//    in the tree?
}

void
bstdb_quit ( void ) {
	// This function will run once (and only once) when the program ends. Use
	// it to free any memory you allocated in the course of operating the
	// database.
	tree_delete(g_linked_list);
	return;
}
