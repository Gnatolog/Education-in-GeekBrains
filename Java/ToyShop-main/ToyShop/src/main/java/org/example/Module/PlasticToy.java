package org.example.Module;

/**
 * Класс описывающий пластиковые игрушки наследуется от абстрактного класса игрушки
 */

public class PlasticToy extends Toy {
    //region public Method

    @Override
    public String toString() {
        return super.toString() + String.format(" | Battery %b",battery);
    }

    //endregion

    //region Files
    boolean battery;          // если ли у игрушки батарейки


    //endregion

    //region Constructor

    public PlasticToy(String name, Integer weight, String material,boolean battery) {
        super(name, weight, material);
        this.battery = battery;

    }

    @Override
    public int compareTo(Toy o) {
        return 0;
    }

    //endregion
}
