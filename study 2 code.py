import os
import random
from psychopy import visual, core, event, data, gui, sound
import pandas as pd


# Create a PsychoPy window
win = visual.Window(size=(800, 600), color='white')

# Prompt the user for a Dyad ID
dlg = gui.Dlg(title="Dyad ID")
dlg.addField("Enter Dyad ID:")
dlg.show()

if dlg.OK:
    dyad_id = dlg.data[0]
else:
    core.quit()

# Define conditions and instructions
conditions = [
    ("BASE", "Proceed to the coordination question."),
    ("SK (UE)", "You might be hearing the same audio as your partner or a different audio."),
    ("SK (CE)", "You are hearing the same audio as your partner. Your partner might be informed that you have the same audio too or not."),
    ("CK1", "Please take off your headphones."),
    ("CFUK", "You are hearing a different audio from your partner.")
]

# Initialize sound components for each audio file
audio_files = [
    '/Users/salim/Library/CloudStorage/OneDrive-CentralEuropeanUniversity/Fall semester 2023/Study 2/Final audios for Study 2/01.06-F.wav',
    '/Users/salim/Library/CloudStorage/OneDrive-CentralEuropeanUniversity/Fall semester 2023/Study 2/Final audios for Study 2/2004-F.wav',
    '/Users/salim/Library/CloudStorage/OneDrive-CentralEuropeanUniversity/Fall semester 2023/Study 2/Final audios for Study 2/Forget-Me-Not-F.wav',
    '/Users/salim/Library/CloudStorage/OneDrive-CentralEuropeanUniversity/Fall semester 2023/Study 2/Final audios for Study 2/Turquoise-F.wav',
    '/Users/salim/Library/CloudStorage/OneDrive-CentralEuropeanUniversity/Fall semester 2023/Study 2/Final audios for Study 2/York-F.wav'
]

# Shuffle the order of audio files and conditions
random.shuffle(audio_files[1:])
random.shuffle(conditions)

# Create a DataFrame to store the experiment data
experiment_data = pd.DataFrame(columns=["Dyad ID", "Condition", "Instruction", "Audio File"])

# Sample data
data = {
    'File Path': ['01.06-F.wav', '2004-F.wav', 'Forget-Me-Not-F.wav', 'Turquoise-F.wav', 'York-F.wav'],
    'Assigned Title': ['Date', 'Year', 'Flower', 'Color', 'City']
}

# Create a DataFrame to store the experiment data
experiment_data = pd.DataFrame(columns=["Dyad ID", "Condition", "Instruction", "Audio File"])

# Sample data
data = {
    'File Path': ['01.06-F.wav', '2004-F.wav', 'Forget-Me-Not-F.wav', 'Turquoise-F.wav', 'York-F.wav'],
    'Assigned Title': ['Date', 'Year', 'Flower', 'Color', 'City']
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)

# Create a text stimulus for instructions
instruction_text = visual.TextStim(win, color='black', height=0.06)

# Create a list of unique pairings of conditions and audio files
pairings = list(zip(conditions, audio_files))

# Randomly shuffle the pairings
random.shuffle(pairings)

