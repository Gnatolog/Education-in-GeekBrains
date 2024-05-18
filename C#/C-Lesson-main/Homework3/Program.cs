// Task1
// Напишите программу, которая принимает на вход  число и проверяет, является ли оно палиндромом. Пример 14212 -> нет 12821 -> да
// Итерационная функция для проверки, является ли заданное число палиндромом или нет

// bool Polindrome (int numb)
// {
//     int mirror = 0;
//     int copy = numb;
//     while (copy > 0)
//     {
//         int cut = copy % 10;
//         copy = copy / 10;
//         mirror = mirror * 10 + cut;
//     }
//      if (mirror == numb)
//      return true;
//      else
//      return false;
// }
// Console.WriteLine($"Введите число что бы проверить является ли оно палиндромом");
// int number = Convert.ToInt32(Console.ReadLine());
// bool result = Polindrome(number);
// if (result == true) Console.WriteLine($"\n\t\t\tВаше число является палиндромом");
// else Console.WriteLine($"\n\tВаше число не является полиндром");
// Console.WriteLine("\nНажмите Enter для Выхода");
// Console.ReadLine();

// Task2
// Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве. 
// Пример A (3,6,8); B (2,1,-7), -> 15.84

// double Distance3D (double x1, double x2, double y1, double y2, double z1, double z2)
// {
//     double root1 = Math.Pow((x2 - x1),2);
//     double root2 = Math.Pow((y2 - y1),2);
//     double root3 = Math.Pow((z2 - z1),2);
//     double distance = Math.Sqrt(root1+root2+root3);
//     double disround = Math.Round(distance,2);
//     return disround;
// }
// Console.WriteLine($"Enter value x1");
// double x1 = Convert.ToDouble(Console.ReadLine());
// Console.WriteLine($"Enter value x2");
// double x2 = Convert.ToDouble(Console.ReadLine());
// Console.WriteLine($"Enter value y1");
// double y1 = Convert.ToDouble(Console.ReadLine());
// Console.WriteLine($"Enter value y2");
// double y2 = Convert.ToDouble(Console.ReadLine());
// Console.WriteLine($"Enter value z1");
// double z1 = Convert.ToDouble(Console.ReadLine());
// Console.WriteLine($"Enter value z2");
// double z2 = Convert.ToDouble(Console.ReadLine());
// double result = Distance3D(x1,x2,y1,y2,z1,z2);
// Console.WriteLine($"\n\t\tThe distance between the points is {result}");
// Console.WriteLine($"\nPress Enter to Exist");
// Console.ReadLine();

// Task3
// Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.

// void Cube(int N)
// {
//     int number = 0;
//     while (number <= N )
//     {
//         int cube = number * number *number;
//         Console.WriteLine($"Куб числа {number} = {cube}");
//         number ++;
//     }

// }
// Console.WriteLine($"Введите число что бы получить таблицу кубов от 1 до Вашего числа");
// int n = Convert.ToInt32(Console.ReadLine());
// Cube(n);
// Console.WriteLine($"\n\t\tPress Enter to Exit");
