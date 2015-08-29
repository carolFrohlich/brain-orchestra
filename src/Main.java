import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import javax.sound.midi.MidiChannel;
import javax.sound.midi.MidiSystem;
import javax.sound.midi.Sequence;
import javax.sound.midi.Synthesizer;
import javax.sound.midi.Track;

public class Main {

	static int[] rois = {4};
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		int[][] musics = new int[236][200];
		BufferedReader br = new BufferedReader(new FileReader("/home/caroline/Documents/projects/Brain-Orchestra/data/rois2_minor_pentatonic.csv"));
		String line;
		int l = 0;
		while ((line = br.readLine()) != null) {
		    String[] cols = line.split(",");
		    for(int i = 0; i < cols.length; i++) {
		    	musics[l][i] = Integer.parseInt(cols[i]);
		    }
		    l++;
		}
		

		try {
			Synthesizer synthesizer = MidiSystem.getSynthesizer();
			synthesizer.open();
			
			MidiChannel[] channels = synthesizer.getChannels();
			
			for(int i = 0; i < 200; i++) {
				for(int j = 0; j < rois.length; j++) {
					
					int pitch = musics[i][rois[j]-1];
					//System.out.println(pitch);
					channels[0].noteOn(pitch, 85);
					
				}
				
				Thread.sleep(250);
				channels[0].allNotesOff();
			}
			
		} catch (Exception e) {e.printStackTrace();}
		
	}

}
