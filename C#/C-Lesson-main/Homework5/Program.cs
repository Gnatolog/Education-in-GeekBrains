// Task1: Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, 
// которая покажет количество чётных чисел в массиве Пример [345, 897, 568, 234] -> 2

// int [] CreateRandomArray(int size)
// {
//     int [] array = new int [size];
//     Random number = new Random();
//     int min = number.Next(100, 500);
//     int max = number.Next(500,1000);
//     for (int i = 0; i< size; i++)
//         array[i]  = new Random().Next(min,max);
//     return array;
// }
// void ShowArray(int [] array)
// {   Console.WriteLine("\nYour Array");
//     for(int i = 0; i < array.Length; i++)
//         Console.Write($"{array[i]}" + "," );
//     Console.WriteLine();
//  }
// void EvenNumbers(int [] array)
// {
//     int even = 0;
//   for (int i = 0; i < array.Length; i ++)
//   {
//        array[i]=array[i]%2;
//        if (array[i] == 0) even ++;
//   }
//     Console.WriteLine($"\n\tNumber of even numbers = {even}");
// }
// Console.WriteLine("Enter size array");
// int size = Convert.ToInt32(Console.ReadLine());
// int [] array = CreateRandomArray(size);
// ShowArray(array);
// EvenNumbers(array);
// Console.WriteLine("\nPress Enter to Exit");
// Console.ReadLine();

//  Task2: Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.
//  Пример [3, 7, 23, 12] -> 19

int [] CreateRandomArray(int size)
{
    int [] array = new int [size];
    Random number = new Random();
    int min = number.Next(1,10);
    int max = number.Next(10,40);
   
    for (int i = 0; i< size; i++)
        array[i]  = new Random().Next(min,max);
    
    return array;
}
void ShowArray(int [] array)
{   Console.WriteLine("\nYour Array");
    for(int i = 0; i < array.Length; i++)
        Console.Write($"{array[i]}" + " " );
    Console.WriteLine();
}
void SumElements( int[] array)
{
    int sum = 0;
    int odd = 0;
    for ( int i = 0; i < array.Length; i++)
     {
        odd = i%2;
        if (odd!=0) sum = sum + array[i];
     }
    Console.WriteLine($"\n\t Sum of odd indices = {sum}");
}
Console.WriteLine("Enter size array");
int size = Convert.ToInt32(Console.ReadLine());
int [] array = CreateRandomArray(size);
ShowArray(array);
SumElements(array);
Console.WriteLine("\nPress Enter to Exit");
Console.ReadLine();

// Task3: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.
// [3 7 22 2 78] -> 76
double [] CreateRandomArray(int size)
{
    double [] array = new double [size];
    Random number = new Random();   
    for (int i = 0; i< size; i++)
        array[i]  = number.Next(100);  
    return array;
}
void ShowArray(double [] array)
{   Console.WriteLine("\nYour Array");
    for(int i = 0; i < array.Length; i++)
        Console.Write($"{array[i]}" + " " );
    Console.WriteLine();
}
double Min_Max (double[] array)
{
    double max = array[0];
    double min = array[1];
    double difference = 0;
    for ( int i = 0; i < array.Length; i++)
    {   
        if (array[i]> max) max = array[i];
        if (array[i] < min) min = array[i];
    } 
    difference = max - min;
    return difference;


}
Console.WriteLine("Enter size array");
int size = Convert.ToInt32(Console.ReadLine());
double [] array = CreateRandomArray(size);
ShowArray(array);
double Diff = Min_Max(array);
Console.WriteLine($"\nРазница между максимальным и минимальным знчением массива  =  {Diff}");
Console.WriteLine("\nPress Enter to Exit");
Console.ReadLine();