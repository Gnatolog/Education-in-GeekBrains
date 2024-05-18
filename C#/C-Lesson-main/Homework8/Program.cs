// Task1  Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.
// Например, задан массив:
// 1 4 7 2          
// 5 9 2 3
// 8 4 2 4'

// В итоге получается вот такой массив:

// 7 4 2 1
// 9 5 3 2
// 8 4 4 2

// int[,] CreateRandom2dArray(int rows, int colums,int minValue,int maxValue)
// {
//     int [,] array = new int[rows,colums];

//     for (int i = 0; i < rows; i ++)
//         for (int j = 0; j < colums; j++)
//             array[i,j] = new Random().Next(minValue,maxValue +1);
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
// void SelectionSort (int[,] array)
//      // функция упорядочивает двумерный массив по убыванию
// {
//     int tmp;
//     for (int n = 0; n < array.GetLength(0) * array.GetLength(1) ; n++) // перебираем все матрицу
//     {
//         for (int i = array.GetLength(0)-1; i >= 0; i--) // проход по collum
//         {
//             for (int j = 0; j < array.GetLength(1)-1; j++) // проход row
//             {
//                 if (array[i,j+1] > array[i, j] &&  j != array.GetLength(0) - 1)     //       
//                {   

//                 tmp = array[i, j+1];
//                 array[i, j+1] = array[i,j];
//                 array[i, j] = tmp;            
//                }

//             }   
//         }   
         
//     }
           
// }

// Console.Write("input a quantity of rows:");
// int rows = Convert.ToInt32(Console.ReadLine());
// Console.Write("input a quantity of columns:");
// int columns = Convert.ToInt32(Console.ReadLine());
// Console.Write("input a min value:");
// int minValue = Convert.ToInt32(Console.ReadLine());
// Console.Write("input a max value:");
// int maxValue = Convert.ToInt32(Console.ReadLine());

// int [,] array = CreateRandom2dArray(rows,columns,minValue,maxValue);
// Show2dArray(array);
// SelectionSort(array);
// Show2dArray(array);
// Console.WriteLine("Press Enter to Exit");
// Console.ReadLine();


// Task 2  Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.

// Например, задан массив:
// 1 4 7 2

// 5 9 2 3

// 8 4 2 4

// 5 2 6 7

// Программа считает сумму элементов в каждой строке и выдаёт номер строки с наименьшей суммой элементов: 1 строка

// int[,] CreateRandom2dArray(int rows, int colums,int minValue,int maxValue)
// {
//     int [,] array = new int[rows,colums];

//     for (int i = 0; i < rows; i ++)
//         for (int j = 0; j < colums; j++)
//             array[i,j] = new Random().Next(minValue,maxValue +1);
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

// int RowMinSum (int[,] array)
     // функция устанавливает наименьшее значение суммы строки и ищет номер строки с  
    //  наименьшей суммы строки всей матрицы
// {
//     int min = 0;
//     int col = 0;
    
//         for (int j = 0; j < array.GetLength(1);  j++)  min += array[0,j]; // установка  минимальной суммы строки
        

//         for (int i = 0; i < array.GetLength(0);  i++) // поиск наименьшой строки
//         {
//             int sum=0;
            
//             for (int j = 0; j < array.GetLength(1);j++) sum+=array[i,j];    

//             if (sum < min) 
//             {
//                 col=i;
//             }    
//         }
        
//     return col+1;          
// }

// Console.Write("input a quantity of rows:");
// int rows = Convert.ToInt32(Console.ReadLine());
// Console.Write("input a quantity of columns:");
// int columns = Convert.ToInt32(Console.ReadLine());
// Console.Write("input a min value:");
// int minValue = Convert.ToInt32(Console.ReadLine());
// Console.Write("input a max value:");
// int maxValue = Convert.ToInt32(Console.ReadLine());

// int [,] array = CreateRandom2dArray(rows,columns,minValue,maxValue);
// Show2dArray(array);
// int minrow = RowMinSum(array);
// Console.WriteLine($"Номер строки с наименьшей суммой элементов\t{minrow}");
// Console.WriteLine("Press Enter to Exit");
// Console.ReadLine();

// Task3 Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.(перемножение матриц)
// Например, даны 2 матрицы:
// 2 4 | 3 4
// 3 2 | 3 3
// Результирующая матрица будет:
// 18 20
// 15 18

// int[,] CreateRandom2dArray()
// {
//     int rows = 2;
//     int colums = 2;
//     int [,] array = new int[rows,colums];

//     for (int i = 0; i < rows; i ++)
//         for (int j = 0; j < colums; j++)
//             array[i,j] = new Random().Next(1,11);
//     return array;
// }

// void Show2dArray2(int[,] array,int[,] array2)
// {
//     for(int i = 0; i < array.GetLength(0);i++)
//     {
//         for (int j = 0; j < array.GetLength(1);j++)
//             Console.Write(array[i,j] + " ");

//         Console.WriteLine();
//     }
//     Console.WriteLine();

