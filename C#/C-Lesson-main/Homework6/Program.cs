// Task1 Задача 41: Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь. 
// Пример 0, 7, 8, -2, -2 -> 2 1, -7, 567, 89, 223-> 3

// void ShowArray(int [] array)

// {
//     Console.WriteLine("Введёные Вами числа");
//     for(int i = 0; i < array.Length; i++)
//         Console.Write(array[i] + " ");

//     Console.WriteLine();

// }
// int Counter(int[] array)
// {
//  int i = 0;
//  int j = 0;
//  int answer = 2;
//  while (answer != 0)

//  {
//     Console.WriteLine("Введите число");
//     int m = Convert.ToInt32(Console.ReadLine());
//     Console.WriteLine("Будите продолжать вводить числа если да введите 1 если нет введите 0 ");
//     answer = Convert.ToInt32(Console.ReadLine());
//     j++;
//     array[j-1]= m;

//     if (m > 0) i ++;
//     Console.WriteLine();
//  }
//  return i;
// } 
// int [] array = new int [5];
// int count = Counter(array);
// ShowArray(array);
// Console.WriteLine();
// Console.WriteLine($"Из введенных Вами чисел больше 0 = {count}");

// Task2 Напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями 
// y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.
// b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; -0,5)

void Linear(double b1,double b2,double k1, double k2)
{
     double x = (b2-b1)/(k1 - k2);
     double y = (k2 * x) + b2;
     Console.WriteLine($"Точкой пересечения заданной Вами двух прямых является =  {x};{y}");
}
Console.WriteLine("Введите b1");
double b1 = Convert.ToDouble(Console.ReadLine());
Console.WriteLine("Введите b2");
double b2 = Convert.ToDouble(Console.ReadLine());
Console.WriteLine("Введите k1");
double k1 = Convert.ToDouble(Console.ReadLine());
Console.WriteLine("Введите k2");
double k2 = Convert.ToDouble(Console.ReadLine());
Console.WriteLine();
Linear(b1,b2,k1,k2);