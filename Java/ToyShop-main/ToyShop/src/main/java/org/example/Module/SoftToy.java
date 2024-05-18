package org.example.Module;

/**
 * Класс описывающий мягкую игрушку наследуемый от класаа игрушка
 */
public class SoftToy extends Toy {

    //region public Method

    @Override
    public String toString() {
        return super.toString() + String.format(" | laundry: %b",laundry);
    }

    //endregion

    //region Files
    private final boolean laundry;  // возможность стирать игрушку

    //endregion

    //region Constructor

    public SoftToy(String name, Integer weight, String material,boolean laundry) {
        super(name, weight, material);
        this.laundry=laundry;
    }

    @Override
    public int compareTo(Toy o) {
        return 0;
    }

    //endregion
}
