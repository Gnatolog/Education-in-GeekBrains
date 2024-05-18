using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

class CardPicker
{
    static Random random = new Random();
    public static string[]PickSomeCards (int numberOfCards)
    {
      string[] pickedCards = new string[numberOfCards];
      for (int i = 0; i < numberOfCards; i++)
      {
        pickedCards[i] = RandomValue() + " of " + RandomSuit();
      }        
      return pickedCards;
    }
     private static string RandomValue()
      {
        int value = random.Next(1,14);
        // если это 1 то вернуть строку Ace
        if (value == 1) return "Ace";
        // если это 1 то вернуть строку Jack
        if (value == 11) return "Jack";
        // если это 1 то вернуть строку Queen
        if (value == 12) return "Queen";
        // если это 1 то вернуть строку King
        if (value == 13) return "King";
        return value.ToString();
        throw new NotImplementedException();
      }
     private static string RandomSuit()
     {
        int value = random.Next(1,5);
        if (value == 1) return "Spades";
        if (value == 2) return "Hearts";
        if (value == 3) return "Clubs";
        return "Diamonds";
        throw new NotImplementedException();
     }     


}