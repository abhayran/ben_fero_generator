import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class BenFeroDatasetGenerator {

    public static void main(String[] args) {
        BenFeroDatasetGenerator benfero = new BenFeroDatasetGenerator();
        benfero.mapper();
    }

    private final Gson gson = new GsonBuilder()
            .create();

    public void mapper() {
        try {
            File myObj = new File("benfero");
            Scanner myReader = new Scanner(myObj);
            Map<String, List<String>> dataset = new HashMap<>();
            List<String> song = new ArrayList<String>();
            boolean nameFlag = true;
            String songName = "";
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                if(nameFlag){
                    songName = data;
                    nameFlag = false;
                }else {
                    if(!data.equals("*")){
                        song.add(data);
                    } else{
                        dataset.put(songName, song);
                        nameFlag = true;
                    }
                }

            }


            String songMap = gson.toJson(dataset);
            myReader.close();
            FileWriter file = new FileWriter("biladerimIcin");
            file.write(songMap);

        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }




}

