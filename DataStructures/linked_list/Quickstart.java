public class Quickstart {

	public static void main(String[] args) {
		LinkedList<Integer> bag1 = new LinkedList<Integer>();
		
		/*Adding nodes to the linked list */
		bag1.add(3);
		bag1.add(4);
		bag1.add(5);
		bag1.add(6);
		bag1.add(7);
		bag1.add(8);
		
		/*Removing node from the list */
		bag1.remove(5);
		
		/*Printing the nodes in the linked list*/
		bag1.printLinkedList();

		/*Clearing the list*/
		bag1.clear();

		/*Checking if linked list is empty*/
		System.out.println("Bag1 is empty: " + bag1.empty());

		bag1.printLinkedList();
	}
}
