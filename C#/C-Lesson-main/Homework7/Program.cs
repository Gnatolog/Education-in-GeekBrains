//  Task1 Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.
// Пример  m = 3, n = 4.
// 0,5 7 -2 -0,2
// 1 -3,3 8 -9,9
// 8 7,8 -7,1 9

// double[,] CreateRandom2dArray(int rows, int colums)
// {
//     double [,] array = new double[rows,colums];

//     for (int i = 0; i < rows; i ++)
//         for (int j = 0; j < colums; j++)
//             array[i,j] = new Random().NextDouble();
//     return array;
// }
// void Show2dArray(double[,] array)
// {
//     Console.WriteLine("Массив с вещественными рандомными числами отформатированый");
//     Console.WriteLine();
//     for(int i = 0; i < array.GetLength(0);i++)
//     {
//         for (int j = 0; j < array.GetLength(1);j++)
//         {
//             array[i,j] = Math.Round(array[i,j],2);
//             Console.Write(array[i,j] + " ");
//         }
//         Console.WriteLine();
//     }
//     Console.WriteLine();
// }
// Console.WriteLine("input a quantity of m: ");
// int rows = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine("input a quantity of n: ");
// int columns = Convert.ToInt32(Console.ReadLine());
// double [,] myArray = CreateRandom2dArray(rows,columns);
// Console.WriteLine();
// Show2dArray(myArray);
// Console.WriteLine($"Press Enter to exit");
// Console.ReadLine();

// Task2 Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, 
// и возвращает значение этого элемента или же указание, что такого элемента нет.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// 1 7 -> числа с такими индексами в массиве нет

// int[,] CreateRandom2dArray(int rows, int colums)
// {
//     int [,] array = new int[rows,colums];

//     for (int i = 0; i < rows; i ++)
//         for (int j = 0; j < colums; j++)
//             array[i,j] = new Random().Next(10,100);
//     return array;
// }
// void Show2dArray(int[,] array)
// {
//     for(int i = 0; i < array.GetLength(0);i++)
//     {
//         for (int j = 0; j < array.GetLength(1);j++)
//             Console.Write(array[i,j] + " ");

//         Console.WriteLine();
//     }
//     Console.WriteLine();
// }

// void CheckElements(int[,] array,int rows,int colums)
// {
//         int elements = 0;
//         for(int i = 0; i < array.GetLength(0);i++)    
//             for (int j = 0; j < array.GetLength(1);j++)
//             {
//                 if(rows == i && colums == j)
//                 elements = array[i,j];
//             }
//     if (elements!=0)
//     Console.WriteLine($"Element Found is - {elements}");
//     else
//     Console.WriteLine("Element not Found");
// }

// Console.WriteLine("Position elements in array rows: ");
// int rows = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine("Position elements in array colums: ");
// int colums = Convert.ToInt32(Console.ReadLine());
// int[,] myArray = CreateRandom2dArray(5,5);
// Console.WriteLine();
// Show2dArray(myArray);
// CheckElements(myArray,rows,colums);
// Console.WriteLine("\n\tPress Enter to Exit");
// Console.ReadLine();

// Task3 Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.

// int[,] CreateRandom2dArray(int rows, int colums)
// {
//     int [,] array = new int[rows,colums];

//     for (int i = 0; i < rows; i ++)
//         for (int j = 0; j < colums; j++)
//             array[i,j] = new Random().Next(1,10);
//     return array;
// }

// void Show2dArray(int[,] array)
// {
//     for(int i = 0; i < array.GetLength(0);i++)
//     {
//         for (int j = 0; j < array.GetLength(1);j++)
//             Console.Write(array[i,j] + " ");

//         Console.WriteLine();
//     }
//     Console.WriteLine();
// }

// void Average (int [,]array)
// { 
    
//     Console.Write($"\nArithmetic mean of each column: ");
//     for(int i = 0;i < array.GetLength(1);i++)
//     {
//         double sum = 0;  
//             for (int j = 0;j < array.GetLength(0);j++)             
//                 sum = sum + array[j,i];        
//     sum = Math.Round(sum / array.GetLength(0),2);
//     Console.Write($"{sum}; "); 
//     }       
//     Console.WriteLine();
// }

// int[,] myArray = CreateRandom2dArray(3,4);

// Console.WriteLine();
// Show2dArray(myArray);
// Average(myArray);
// Console.WriteLine();
// Console.WriteLine($"\n\t\tPress Enter to Exit");
// Console.ReadLine();



