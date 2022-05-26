package linked_list;

public class Node<E> {
	
	/*Instance variables*/
	private E data;
	private Node<E> link;
	
	/**
	 * Parameterized constructor used to initialize a node with specified initial data and a link to the next node.
	 * @param data The initial data of this node.
	 * @param initialLink Reference to the node after this new node.
	 */
	public Node(E data, Node<E> initialLink) {
		this.data = data;
		this.link = initialLink;
	}
	
	/**
	 * Adds a new node after this node.
	 * @param element The data of the new node.
	 * @throws OutOfMemoryError This indicates that there is insufficient memory for a new Node.
	 */
	public void addNodeAfter(E element) {
		this.link = new Node<E>(element, this.link);
	}
	
	/**
	 * Accessor method to get the data of the node.
	 * @return The data of the node.
	 */
	public E getData() {
		return this.data;
	}
	
	/**
	 * Accessor method to get the next node after this node.
	 * @return The next node.
	 */
	public Node<E> getLink() {
		return this.link;
	}
	
	/**
	 * Removes the next node.
	 */
	public void removeNodeAfter() {
		link = link.link;
	}
	
	/**
	 * Setter method to set the data of this node.
	 * @param newData
	 */
	public void setData(E newData) {
		this.data = newData;
	}
	
	/**
	 * Setter method to set the link of this node.
	 * @param newLink
	 */
	public void setLink(Node<E> newLink) {
		link = newLink;
	}
	
	/**
	 * Copies the source given in the parameter.
	 * @param source The head node of the list to copy.
	 * @return The head reference of the copy.
	 */
	public static <E> Node<E> listCopy(Node<E> source) {
		Node<E> copyHead, cursor;
		
		/*Handling special case of empty list*/
		if(source == null) {
			return null;
		}
		
		copyHead = new Node<E>(source.data, null);
		cursor = copyHead;
		
		/*copying the rest of the nodes.*/
		while(source.link != null) {
			source = source.link;
			cursor.addNodeAfter(source.data);
			cursor = cursor.link;
		}
		
		return copyHead;
	}
	
	/**
	 * Print out the values in the list
	 */
	public static <E> void printList(Node<E> source) {
		if (source == null) { 
			System.out.println("Empty Linked List"); 
			return;
		}
		Node<E> cursor = source;
		
		while(cursor != null) {
			System.out.print(cursor.data);
			System.out.print(" -> ");
			cursor = cursor.link;
		}
		System.out.println("END OF LINKED LIST");
	}
}
