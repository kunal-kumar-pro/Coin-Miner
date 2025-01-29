import pyautogui
import time
import random

phrases = """She's asked the question so many times that she barely listened to the answers anymore. The answers were always the same. Well, not exactly the same, but the same in a general sense. A more accurate description was the answers never surprised her. So, she asked for the 10,000th time, "What's your favorite animal?" But this time was different. When she heard the young boy's answer, she wondered if she had heard him correctly.
Her hand was balled into a fist with her keys protruding out from between her fingers. This was the weapon her father had shown her how to make when she walked alone to her car after work. She wished that she had something a little more potent than keys between her fingers. It would have been nice to have some mace or pepper spray. He had been meaning to buy some but had never gotten around to it. As the mother bear took another step forward with her cubs in tow, she knew her fist with keys wasn't going to be an adequate defense for this situation.
It had been a simple realization that had changed Debra's life perspective. It was really so simple that she was embarrassed that she had lived the previous five years with the way she measured her worth. Now that she saw what she had been doing, she could see how sad it was. That made her all the more relieved she had made the change. The number of hearts her Instagram posts received wasn't any longer the indication of her own self-worth.
Should he write it down? That was the question running through his mind. He couldn't believe what had just happened and he knew nobody else would believe him as well. Even if he documented what had happened by writing it down, he still didn't believe anyone would still believe it. So the question remained. Was it be worth it to actually write it down?
There were about twenty people on the dam. Most of them were simply walking and getting exercise. There were a few who were fishing. There was a family who had laid down a blanket and they were having a picnic. It was like this most days and nothing seemed out of the ordinary. The problem was that nobody noticed the water leaking through the dam wall."""
word_list = phrases.split()
def generate_random_word():
    num = random.randint(0,len(word_list))
    return word_list[num]

time.sleep(7)
print(pyautogui.position())
for i in range (30):    
    string = generate_random_word()
    timer = random.randint(10,15)
    pyautogui.click(505,186,duration=1)
    pyautogui.write(string)
    pyautogui.hotkey("Enter")
    time.sleep(timer)
    pyautogui.click(895,190,duration=1)