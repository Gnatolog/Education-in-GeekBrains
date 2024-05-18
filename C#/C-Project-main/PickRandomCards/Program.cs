Console.WriteLine("Enter card number");
string line = Console.ReadLine();
if ( int.TryParse(line, out int numberOfCards))
{
    foreach(string card in CardPicker.PickSomeCards(numberOfCards))
    {
        Console.WriteLine(card);
    }
}
else
{
Console.WriteLine("Number is not valued");
}