'''

Order of operation:

1) Populate All_Notes, ref scale arrays (end of file)
2) Call startfunc()
3) Call mainloop()
4) Call scale_builder()
5) Exit

'''

import sys


def startfunc():
    print("Choose mode")
    print("1. Major Scale")
    print("2. Minor Scale")
    print("3. Exit")
    mainloop()


def scale_builder(Root_Note_arg, mode):
    if mode == 1:
        Ref_scale = Major_scale
        print(Root_Note_arg + " major scale is ")
    elif mode == 2:
        Ref_scale = Minor_scale
        print(Root_Note_arg + " minor scale is ")
    else:
        print("Invalid scale input")
        return

    indexNo = All_Notes.index(Root_Note_arg)

    New_scale = [Root_Note_arg]
    NoteCounter = indexNo
    for i in range(1, len(Ref_scale)):

        if Ref_scale[i - 1] == 'W':  # Loop when Whole note is in scale
            NoteCounter += 2
            if NoteCounter > 11:  # If end of 12 note array is reached, circularly shift back to 1st element
                NoteCounter = NoteCounter - 12
            New_scale.append(All_Notes[NoteCounter]) # Add new note to New_scale list

        elif Ref_scale[i - 1] == 'H':  # Loop when half note is in scale
            NoteCounter += 1
            if NoteCounter > 11:
                NoteCounter = NoteCounter - 12
            New_scale.append(All_Notes[NoteCounter])
    print(New_scale)


def mainloop():
    switch = int(input())
    if switch == 1 or switch == 2:  # Scale mode, 1 = Major, 2 = Minor
        print("Enter Root note:")
        Root_Note = (input()).upper()  # Capitalise all input to make life easier
        if Root_Note in All_Notes:
            scale_builder(Root_Note, switch)  # Call scale builder function, pass root note and mode
        else:
            print("Invalid Root note")  # Incase of rubbish input for root note

    elif switch == 3:
        sys.exit("Exit chosen...")
    else:
        print("Invalid Response. Retry.")
        startfunc()


All_Notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
Major_scale = ['W', 'W', 'H', 'W', 'W', 'W', 'H']
Minor_scale = ['W', 'H', 'W', 'W', 'H', 'W', 'W']
startfunc()
