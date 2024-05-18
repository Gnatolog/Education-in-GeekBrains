package org.example.Module;

import java.io.FileWriter;
import java.io.IOException;
import java.util.List;


/**
 * Класс созранения результата розыгрыша в файл
 */
public class Saving {

    /**
     * Метод сохранения получнных дынных розыграша в файл txt
     * @param list список розыгранных игрушек
     */
    public void save_files(List<Toy> list)  {
        String path = "result.txt";
        try(FileWriter writer = new FileWriter(path)){
            for (Toy toy: list) {
                try {
                    writer.write("\n\tВыпала игрушка: " + toy.toString() + "\n");
                    writer.write("\tToy id: "+toy.getId() + "\n");
                }
                catch (NullPointerException e){
                    writer.write("""

                             Нечего не выпало
                            """);
                }
            }
        }
        catch (IOException e){
            System.out.println("File not Found");
        }
    }

}
