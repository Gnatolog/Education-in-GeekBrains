// Task 1 
// Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа. Пример: 456 -> 5
// int TwoNumbers(int num)
// {
//            num = num / 10;
//     int twonum = num % 10;
//     return twonum;
// }
// Console.Write($"Enter three-digit number: ");
// int isNumber = 0;
// while (isNumber < 99 || isNumber > 999 )
// {
//      isNumber = Convert.ToInt32(Console.ReadLine());
//      if (isNumber < 99 || isNumber > 999 )
//      {
//         Console.WriteLine ($"   Incorected numb");
//         Console.Write ($"Please re-enter the number: ");
//      }
// }
// int calculation = TwoNumbers(isNumber);
// Console.WriteLine($"This is the second number: {calculation}");
// ??? Есть впопрос Можите подсказать как сделать защиту программы от краша если пользователь введет не цифры а буквы или символы ???

// Task 2 
// Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет. Пример 645 -> 5 . 78 -> третьей цифры нет

// Console.WriteLine($"Enter number");
// int number = 0;

// while (number == 1 || number < 100)
// {
//       number = Convert.ToInt32(Console.ReadLine());
//       if (number == 1 || number < 100) 
//       {
//         Console.WriteLine($"   Трерьей цифры нет");
//         Console.Write($"Please re-enter the number: ");
//       }
// }
// string convert = Convert.ToString (number);

// Console.WriteLine(convert[2]);

// Task 3 
// Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным. 6 - да 7 -  да 3 -  нет
// bool Whatday (int num)
// {  

//    if (num == 6 || num == 7)
//        return true;
//     else
//        return false;
// }
// Console.WriteLine($"Please Enter 1 to 7 number : ");
// int number = Convert.ToInt32 (Console.ReadLine());
// bool result = Whatday(number);
// if (result == true) Console.WriteLine($"This day is day off");
// else Console.WriteLine($"This day is not a day off");

