
public class Quickstart {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Stack<Double> nums = new Stack<Double>();
		
		/*Pushing elements onto the stack.*/
		nums.push(2.0);
		nums.push(4.0);
		nums.push(6.0);
		nums.push(8.0);
		nums.push(10.0);
		
		Stack<Double> duplicate = nums.clone(); // Cloning stacks
		int length = nums.size(); //Retrieving size of stack.
		
		/*Popping elements off of the stack.*/
		for(int i = 0; i < length; i++) {
			System.out.println(nums.pop()); //Popping element off of stack
		}
		
		System.out.println("Next Stack");
		
		for(int i = 0; i < length; i++) {
			System.out.println(duplicate.peek()); //Peeking at element, but not removing.
		}
		
		System.out.println("Size of nums stack: " + nums.size());
		System.out.println("Size of duplicate stack: " + duplicate.size());
	}
}
