import numpy as np
from midiutil.MidiFile import MIDIFile


def save_midi(pitches, tempo, rois, file_name):

    # Create the MIDIFile Object with x tracks
    MyMIDI = MIDIFile(len(rois))


    for i in range(len(rois)):
        # Tracks are numbered from zero. Times are measured in beats.
        track = i   
        time = 0
        # Add track name and tempo.
        MyMIDI.addTrackName(track,time,str(i))
        MyMIDI.addTempo(track,time,120)
        MyMIDI.addProgramChange(track,0, time, rois[i]['instrument'])

        pitch_roi = pitches[:,rois[i]['id']]

        tempo_roi = tempo[:,rois[i]['id']]

        total_time = 0

        print '- - - - - - - - - - - ', rois[i]['id'], '- - - - - - - - - - - ' 

        for j in range(len(pitches)):

            channel = 0
            pitch = pitch_roi[j]
            time = total_time
            print j, tempo_roi[j]
            duration = 0.5 / float(tempo_roi[j])
            print duration
            volume = 100
            total_time += duration

            print 'pitch:', pitch, 'time:', time, 'duration:', duration, 'tempo:', tempo_roi[j]

            #set volume. the solo is always higher
            if rois[i]['solo']:
                if tempo_roi[j] ==1:
                    volume = 100
                elif tempo_roi[j] == 2:
                    volume = 80
                elif tempo_roi[j] == 4:
                    volume = 75
                else:
                    volume = 50
            else:
                if tempo_roi[j] ==1:
                    volume = 70
                elif tempo_roi[j] == 2:
                    volume = 50
                elif tempo_roi[j] == 4:
                    volume = 45
                else:
                    volume = 20

            # Now add the note.
            MyMIDI.addNote(track,channel,pitch,time,duration, volume)



    # And write it to disk.
    binfile = open(file_name, 'wb')
    MyMIDI.writeFile(binfile)
    binfile.close()
    print 'file', file_name, 'saved.'