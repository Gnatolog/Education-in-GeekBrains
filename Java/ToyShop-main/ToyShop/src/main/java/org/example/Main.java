package org.example;
import org.example.Module.*;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {


        ArrayList<Toy> list = new ArrayList<>(); // Список для хранения результата розыграша
        Saving saving = new Saving();           // Класс для созранения результатов в файл
        ToyAutomat automat = new ToyAutomat();  // Игровой автомат для загрузки игрушек

        // Создаём игрушки
        SoftToy softToy = new SoftToy("Beer",2,"Cotton",true);
        PlasticToy plasticToy = new PlasticToy("Car",6,"ABS",true);
        Dolls dolls = new Dolls("Doll Irina",8,"silicon",true);
        SoftToy softToy2 = new SoftToy("Cat",4,"Cotton",true);
        PlasticToy plasticToy2 = new PlasticToy("tractor",6,"ABS",true);
        Dolls dolls2 = new Dolls("Doll Gloria",3,"nylon",true);

        // Добавляем игрушки в автомат
        automat.put(softToy);
        automat.put(plasticToy);
        automat.put(dolls);
        automat.put(softToy2);
        automat.put(plasticToy2);
        automat.put(dolls2);

        // Проводим розыгрыш игрушек 10 раз
        list.add(automat.get());
        list.add(automat.get());
        list.add(automat.get());
        list.add(automat.get());
        list.add(automat.get());
        list.add(automat.get());
        list.add(automat.get());
        list.add(automat.get());
        list.add(automat.get());
        list.add(automat.get());
        list.add(automat.get());

        // Сохраняем полученный результат в файл
        saving.save_files(list);

    }
}