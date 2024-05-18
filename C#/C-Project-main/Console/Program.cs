
int Multiply(int factor1, int factor2)
{
    int product = factor1 * factor2;
    return product;
}
Console.WriteLine("numb 1: ");
int height = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("numb 2: ");
int width = Convert.ToInt32(Console.ReadLine());
int area = Multiply(height,width);
Console.WriteLine("Value = " + area);