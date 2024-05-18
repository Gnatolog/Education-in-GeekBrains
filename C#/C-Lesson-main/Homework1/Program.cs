//Task1
// Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее

// Console.Write("enter one number: ");
// int num1 = Convert.ToInt32(Console.ReadLine());
// Console.Write("enter two number: ");
// int num2 = Convert.ToInt32(Console.ReadLine());
// if (num1 > num2) Console.WriteLine( "max = " + num1 );
// else Console.WriteLine( "max = " + num2 );

//Task2
// Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел
// Console.Write("enter one number: ");
// int num1 = Convert.ToInt32(Console.ReadLine());
// Console.Write("enter two number: ");
// int num2 = Convert.ToInt32(Console.ReadLine());
// Console.Write("enter trhee number: ");
// int num3 = Convert.ToInt32(Console.ReadLine());
// int max = 0;
// if (num1 > num2) max = max + num1;
// else max = max + num2;
// if (max < num3) max = num3;
// Console.WriteLine("Max value = " + max);

//Task3
//Напишите программу, которая на вход принимает число и выдаёт, является ли число чётным (делится ли оно на два без остатка)
// Console.Write("Enter number: ");
// int num1 = Convert.ToInt32(Console.ReadLine());
// int num2 = 2;
// int rem = num1%num2;
// if (rem == 0) Console.WriteLine("Число Чётное");
// else Console.WriteLine("Число Нечётное");

//Task4
//Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
Console.Write("Enter number: ");
int N = Convert.ToInt32(Console.ReadLine());
int num1 = 1;
int num2 = 2;
 while(num1 <= N)
 { 
    int rem = num1%num2;
    if (rem == 0) Console.Write(num1 + " , ");
    num1 ++; // num + 1
 }








