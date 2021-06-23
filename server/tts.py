from gtts import gTTS
from pygame import mixer

class TTS:
    def __init__(self):
        # self.path = 'C:/Users/Programmer/Desktop/Projects/nlp_assignment_2/client/public/audios'
        self.sentences = []
        mixer.init()

    def init_sentences(self, sentences):
        if self.sentences == []:
            self.sentences = sentences

    def generate_audio(self, folder_name, current_index, should_play):
        print(should_play)
        if should_play == 'play':
            if self.sentences != [] and len(self.sentences) > current_index:
                tts = gTTS(
                    self.sentences[int(current_index)], lang="en", tld="co.uk")
                tts.save(f"audios/{folder_name}_{current_index}.mp3")
                self.play_sound(folder_name, current_index, should_play)
        else:
            mixer.quit()

    def play_sound(self, folder_name, index, play):
        if mixer.get_init() != None:
            mixer.music.load(f"audios/{folder_name}_{index}.mp3")
            mixer.music.play()
            while mixer.music.get_busy() == True:
                continue

            self.generate_audio(folder_name, index + 1, play)
