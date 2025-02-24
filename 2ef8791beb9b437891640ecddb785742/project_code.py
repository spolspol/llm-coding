csharp/*design a program to solve a quadratic equation of x^2 + b*x + c = 0
Your program should handle real and complex roots.
Use console Based user input and display output on console. */

using System;

class QuadraticEquationSolver
{
    static void Main(string[] args)
    {
        Console.Write("Enter coefficient b: ");
        double b = Convert.ToDouble(Console.ReadLine());
        Console.Write("Enter coefficient c: ");
        double c = Convert.ToDouble(Console.ReadLine());

        double discriminant = b * b - 4 * c;

        if (discriminant > 0)
        {
            double root1 = (-b + Math.Sqrt(discriminant)) / 2;
            double root2 = (-b - Math.Sqrt(discriminant)) / 2;
            Console.WriteLine($"The roots are real and different. Root1 = {root1}, Root2 = {root2}");
        }
        else if (discriminant == 0)
        {
            double root = -b / 2;
            Console.WriteLine($"The roots are real and same. Root = {root}");
        }
        else
        {
            // Handle complex roots
            double realPart = -b / 2;
            double imaginaryPart = Math.Sqrt(-discriminant) / 2;

            Console.WriteLine($"The roots are complex and different.");
            Console.WriteLine($"Root1 = {realPart} + {imaginaryPart}i");
            Console.WriteLine($"Root2 = {realPart} - {imaginaryPart}i");
        }
    }
}
