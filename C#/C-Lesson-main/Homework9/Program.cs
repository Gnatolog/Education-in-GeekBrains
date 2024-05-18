//  Сппасибо за обучение было сложно но интересно!)


// Task1 Задайте значение N. Напишите программу, которая выведет 
// все натуральные числа в промежутке от N до 1. Выполнить с помощью рекурсии. (void)

// N = 5 -> "5, 4, 3, 2, 1"
// N = 8 -> "8, 7, 6, 5, 4, 3, 2, 1"

// void ShowNum(int n)
// // Рекурсивная функция выводит число от N до 1
// {
//     Console.Write(n + " ");
//     if(n > 1)ShowNum(n-1);  
// }

// Console.WriteLine("Введите натуральное число больше: ");
// int n = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine("Natural numbers from N to 1");
// ShowNum(n);
// Console.WriteLine();
// Console.WriteLine();
// Console.WriteLine("Press Enter to Exit");
// Console.ReadLine();

// Задача 66: Задайте значения M и N. Напишите программу, которая найдёт 
// сумму натуральных элементов в промежутке от M до N.(int)

// M = 1; N = 15 -> 120
// M = 4; N = 8. -> 30

// int SearchSum(int m, int n)
// // Рекурсивный метод который ищет сумму от M до  N
// {       
//     if (n >= m ) return SearchSum(m, n - 1) + n;
//     return 0;
// }
// Console.WriteLine();
// Console.WriteLine($" Sum numbers: {SearchSum(1,15)}");
// Console.WriteLine();
// Console.WriteLine("Press Enter to Exit");
// Console.ReadLine();

// Задача 68: Напишите программу вычисления функции Аккермана с помощью рекурсии. 
// Даны два неотрицательных числа m и n.
// m = 2, n = 3 -> A(m,n) = 9
// m = 3, n = 2 -> A(m,n) = 29

// int FunctionAcerman(int n, int m)
// Программа вычисления функции Акермана
// {
//   if (n == 0)
//     return m + 1;
//   else
//        if ((n != 0) && (m == 0))
//           return FunctionAcerman(n - 1, 1);
//         else
//           return FunctionAcerman(n - 1, FunctionAcerman(n, m - 1));    
// }

// Console.WriteLine();
// Console.WriteLine($" Sum numbers: {FunctionAcerman(3,2)}");
// Console.WriteLine();
// Console.WriteLine("Press Enter to Exit");
// Console.ReadLine();