//         for(int i = 0; i < array2.GetLength(0);i++)
//     {
//         for (int j = 0; j < array2.GetLength(1);j++)
//             Console.Write(array2[i,j] + " ");

//         Console.WriteLine();
//     }
//     Console.WriteLine();
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


// int [,] MultiplicationMatrix(int[,] array,int[,] array2)
// // функция  произведение двух матриц
// {
//     if (array.GetLength(0) != array2.GetLength(1))
//     {
//         Console.WriteLine("Умножить не возможно так как матрицы не равны");
//     }
//     int [,] matrixresult = new int[array.GetLength(0),array.GetLength(1)];

//     for(int i = 0; i < array.GetLength(0);i++)
//     {
//         for(int j = 0; j < array.GetLength(1);j++)
//         {
//             matrixresult[i,j] = 0;
        
//             for(int k = 0; k < array.GetLength(0);k++)
//             {
//                 matrixresult[i,j] +=  array[i,k] * array2[k,j];
//             }
//         }
//     }   
//     return matrixresult;
// }
// int [,] array = CreateRandom2dArray();
// int [,] array2 = CreateRandom2dArray();
// Show2dArray2(array,array2);
// int [,] result = MultiplicationMatrix(array,array2);
// Console.WriteLine("Результат произведенния двух матриц:");
// Show2dArray(result);

// Task4 .Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу, 
// которая будет построчно выводить массив, добавляя индексы каждого элемента.
// Массив размером 2 x 2 x 2
// Пример:
// 66(0,0,0) 25(0,1,0)
// 34(1,0,0) 41(1,1,0)
// 27(0,0,1) 90(0,1,1)
// 26(1,0,1) 55(1,1,1)

// int[,,] CreateRandom3dArray()
// // Создаёт трехмерный массив с ручным вводом чисел и рамерностью
// {
//     int [,,] array = 
//     {
//         {
//             {45,16},
//             {44,97}
//         },
//         {
//             {32,40},
//             {60,23}

//         }

//     };
//     return array;
// }

// void Show3dArray(int[,,] array)
// //Выводит трехмерный массив со значениями и их индексами
// {
//     for(int i = 0; i < array.GetLength(0);i++)
//     {
//         Console.WriteLine();
        
//         for (int j = 0; j < array.GetLength(1);j++)
//             for(int k = 0; k < array.GetLength(2); k++)
//                 Console.Write($" {array[i,j,k]}({i},{j},{k}) ");
//                 Console.WriteLine();
        

//     Console.WriteLine();
//     }
// }

// int [,,] array = CreateRandom3dArray();
// Show3dArray(array);
// Console.WriteLine("Press Enter to Exit");
// Console.ReadLine();

// Task 5 Напишите программу, которая заполнит спирально массив 4 на 4.
// Например, на выходе получается вот такой массив:
// 01 02 03 04
// 12 13 14 05
// 11 16 15 06
// 10 09 08 07


// int[,] CreateRandom2dArray()
//  Функция заполняет матрицу по спирали
// Думаю не самое лучшее решение но получилось пока так(
// {
//     int [,] array = new int[4,4];
//     int row = 0;
//     int col = 0;
//     int dx = 0;
//     int dy = 0;
//     int n = array.GetLength(0) * array.GetLength(1);
//     int v = 1;
//     while (n !=0 )
//     {
//         if (dx == 0 && dy == 0 || dy < array.GetLength(1)-1)
//         {
//             array[row,col] = v;
//             v++;
//             dy++;
//             col=dy;
//         }
//         if (col==array.GetLength(0)-1 && dx <= array.GetLength(1)-1)  
//         {  
//            array[row,col] = v;
//            dx++;
//            row=dx;
//            v++;
//         }
//         if (v > 7 && v <=10)  
//         {  row=array.GetLength(0)-1;
//            col= col-1;
//            array[row,col] = v;           
//            v++;           
//         }
//         if (v > 10 && v <= 12)
//         {
//             col = 0;
//             row = row-1;
//             array[row,col] = v;           
//             v++;
//         }
//         if (v > 12 && v <= 14)
//         {
//             col ++;
//             row = 1;
//             array[row,col] = v;           
//             v++;
//         }
//         if (v > 14 && v <= 15)
//         {
//             row = 2;
//             array[row,col] = v;           
//             v++;
//         }
//         if (v > 15 && v <= 16)
//         {
//             col--;
//             row = 2;
//             array[row,col] = v;           
//             v++;
//         }
//      n--;

//     }

//     return array;
// }

// void Show2dArray(int[,] array)
// {
//     for(int i = 0; i < array.GetLength(0);i++)
//     {
//         for (int j = 0; j < array.GetLength(1);j++)
//             if (array[i,j] < 10) Console.Write($"0{array[i,j]}" + " " );
//             else Console.Write($"{array[i,j]}" + " " );


//         Console.WriteLine();
//     }
//     Console.WriteLine();
// }

// int [,] array = CreateRandom2dArray();
// Show2dArray(array);

