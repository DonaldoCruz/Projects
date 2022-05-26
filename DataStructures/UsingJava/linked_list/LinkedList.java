package linked_list;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class LinkedList<E> implements Iterator<E> {
	
	/*Declaring instance variables*/
	private Node<E> head, tail, current;
	private int nodeCount;
	
	/**
	 * Default constructor
	 */
	public LinkedList() {
		this.head = null;
		this.tail = head;
		this.current = head;
		nodeCount = 0;
	}
	
	/**
	 * Adds a node to this linked list.
	 * @param element The data of the node to be added.
	 */
	public void add(E element) {
		
		if(this.head == null) {
			this.head = new Node<E>(element, null);
			this.tail = head;
			this.current = head;
		}
		else {
			tail.setLink(new Node<E>(element, null));
			tail = tail.getLink();
			// this.head.addNodeAfter(element); //Not using this method of adding a node to the linked list because it doesn't add the nodes in-order.
		}
		nodeCount++;
	}
	
	/**
	 * Removes the node with the specified data
	 * @param target The specified data to look for.
	 * @return true if the target was found and removed.
	 */
	public boolean remove(E target) {
		Node<E> cursor = this.head;
		Node<E> theLink = cursor.getLink();
		
		if(cursor != null && cursor.getData().equals(target)) {
			this.head = this.head.getLink();
			return true;
		}
		
		while(theLink != null) {
			if(theLink.getData().equals(target)) {
				cursor.removeNodeAfter();
				return true;
			}
			cursor = theLink;
			theLink = cursor.getLink();
		}
		return false;
	}
	
	/**
	 * Clears the entire linked list.
	 */
	public void clear() {
		this.head = null;
		this.nodeCount = 0;
	}
	
	/**
	 * This function return true if a linked list is empty.
	 * @return True if the head of a linked list is null.
	 */
	public boolean empty() {
		return head == null;
	}
	
	/**
	 * Print out the nodes in this linked list.
	 */
	public void printLinkedList() {
		Node.printList(head);
	}
	
	/**
	 * This function gives the number of nodes in this linked list.
	 * @return The number of nodes in linked list.
	 */
	public int length() {
		return nodeCount;
	}

	/**
	 * This function overrides the hasNext method of the Iterator Interface
	 * @return True if node exists.
	 */
	public boolean hasNext() {
		return current != null;
	}

	/**
	 * This function returns the data of the current node.
	 * @return The data contained in the current node.
	 */
	public E next() {
		E answer;

		if (!hasNext())
			throw new NoSuchElementException("The linked list is empty");
		
		answer = current.getData();
		current = current.getLink();

		return answer;
	}



}
