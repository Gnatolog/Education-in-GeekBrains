// Task: Написать программу, которая из имеющегося массива строк формирует новый массив из строк, 
// длина которых меньше, либо равна 3 символам. Первоначальный массив можно ввести с клавиатуры, 
// либо задать на старте выполнения алгоритма. 
// При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.
// Примеры:
// [“Hello”, “2”, “world”, “:-)”] → [“2”, “:-)”]
// [“1234”, “1567”, “-2”, “computer science”] → [“-2”]
// [“Russia”, “Denmark”, “Kazan”] → []

using System;

string [] CreateArray(int size)
{
   string[] array = new string [size];
   int i = 0;
   while (i < size )
   {
    Console.WriteLine("Enter values ​​Lines");
    array[i] = Console.ReadLine()?? "Value cannot be empty";
    i++;
   }  
   return array;
}

void ShowArray(string [] array)
{   Console.WriteLine("\nYour Array");
    for(int i = 0; i < array.Length; i++)
        Console.Write($"{array[i]}" + ", " );
    Console.WriteLine();
}

void VerifiedArray (string[] array)
{
    string [] arrays = new string[array.Length];
    int value = 0;
    Console.WriteLine("\nVerified Array");
    for(int i = 0; i < array.Length; i++)
    {
        value = array[i].Length;  
        if (value <= 3) 
        { 
           arrays[i] += array[i];
           Console.Write($"{arrays[i]}" + ", " );
        }   
    }
    Console.WriteLine();
}

Console.WriteLine("Enter the number of lines you want to check");
int size = Convert.ToInt32(Console.ReadLine());
string [] list = CreateArray(size);    
ShowArray(list);
VerifiedArray(list);
Console.WriteLine("\nPress Enter to Exit");
Console.ReadLine();



