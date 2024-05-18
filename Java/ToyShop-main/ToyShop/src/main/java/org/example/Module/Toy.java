package org.example.Module;


/**
 * Базовый абстрактный класс игрушки
 */
public abstract class Toy implements Comparable<Toy> {



    //region public Method
    @Override
    public String toString() {
        return String.format("id toy: %d | wight toy: %d | name toy: %s | material toy: %s ",
                id,weight,name,material);
    }
    //endregion

    //region Constructor

    public Toy( String name, Integer weight, String material) {
        this.id = ++count;
        this.name = name;
        this.weight = weight;
        this.material = material;
    }

    //endregion


    //region Getter and Setter


    public String getMaterial() {
        return material;
    }

    public Integer getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public Integer getWeight() {
        return weight;
    }
    // endregion

    //region Files
    static Integer count = 0;
    private final Integer id;
    protected String name;
    protected Integer weight;

    protected String material;
    //endregion
}
