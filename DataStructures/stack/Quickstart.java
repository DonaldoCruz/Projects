import java.util.Stack;
import java.util.Scanner;
import java.util.regex.Pattern;

public class Quickstart {

    public static final Pattern UNSIGNED_DOUBLE = Pattern.compile("((\\d+\\.?\\d*)|(\\.\\d+))([Ee][-+]?\\d+)?.*?");
    public static final Pattern CHARACTER = Pattern.compile("\\S.*?");

    public static void main(String[] args) {
        System.out.println(evaluate("((5+2)*(3+9))"));
    } 

    /*Practicing with imported Stack*/
    public static double evaluate(String expression) {
        Stack<Double> numbers = new Stack<Double>();
        Stack<Character> operations = new Stack<Character>();

        //Converting expression to a Scanner for easier processing.
        Scanner input = new Scanner(expression);
        //next string holds the next piece of the expression.
        String next;
        
        while(input.hasNext()) {
            if(input.hasNext(UNSIGNED_DOUBLE)) { // Checks if the next character in the expression is a number.
                next = input.findInLine(UNSIGNED_DOUBLE);
                numbers.push(Double.valueOf(next));
            }
            else {  // If it is not a number than it is an operation or parenthesis. (,),+,-,*, or /
                next = input.findInLine(CHARACTER);
                switch(next.charAt(0)) {
                    case '+': //Addition
                    case '-': //Subtraction
                    case '*': //Multiplication
                    case '/': //Division
                        operations.push(next.charAt(0));
                        break;
                    case ')': // Right paranthesis indicates to evaluate the top two numbers on the stack.
                        evaluateStackTops(numbers, operations);
                        break;
                    case '(': //Left paranthesis
                        break;
                    default:
                        input.close();
                        throw new IllegalArgumentException("Illegal character");
                }
            }
        }
        System.out.println(numbers.size());
        if(numbers.size() != 1) {
            input.close();
            throw new IllegalArgumentException("Illegal input expression");
        }
        input.close();
        return numbers.pop();
    }

    public static void evaluateStackTops(Stack<Double> numbers, Stack<Character> operations) {
        double operand1, operand2;

        if(numbers.size() < 2 || operations.isEmpty())
            throw new IllegalArgumentException("Illegal expression");
        operand2 = numbers.pop();
        operand1 = numbers.pop();

        switch(operations.pop()) {
            case '+':
                numbers.push(operand1 + operand2);
                break;
            case '-':
                numbers.push(operand1 - operand2);
                break;  
            case '*':
                numbers.push(operand1 * operand2);
                break;
            case '/':
                numbers.push(operand1 / operand2);
                break;
            default: 
                throw new IllegalArgumentException("Illegal operation");
        }
    }
}