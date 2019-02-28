import java.io.*;
import java.util.Random;
public class autoGenXML{
	public static final Random rand = new Random();
	public static final String alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	public static String [] genXML(){
				String [] rands = new String [rand.nextInt(150) + 100];
		for(int i = 0; i < rands.length; i++){
			rands[i] = generateTag();
		}
		return rands;
	}

	public static String generateTag(){
		String tag = "";
		int cond = 0;
		while(cond < rand.nextInt(25) + 1){
			tag += alpha.charAt(rand.nextInt(52)) + "";
			cond++;
		}

		String retTag = "<" + tag+ ">";
		for(int i = 0; i < rand.nextInt(10); i++){
			if(rand.nextInt(2) == 0){
				break;
			}
			retTag += generateTag();
		}
		retTag += "</" + tag+ ">";
		return retTag;
	}

	public static void main(String [] args){
		PrintWriter writer;
		for(int i = 0; i < 20; i++){
			try {
			String fileName = "input/input" + i + ".txt";
			writer = new PrintWriter(new FileWriter(fileName));
			String [] rands = genXML();
			for(int j = 0; j < rands.length; j++) {
				writer.println(rands[j]);
			}
			writer.close();
			generateAnswer(fileName, "output/output" + i +".txt" );
		} catch (IOException e) {
			System.out.println("In catch");
		}

		}
	}
	public static void generateAnswer(String inputFileName, String outputFileName) throws java.io.IOException {
	ProcessBuilder builder = new ProcessBuilder("java", "Solution");
	builder.redirectInput(new File(inputFileName));
	builder.redirectOutput(new File(outputFileName));
	builder.start();
	}
}
