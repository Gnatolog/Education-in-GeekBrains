Console.WriteLine ("Enter your name: ");
string username = Console.ReadLine();

if (username.ToLower() == "маша")
{
    Console.WriteLine("Ура, этоже Маша!");
}
else 
{
    Console.Write("Привет, ");
    Console.WriteLine (username);
}
