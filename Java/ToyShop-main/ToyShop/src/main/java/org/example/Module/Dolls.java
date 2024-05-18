package org.example.Module;

/**
 * Класс описывающий кукол наследуется от игрушки
 */
public class Dolls extends Toy {

    //region public Method

    @Override
    public String toString() {
        return super.toString() + String.format(" | Hair %b",hair);
    }

    //endregion

    //region Files
    boolean hair;          // если ли у куклы волосы


    //endregion

    //region Constructor

    public Dolls(String name, Integer weight, String material,boolean hair) {
        super(name, weight, material);
        this.hair = hair;

    }

    @Override
    public int compareTo(Toy o) {
        return 0;
    }

    //endregion
}
