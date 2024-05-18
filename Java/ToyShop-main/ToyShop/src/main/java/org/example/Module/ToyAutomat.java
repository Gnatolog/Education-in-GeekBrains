package org.example.Module;

import java.util.PriorityQueue;
import java.util.Random;


/**
 * Класс игового автомата
 */
public class ToyAutomat {


    //region public Method

    /**
     * Метод добавления игрушек в автомат
     * @param toy игрушка которую добовляем в автомат
     */
    public void put (Toy toy){
        toys.add(toy);
    }

    /**
     * Метод выполняющий розыгрыш
     * @return возвращает либо выйгронную игрушку либо null
     */

    public Toy get (){
        Random random = new Random();
        int numb;
        for (Toy toy:toys) {
            numb = random.nextInt(1,10+1);
            if(numb <= toy.getWeight()){
                toys.remove(toy);        // елси игрушка выпала мы её удаляем из автомата
                return toy;             // и возвращаем игрушку
            }
        }
        return null;                  // если игрушка не выпала то возвращаем null
    }

    //endregion

    //region Files
    PriorityQueue<Toy> toys = new PriorityQueue<>(); // хранилище игрушек загруденных в автомат
    //endregion
}
