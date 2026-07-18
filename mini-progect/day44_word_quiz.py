import random as rd


   # 단어 맞추기 퀴즈 프로그램 #
class word_quiz:
    def __init__(self, word, meaning):  # 단어장의 첫 단어와 뜻 입력받기

            ## 단어장 안에 단어와 뜻을 구분해서 저장하기 #
        word_dict = {}
        word_dict[word] = meaning
        self.word_dict = word_dict


    def add_word(self, word, meaning):    # 단어장에 단어와 뜻 추가하기
        self.word = word
        self.meaning = meaning
        self.word_dict[word] = meaning

    def remove_word(self, word):                # 단어장에 든 단어 삭제하기
        if word in self.word_dict:
            del self.word_dict[word]
        else:
            print(f"{word} not found in the dictionary.")

    def get_meaning(self, word):                    # 단어의 뜻을 확인하기
        if word in self.word_dict:
            return self.word_dict[word]
        else:
            return f"{word} not found in the dictionary."

    def word_list(self):                   # 단어장에 든 단어 확인하기
        return list(self.word_dict.keys())


    def quiz(self):                           # 단어 맞추기 퀴즈 시작 !
        if not self.word_dict:
            print("The word dictionary is empty. Please add some words first.")
            return

        word = rd.choice(list(self.word_dict.keys()))            # 랜덤으로 단어장의 단어 하나 가져오기
        meaning = self.word_dict[word]                            # 해당 단어의 뜻 가져오기

        print(f"What is the meaning of the word '{word}'?")
        user_answer = input("Your answer: ")                         # 유저가 뜻 맞추기

        if user_answer.strip().lower() == meaning.lower():     # 맞춘 경우
            print("Correct!")
        else:
            print(f"Incorrect. The correct meaning is: {meaning}")  # 틀린 경우

## 객체 만들기 ##

player1 = word_quiz("apple", "A fruit that is typically red, green, or yellow.")
player1.add_word("banana", "A long curved fruit that grows in clusters and has soft pulpy flesh and yellow skin when ripe.")
player1.add_word("cat", "A small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws.")

player1.quiz()

print('-' * 60)
print() 

player2 = word_quiz("dog", "A domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, and a barking, howling, or whining voice.")
player2.add_word("elephant", "A large mammal with a long trunk, tusks, and large ears.")
player2.get_meaning("dog")
player2.word_list()


player2.quiz()