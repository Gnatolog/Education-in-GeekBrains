// Task 1: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B. Пример 3, 5 -> 243 (3⁵)

// int Degree (int num_a, int num_b) 
// {
//     int i = 0;
//     int deg = 1;
//     while (i < num_b)
//     {
//         deg = deg * num_a;  
//         i ++;
//     }
    
//     return deg;
// }
// Console.Write("\nВведите число которое хотите возвести в степень: ");
// int a = Convert.ToInt32(Console.ReadLine());
// Console.Write("\nВведите степень в которую хотите возвести число: ");
// int b = Convert.ToInt32(Console.ReadLine());
// int result = Degree(a,b);
// Console.WriteLine ($"\n\tЧисло {a} возведённое в степень {b} = {result}");
// Console.WriteLine($"\nPress Enert to exit");
// Console.ReadLine();

// Task 2: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе. Пример 452 -> 11

// int Sumnumb(int num)
// {
//     int num1 = num;
//     int num2 = 0;
//     int sum = 0;
//     while(num1 > 0)
//     {
//         num2 = num1 %= 10;
//         num1 = num /= 10;
//         sum = num2 + sum;
//     }  
//      return sum;
// }
// Console.Write($"\nВведите число сумму чисел которого хотите получить: ");
// int number = Convert.ToInt32(Console.ReadLine());
// int result = Sumnumb(number);
// Console.WriteLine($"\n\tСумма цифр в  чисел {number} = {result}");
// Console.WriteLine($"\nPress Enter to Exit");
// Console.ReadLine();

// Task 3: Напишите программу, которая задаёт массив из 8 элементов и выводит их на экран. Пример 1, 2, 5, 7, 19 -> [1, 2, 5, 7, 19]

//  void Array ()
// {
//    int [] array = {1,2,3,4,5,6,7,8};
//    int i = 0;
//    int n = array.Length;
//    string result = "";
//    while (i < n ) 
//    {
//       if (array[i] < n + 1)
//       result = result + array[i] + ", ";
//       i++;
//    }
//       Console.WriteLine($"\nУ меня есть Массив = [{result}]");
// }
// Array();
// Console.WriteLine("\nPress Enter to Exit");
// Console.ReadLine();

