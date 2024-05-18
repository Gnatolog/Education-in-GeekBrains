void RandomNum ( int[]  collection)
{
    int len = collection.Length; 
    int index = 0;
    while(index<len)
    {
        collection[index] = new Random().Next(1,10);
        index ++;
    }
}

void PrintArray ( int[] col)
{
    int value = col.Length;
    int possition = 0;
    while ( possition < value )
    {
        Console.WriteLine(col[possition]);
        possition ++;
    }

}

int IndexOf (int[] collection, int find)
{
    int value = collection.Length;
    int index = 0;
    int possition = -1;

    while ( index < value)
    {
        if (collection[index] == find)
        {
            possition = index;
            break;
        }
        index ++;
    }
    return possition;
}

int[] array = new int [10];

RandomNum(array);
PrintArray(array);
int pos = IndexOf(array,66);
Console.WriteLine("index Find = " + pos);