# Run the trials with shuffled pairings
for (condition, instruction), audio_file in pairings:
    # Display the instruction
    instruction_text.text = instruction
    instruction_text.draw()
    win.flip()

    # Play audio (if not in BASE condition)
    if condition != "BASE" and audio_file:
        audio_sound = sound.Sound(audio_file, stereo=True, hamming=True)
        audio_sound.setVolume(1.0)
        audio_sound.play()
        core.wait(audio_sound.getDuration())  # Wait for audio duration
        audio_sound.stop()

 # Display the additional instruction after '01.06-F.wav' is played
        if "01.06-F.wav" in audio_file:
            # Create a new text stimulus for the additional instruction
            additional_instruction_red = visual.TextStim(win, text="Answer the question below. If both you and your partner give the same answer, you will win this round.",
                                                     color='red', height=0.06, bold=True, pos=(0, 0.1))
            additional_instruction_black = visual.TextStim(win, text="Write down any day of the year: (day) /(month).",
                                                     color='black', height=0.06, pos=(0, -0.05))
            additional_instruction_red2 = visual.TextStim(win, text="Remember there is not a one correct answer.",
                                                     color='red', height=0.06, bold=True, pos=(0, -0.2))
            additional_instruction_red.draw()
            additional_instruction_black.draw()
            additional_instruction_red2.draw()
            win.flip()
            event.waitKeys(keyList=['7'])  # Wait for a key press to continue

        # Display the additional instruction after '2004-F.wav' is played
        if "2004-F.wav" in audio_file:
            # Create a new text stimulus for the additional instruction
            additional_instruction_red = visual.TextStim(win, text="Answer the question below. If both you and your partner give the same answer, you will win this round.",
                                                     color='red', height=0.06, bold=True, pos=(0, 0.1))
            additional_instruction_black = visual.TextStim(win, text="Write down any year, past, present, or future.",
                                                     color='black', height=0.06, pos=(0, -0.05))
            additional_instruction_red2 = visual.TextStim(win, text="Remember there is not a one correct answer.",
                                                     color='red', height=0.06, bold=True, pos=(0, -0.2))
            additional_instruction_red.draw()
            additional_instruction_black.draw()
            additional_instruction_red2.draw()
            win.flip()
            event.waitKeys(keyList=['7'])  # Wait for a key press to continue

        # Display the additional instruction after 'Forget-Me-Not-F.wav' is played
        if "Forget-Me-Not-F.wav" in audio_file:
            # Create a new text stimulus for the additional instruction
            additional_instruction_red = visual.TextStim(win, text="Answer the question below. If both you and your partner give the same answer, you will win this round.",
                                                     color='red', height=0.06, bold=True, pos=(0, 0.1))
            additional_instruction_black = visual.TextStim(win, text="Name any flower.",
                                                     color='black', height=0.06, pos=(0, -0.05))
            additional_instruction_red2 = visual.TextStim(win, text="Remember there is not a one correct answer.",
                                                     color='red', height=0.06, bold=True, pos=(0, -0.2))
            additional_instruction_red.draw()
            additional_instruction_black.draw()
            additional_instruction_red2.draw()
            win.flip()
            event.waitKeys(keyList=['7'])  # Wait for a key press to continue

        # Display the additional instruction after 'York-F.wav' is played
        if "York-F.wav" in audio_file:
            # Create a new text stimulus for the additional instruction
            additional_instruction_red = visual.TextStim(win, text="Answer the question below. If both you and your partner give the same answer, you will win this round.",
                                                     color='red', height=0.06, bold=True, pos=(0, 0.1))
            additional_instruction_black = visual.TextStim(win, text="Name any British town or city.",
                                                     color='black', height=0.06, pos=(0, -0.05))
            additional_instruction_red2 = visual.TextStim(win, text="Remember there is not a one correct answer.",
                                                     color='red', height=0.06, bold=True, pos=(0, -0.2))
            additional_instruction_red.draw()
            additional_instruction_black.draw()
            additional_instruction_red2.draw()
            win.flip()
            event.waitKeys(keyList=['7'])  # Wait for a key press to continue
    
    # Display the additional instruction after 'Turquoise-F.wav' is played
        if "Turquoise-F.wav" in audio_file:
            # Create a new text stimulus for the additional instruction
            additional_instruction_red = visual.TextStim(win, text="Answer the question below. If both you and your partner give the same answer, you will win this round.",
                                                     color='red', height=0.06, bold=True, pos=(0, 0.1))
            additional_instruction_black = visual.TextStim(win, text="Write down any color.",
                                                     color='black', height=0.06, pos=(0, -0.05))
            additional_instruction_red2 = visual.TextStim(win, text="Remember there is not a one correct answer.",
                                                     color='red', height=0.06, bold=True, pos=(0, -0.2))
            additional_instruction_red.draw()
            additional_instruction_black.draw()
            additional_instruction_red2.draw()
            win.flip()
            event.waitKeys(keyList=['7'])  # Wait for a key press to continue

    # Wait for the '7' key press to end the trial
    keys = event.waitKeys(keyList=['7'])

    # Record the data, including the Dyad ID
    # Get the corresponding values from the 'df' DataFrame based on the audio_file
    assigned_title = df[df['File Path'] == os.path.basename(audio_file)]['Assigned Title'].values[0]
    experiment_data.loc[len(experiment_data)] = [dyad_id, condition, instruction, assigned_title]

# Append the experiment data to an existing Excel file (if it exists)
try:
    existing_data = pd.read_excel("experiment_data.xlsx")
    combined_data = pd.concat([existing_data, experiment_data], ignore_index=True)
    combined_data.to_excel("experiment_data.xlsx", index=False)
except FileNotFoundError:
    # If the file doesn't exist, create a new one
    experiment_data.to_excel("experiment_data.xlsx", index=False)

# Close the PsychoPy window
win.close()