/**
 * Programmed by: Donaldo Cruz with help from the book, Data Structures & Other Objects Using JAVA, by Michael Main.
 * Stack: a data structure of ordered items such that items can be inserted and removed only at one end (called the top).
 */
import java.util.EmptyStackException;

public class Stack<E> implements Cloneable {

    /*Instance variables*/
	private Node<E> top;
	
    /**
     * Default Constructor
     */
    public Stack() {
    	this.top = null;
    }

    /**
     * This method determines if this stack is empty.
     * @return True if this stack is empty.
     */
    public boolean isEmpty() {
    	return top == null;
    }

    /**
     * This method gets the top element of the stack without removing the item.
     * @return The element at the top of the stack.
     */
    public E peek() {
    	if (top == null)
    		throw new EmptyStackException();
    	return this.top.getData();
    }

    /**
     * This method gets the top element of the stack, and removes it from the stack.
     * @return The element at the top of the stack.
     */
    public E pop() {
    	if (top == null) 
    		throw new EmptyStackException();
    	
    	E answer = this.top.getData();
    	this.top = this.top.getLink();
    	return answer;
    }

    /**
     * This method add an element to the top of the stack.
     * @param element The element to be added to the top of the stack.
     */
    public void push(E element) {
    	top = new Node<E>(element, top);
    }

    /**
     * This method determines the number of elements in this stack.
     * @return The number of elements in this stack.
     */
    public int size() {
    	return Node.listLength(top);
    }
    
    /**
     * This method returns a clone of this stack.
     * @return The copy of this stack.
     */
    public Stack<E> clone() {
    	Stack<E> copy;
    	
    	try {
    		copy = (Stack<E>) super.clone();
    	}
    	catch(CloneNotSupportedException e) {
    		throw new RuntimeException("This class does not implement Cloneable.");
    	}
    	copy.top = Node.listCopy(top);
    	return copy;
    }
}